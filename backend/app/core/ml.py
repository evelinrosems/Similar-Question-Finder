from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class MLModels:
    def __init__(self):
        print("Loading TF-IDF model...")

        self.topics = [
            "Biology",
            "Physics",
            "Chemistry",
            "Mathematics",
            "Computer Science"
        ]

        self.vectorizer = TfidfVectorizer()
        self.topic_vectors = self.vectorizer.fit_transform(self.topics)

        print("ML Models loaded successfully.")

    def get_embedding(self, text):
        vector = self.vectorizer.transform([text]).toarray()[0]
        return vector.tolist()

    def assign_topic(self, query_embedding):
        query_vec = np.array(query_embedding)

        scores = []

        for topic_vec in self.topic_vectors.toarray():
            if np.linalg.norm(topic_vec) == 0 or np.linalg.norm(query_vec) == 0:
                scores.append(0)
            else:
                score = np.dot(topic_vec, query_vec) / (
                    np.linalg.norm(topic_vec) * np.linalg.norm(query_vec)
                )
                scores.append(score)

        best_idx = np.argmax(scores)
        return self.topics[best_idx]

    def compute_cosine_similarity(self, vec1, vec2):
        v1 = np.array(vec1)
        v2 = np.array(vec2)

        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
            return 0.0

        return float(
            np.dot(v1, v2) /
            (np.linalg.norm(v1) * np.linalg.norm(v2))
        )

ml_service = MLModels()
