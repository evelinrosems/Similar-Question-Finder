from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np


class MLModels:
    def __init__(self):
        print("Loading ML Models...")

    def get_embedding(self, text):
        try:
            vectorizer = TfidfVectorizer()
            vector = vectorizer.fit_transform([text]).toarray()[0]
            return vector.tolist()
        except Exception as e:
            print(f"Embedding Error: {e}")
            return [0.0]

    def assign_topic(self, query_text):
        text = query_text.lower()

        if any(word in text for word in [
            "machine learning",
            "artificial intelligence",
            "python",
            "programming",
            "computer",
            "algorithm",
            "database",
            "software",
            "coding",
            "data structure"
        ]):
            return "Computer Science"

        elif any(word in text for word in [
            "dna",
            "cell",
            "genetics",
            "organism",
            "photosynthesis",
            "ecosystem",
            "biology",
            "human body"
        ]):
            return "Biology"

        elif any(word in text for word in [
            "gravity",
            "force",
            "motion",
            "energy",
            "electricity",
            "velocity",
            "newton",
            "physics"
        ]):
            return "Physics"

        elif any(word in text for word in [
            "acid",
            "base",
            "atom",
            "molecule",
            "compound",
            "chemical",
            "chemistry",
            "reaction"
        ]):
            return "Chemistry"

        elif any(word in text for word in [
            "equation",
            "algebra",
            "calculus",
            "geometry",
            "matrix",
            "probability",
            "statistics",
            "mathematics"
        ]):
            return "Mathematics"

        return "Computer Science"

    def compute_cosine_similarity(self, vec1, vec2):
        try:
            v1 = np.array(vec1, dtype=float)
            v2 = np.array(vec2, dtype=float)

            # Make vectors same size
            max_len = max(len(v1), len(v2))

            v1 = np.pad(v1, (0, max_len - len(v1)))
            v2 = np.pad(v2, (0, max_len - len(v2)))

            if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
                return 0.0

            similarity = np.dot(v1, v2) / (
                np.linalg.norm(v1) * np.linalg.norm(v2)
            )

            return float(similarity)

        except Exception as e:
            print(f"Cosine Similarity Error: {e}")
            return 0.0


ml_service = MLModels()
