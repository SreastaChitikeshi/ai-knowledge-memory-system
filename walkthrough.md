# AI Knowledge Memory System - Walkthrough

## Overview
The AI Knowledge Memory System acts as a "Second Brain" to intelligently store, process, and retrieve user notes and text study materials using Natural Language Processing (NLP) and vector embeddings. It was built using Python, `sentence-transformers`, `faiss-cpu`, and Streamlit for the user interface.

## Changes Made
- **[NEW] [requirements.txt](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/requirements.txt)**: Added core dependencies allowing reproducibility (`streamlit`, `pandas`, `scikit-learn`, `sentence-transformers`, `faiss-cpu`, `nltk`).
- **[NEW] [core.py](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/core.py)**: Created the backend system managing text processing and memory storage.
  - Implemented [TextProcessor](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/core.py#26-45) to handle lowercase conversion, removing punctuation, and standardizing stopword removal using `nltk`.
  - Implemented [KnowledgeBase](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/core.py#46-127) to generate semantic encodings via `SentenceTransformer('all-MiniLM-L6-v2')` and store vector embeddings locally using `faiss`. It also maintains tabular data of text concepts using `pandas`.
- **[NEW] [app.py](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/app.py)**: Developed the Streamlit interface with two main functions:
  - **Add Knowledge**: A user form to add new knowledge nodes based on Topic, Date, and their Content text.
  - **Search Knowledge**: A query box to execute a semantic search on the added text chunks and visually render the closest matching topic snippets.

## Validation Results
We ran tests ensuring the following flow works correctly:
1. [core.py](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/core.py) successfully added memory nodes to the FAISS index database:
    - Example Note: "Backpropagation is used to update weights in neural networks using gradient descent."
2. [core.py](file:///c:/Users/CH_SREASTA/OneDrive/Documents/ai%20knowledge%20memory%20system/core.py) correctly resolved similarity matches when queried with completely different words but identical semantics (e.g. querying "What updates weights in neural networks?" retrieves the backpropagation node).

All libraries and downloads (`nltk` models and `huggingface` models) have been securely fetched and evaluated locally.

### How to Run Locally
Open a terminal in the project directory where the files have been created (`c:\Users\CH_SREASTA\OneDrive\Documents\ai knowledge memory system`) and execute:
```bash
python -m streamlit run app.py
```
This will automatically launch the web application in your browser.
