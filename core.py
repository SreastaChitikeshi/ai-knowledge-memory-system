import os
import pandas as pd
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string

# Download NLTK data (only runs if not already downloaded)
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt_tab')
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')


class TextProcessor:
    def __init__(self):
        self.stop_words = set(stopwords.words('english'))

    def process(self, text):
        if not text:
            return ""
        
        # Lowercase conversion
        text = text.lower()
        
        # Removing punctuation
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Tokenization and Stop word removal
        tokens = word_tokenize(text)
        cleaned_tokens = [word for word in tokens if word not in self.stop_words]
        
        return " ".join(cleaned_tokens)

class KnowledgeBase:
    def __init__(self, data_file="knowledge_base.csv", index_file="knowledge_index.faiss"):
        self.data_file = data_file
        self.index_file = index_file
        self.processor = TextProcessor()
        
        # Initialize embedding model
        # Using a reliable lightweight model
        self.encoder = SentenceTransformer('all-MiniLM-L6-v2')
        self.embedding_dimension = self.encoder.get_sentence_embedding_dimension()
        
        # Initialize FAISS Index
        if os.path.exists(self.index_file):
            self.index = faiss.read_index(self.index_file)
        else:
            # L2 distance (Euclidean) or Inner Product (Cosine Similarity for normalized vectors)
            self.index = faiss.IndexFlatL2(self.embedding_dimension)
            
        # Initialize Knowledge Storage
        if os.path.exists(self.data_file):
            self.df = pd.read_csv(self.data_file)
        else:
            self.df = pd.DataFrame(columns=["id", "topic", "date", "content", "cleaned_content"])

    def add_knowledge(self, topic, date, content):
        # 1. Clean the text
        cleaned_content = self.processor.process(content)
        
        # 2. Combine for embedding (Topic + Content semantics matter)
        text_to_embed = f"{topic}. {cleaned_content}"
        
        # 3. Generate embedding
        vector = self.encoder.encode([text_to_embed])[0]
        vector = np.array([vector]).astype('float32')
        
        # 4. Add to FAISS index
        _id = int(self.index.ntotal)
        self.index.add(vector)
        faiss.write_index(self.index, self.index_file)
        
        # 5. Store in DataFrame
        new_entry = pd.DataFrame({
            "id": [_id],
            "topic": [topic],
            "date": [date],
            "content": [content],
            "cleaned_content": [cleaned_content]
        })
        self.df = pd.concat([self.df, new_entry], ignore_index=True)
        self.df.to_csv(self.data_file, index=False)
        
        return True

    def query_knowledge(self, user_query, top_k=3):
        if self.index.ntotal == 0:
            return []
            
        # 1. Process query
        cleaned_query = self.processor.process(user_query)
        
        # 2. Generate embedding
        query_vector = self.encoder.encode([cleaned_query])[0]
        query_vector = np.array([query_vector]).astype('float32')
        
        # 3. Semantic Search
        k = min(top_k, self.index.ntotal)
        distances, indices = self.index.search(query_vector, k)
        
        results = []
        for i in range(k):
            idx = indices[0][i]
            if idx != -1: # Valid hit
                match = self.df[self.df["id"] == idx].iloc[0]
                results.append({
                    "topic": match["topic"],
                    "date": match["date"],
                    "content": match["content"],
                    "distance": float(distances[0][i])
                })
                
        return results
