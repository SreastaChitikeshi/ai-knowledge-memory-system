# AI Knowledge Memory System (Second Brain AI)

## Description
The AI Knowledge Memory System, also referred to as a Second Brain AI, is an intelligent personal knowledge management system that helps users store, organize, and retrieve information efficiently using artificial intelligence. Instead of relying on traditional keyword searches, this system understands the semantic meaning of user queries and retrieves the most relevant knowledge entries using Natural Language Processing (NLP) techniques and vector embeddings.

## Objectives
- Create an AI-powered personal knowledge storage system.
- Enable semantic search across stored knowledge.
- Improve knowledge recall using NLP.
- Provide intelligent responses to user queries.
- Build a personal learning assistant.

## Key Features
- **Intelligent Note Storage:** Store text notes, documents, and study content efficiently.
- **Semantic Search Capability:** Search by meaning rather than exact keywords.
- **Knowledge Embedding:** Process notes into vector embeddings using NLP models (like Sentence Transformers).
- **Fast Retrieval:** Utilize vector databases (like FAISS) for high-performance similarity search.
- **Natural Language Queries:** Ask questions in plain English and get contextual answers.
- **User-friendly Interface:** Built with Streamlit for seamless interaction.

## Technologies Used
- **Python**
- **Streamlit** (User Interface)
- **Sentence-Transformers** (Embedding Generation)
- **FAISS (cpu)** (Vector Database)
- **Scikit-learn**, **Pandas**, **Numpy** (Data Processing)
- **NLTK** (Text Preprocessing & Tokenization)

## System Architecture
The system consists of several interconnected modules:
1. **Knowledge Input Module:** Collects notes and documents.
2. **Text Processing Module:** Cleans, tokenizes, and normalizes text.
3. **Embedding Generation Module:** Converts text into NLP vector embeddings.
4. **Vector Storage Module:** Stores and indexes embeddings in a vector database.
5. **Query Processing & Semantic Search Module:** Processes user questions and finds the most similar knowledge entries using Cosine Similarity.
6. **Response Generation Module:** Formats the retrieved knowledge into a clear response.
7. **User Interface Module:** Allows input and output through Streamlit.

**System Flow:**
```
User Input Knowledge → Text Processing → Embedding Generation → Vector Database Storage
User Query → Query Embedding → Semantic Similarity Search → Knowledge Retrieval → Response Display
```

## How It Works (Algorithm)
1. **Data Ingestion:** Collect notes, text files, and documents.
2. **Preprocessing:** Lowercase conversion, punctuation removal, stop-word removal, and tokenization.
3. **Embedding Generation:** Convert processed text to numerical vectors.
4. **Knowledge Indexing:** Store vectors in FAISS.
5. **Query Processing:** Process user questions with the same NLP pipeline.
6. **Semantic Search:** Compute similarity score (e.g. Cosine Similarity) between the query vector and stored knowledge vectors.
7. **Retrieval & Response:** Return top matching entries as intelligently formatted responses.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd ai-knowledge-memory-system
   ```

2. **Create and activate a virtual environment (optional but recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the Streamlit application from your terminal:
```bash
python -m streamlit run app.py
```
Or simply:
```bash
streamlit run app.py
```
Access the web application in your browser to start adding notes and asking intelligently routed questions.

## Applications & Use Cases
- Personal learning and study assistants
- Research knowledge management
- Student note organization
- Academic knowledge retrieval
- Productivity workflows
