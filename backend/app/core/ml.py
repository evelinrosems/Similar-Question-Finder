from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

class MLModels:
    def __init__(self):
        print("Loading ML Models...")

    def get_embedding(self, text):
        vectorizer = TfidfVectorizer()
        vector = vectorizer.fit_transform([text]).toarray()[0]
        return vector.tolist()

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
        v1 = np.array(vec1)
        v2 = np.array(vec2)

        if np.linalg.norm(v1) == 0 or np.linalg.norm(v2) == 0:
            return 0.0

        return float(
            np.dot(v1, v2) /
            (np.linalg.norm(v1) * np.linalg.norm(v2))
        )

ml_service = MLModels()
