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