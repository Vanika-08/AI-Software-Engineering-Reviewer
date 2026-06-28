from sentence_transformers import SentenceTransformer


class EmbeddingService:

    def __init__(self):

        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def create_embeddings(self, chunks):

        embeddings = self.model.encode(chunks).tolist()

        return embeddings
    
    def create_query_embedding(self, query):

        embedding = self.model.encode(query).tolist()

        return embedding