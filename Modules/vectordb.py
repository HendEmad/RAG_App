import chromadb
from Modules.embedding import load_model

embedding_model = load_model()

def build_vectordb(chunks):
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="Course")
    embeddings = embedding_model.encode(chunks)
    ids = [str(i) for i in range(len(chunks))]
    try:
        collection.delete(ids=ids)
    except:
        pass
    collection.add(
        documents=chunks,
        embeddings=embeddings.tolist(),
        ids=ids
    )
    return collection

# best match
def retrieve(question, collection):
    query_embedding = embedding_model.encode([question])
    results = collection.query(
        query_embeddings=query_embedding.tolist(),
        n_results=3
    )    
    context = results['documents'][0]
    return "\n\n".join(context)