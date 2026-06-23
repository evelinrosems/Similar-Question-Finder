from sentence_transformers import SentenceTransformer
import numpy as np

class MLModels:
    def __init__(self):
        print("Loading Sentence Transformer model...")
        self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
        
        self.topics = [
            "Biology",
            "Physics",
            "Chemistry",
            "Mathematics",
            "Computer Science"
        ]
        
        print("Pre-computing topic embeddings...")
        # Encode all topics once
        self.topic_embeddings = self.embedding_model.encode(self.topics)
        
        print("ML Models loaded successfully.")

    def get_embedding(self, text: str) -> list[float]:
        # Generate dense vector embedding
        embedding = self.embedding_model.encode(text)
        return embedding.tolist()

    def assign_topic(self, query_embedding: list[float]) -> str:
        # Convert query embedding to numpy array
        query_vec = np.array(query_embedding)
        
        # Calculate cosine similarity between query and all topics
        # dot product / (norm(query) * norm(topics))
        scores = np.dot(self.topic_embeddings, query_vec) / (
            np.linalg.norm(self.topic_embeddings, axis=1) * np.linalg.norm(query_vec)
        )
        
        # Find index of max score
        best_idx = np.argmax(scores)
        return self.topics[best_idx]

    def compute_cosine_similarity(self, vec1: list[float], vec2: list[float]) -> float:
        v1 = np.array(vec1)
        v2 = np.array(vec2)
        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
            return 0.0
        return float(np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2)))

# Singleton instance
ml_service = MLModels()
