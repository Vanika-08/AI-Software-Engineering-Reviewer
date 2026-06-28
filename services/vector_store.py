import chromadb


class VectorStore:

    def __init__(self):

        self.client = chromadb.Client()

        self.collection = self.client.get_or_create_collection(
            name="project_review"
        )

    def store(self, chunks, embeddings):

        ids = []

        for i in range(len(chunks)):
            ids.append(str(i))

        self.collection.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )

    def search(self, query_embedding, top_k=5):

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )

        return results