# Leave Policy RAG Chatbot

A Retrieval-Augmented Generation (RAG) chatbot built using LangChain, Google Gemini, and FAISS. The chatbot answers questions based on the content of a PDF document by retrieving relevant information from a vector database and generating context-aware responses.

## Features

* PDF document loading
* Text chunking with overlap
* Google Gemini Embeddings
* FAISS Vector Database
* Similarity Search Retrieval
* Gemini 2.5 Flash LLM Integration
* Interactive Command-Line Chatbot
* Modular Project Structure

## Project Architecture

```text
PDF Document
     ↓
Document Loader
     ↓
Chunking
     ↓
Embeddings
     ↓
FAISS Vector Store
     ↓
Retriever
     ↓
Prompt Augmentation
     ↓
Gemini 2.5 Flash
     ↓
Answer Generation
```

## Project Structure

```text
rag-chatbot/
│
├── data/
│   └── sample.pdf
│
├── vectorstore/
│   └── faiss_index/
│
├── src/
│   ├── loader.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vector_db.py
│   ├── retriever.py
│   ├── llm.py
│   └── rag_pipeline.py
│
├── ingest.py
├── app.py
├── requirements.txt
├── .env
└── README.md
```

## Technologies Used

* Python
* LangChain
* Google Gemini API
* FAISS
* PyPDF
* Python Dotenv

## Installation

### Clone Repository

```bash
git clone <your-github-repository-url>
cd rag-chatbot
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

## Build Vector Database

Place your PDF inside:

```text
data/sample.pdf
```

Run:

```bash
python ingest.py
```

This process:

* Loads the PDF
* Splits the document into chunks
* Generates embeddings
* Creates a FAISS vector database

Generated files:

```text
vectorstore/faiss_index/
├── index.faiss
└── index.pkl
```

## Run Chatbot

```bash
python app.py
```

Example:

```text
Ask Question: What is the minimum attendance requirement?

Answer:
Students must maintain a minimum attendance of 75 percent.
```

## Sample Questions

```text
What is the admission policy?

What is the minimum attendance requirement?

How many books can students borrow?

What is the hostel curfew time?

Can students use mobile phones during examinations?

How can students apply for leave?

What services are provided by the placement cell?

What is the anti-ragging policy?
```

## RAG Workflow

### Retrieval

* User question is converted into embeddings.
* FAISS retrieves the most relevant chunks.

### Augmentation

* Retrieved chunks are combined into context.

### Generation

* Gemini 2.5 Flash generates an answer using the retrieved context.

## Learning Outcomes

This project demonstrates:

* Document Loading
* Metadata Handling
* Text Chunking
* Vector Embeddings
* Vector Databases
* Similarity Search
* Retrieval-Augmented Generation
* LangChain Integration
* Google Gemini Integration

## Future Improvements

* FastAPI Backend
* React Frontend
* Chat History
* Multiple PDF Support
* Metadata Filtering
* Hybrid Search
* ChromaDB Integration
* Pinecone Integration
* User Authentication
* Cloud Deployment

## Author
Dineshkarthick
last updated 
June - 2026



MIT License
Copyright (c) 2026 Dineshkarthick