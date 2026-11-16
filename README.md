# RAG Project
user [pdf] --> chat [pdf]
user [query/ question] --> Embedding [vectors] --> save it [vector database]
pdf [docs] --> Embedding [vectors] --> save it [vector database]
model [similarity_best_match]
context [query + retrieved text] --> llm model --> generate response

# Features
- pdf ingestion (text extract)
- embedding generation for document content
- vector database to store documnets embeddings
- context-aware retrieval for user question/query
- prompt-based response generation

## How to use the repo?
1- Clone repo on your machine
2- Copy content of `.env.example` to yout own `.env` file: 
```cp .env.example .env```

## Issues
[Task] create pdf_utils file
- Description:
    1) extract text from pdf
    2) chunking

[Task] Create embedding.py file
- Description:
    1) load embedding model
    2) Text --> vectors

[Task] create vector database file
Description:
    - Create client
    - create collection
    - add docs embedding vectors to the database
Database [chromadb]

[Task] create llm file
- Use Gemmini API

[Task] create best prompt
- use prompt engineering techniques

[Task] Create App
- Use streamlit

## Project structure
Modules/
    __initi__.py
    pdf_utils.py
    embedding.py
    llm.py
    vectordb.py

Prompts/
    prompt.txt

.env
README.md
requirements.txt