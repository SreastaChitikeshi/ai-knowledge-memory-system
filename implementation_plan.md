# AI Knowledge Memory System - Implementation Plan

## Goal Description
Develop an AI-powered personal knowledge management system that stores user notes, processes text using NLP, converts them into embeddings, and allows semantic search using a vector database (FAISS) and Streamlit for the UI.

## Proposed Changes

### Project Setup
- We will create the project inside `c:\Users\CH_SREASTA\OneDrive\Documents\ai knowledge memory system\`.

#### [NEW] requirements.txt
Dependencies for the project: `streamlit`, `pandas`, `numpy`, `scikit-learn`, `sentence-transformers`, `faiss-cpu`, `nltk`.

#### [NEW] core.py
This file will contain the following logic:
- `TextProcessor`: Responsible for tokenization, lowercase conversion, and stop word removal using `nltk`.
- `KnowledgeBase`: Manages the FAISS index, generating embeddings via `SentenceTransformer('all-MiniLM-L6-v2')`, storing textual metadata, and executing semantic similarity searches using L2 distance/Cosine similarity via FAISS.

#### [NEW] app.py
This file will be the Streamlit web interface:
- **Add Knowledge Tab**: Form to input topic, date, and content of notes.
- **Search Knowledge Tab**: Text input to ask queries, run semantic search, and display the best matches as responses.

## Verification Plan

### Manual Verification
- We will start the Streamlit application and check if the interface loads.
- We will insert sample notes (e.g., about Neural Networks) and perform a search to verify semantics are matched accurately and returned in a clear format.
