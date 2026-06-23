# Similar Question Finder with Auto-Tagging

## Assignment Option

**Option B: Similar Question Finder with Auto-Tagging**

---

## Project Overview

Similar Question Finder is a web application that allows users to register, log in, submit study questions, automatically categorize them into academic topics, and find semantically similar questions using AI/ML techniques.

The system performs semantic similarity search locally using open-source machine learning models without relying on external paid AI APIs.

---

## Features

* User Registration and Login (JWT Authentication)
* Automatic Topic Classification
* Semantic Similarity Search
* Question History Tracking
* SQLite Database Storage
* FastAPI Backend
* React Frontend

---

## Technology Stack

### Frontend

* React
* Vite
* JavaScript
* CSS

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication

### AI / ML

* Sentence Transformers
* all-MiniLM-L6-v2
* Cosine Similarity

---

## Local Setup Instructions

### Backend Setup

```bash
cd backend
pip install -r requirements.txt
python main.py
```

Backend runs on:

```text
http://localhost:8000
```

API Documentation:

```text
http://localhost:8000/docs
```

### Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend runs on:

```text
http://localhost:5173
```

---

## AI/ML Implementation

This project uses the Sentence Transformers model **all-MiniLM-L6-v2** to generate embeddings for study questions.

### Question Submission

1. User submits a question.
2. The question is converted into a vector embedding.
3. Cosine similarity is used to compare the embedding with predefined topic embeddings.
4. The most relevant topic is automatically assigned.
5. Question data is stored in SQLite.

### Similar Question Search

1. Search query is converted into an embedding.
2. Stored question embeddings are retrieved from the database.
3. Cosine similarity is calculated between the query and stored questions.
4. Results are ranked by similarity score.
5. Top matching questions are returned to the user.

All AI functionality runs locally using open-source libraries.

No external paid AI APIs such as OpenAI, Gemini, or Claude are used.

---

## Project Structure

```text
Similar-Question-Finder/
│
├── backend/
│   ├── app/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
└── README.md
```

---

## Author

Evelin Rose M S
MCA Student
