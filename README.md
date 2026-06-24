# Similar Question Finder with Auto-Tagging

## Assignment Option

**Option B: Similar Question Finder with Auto-Tagging**

---

## Project Overview

Similar Question Finder is a web application that allows users to register, log in, submit study questions, automatically categorize them into academic topics, and find similar questions using AI/ML techniques.

The system performs similarity search locally using open-source machine learning libraries without relying on external paid AI APIs.

---

## Features

* User Registration and Login (JWT Authentication)
* Automatic Topic Classification
* Similar Question Search
* Question History Tracking
* SQLite Database Storage
* FastAPI Backend
* React Frontend

---

## Live Demo

### Frontend

https://similar-question-finder-rosy.vercel.app

### Backend API

https://similar-question-finder.onrender.com

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

* Scikit-learn
* TF-IDF Vectorization
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

This project uses Scikit-learn's TF-IDF Vectorizer to convert study questions into vector representations.

### Question Submission

1. User submits a question.
2. The question is converted into a TF-IDF vector.
3. A topic is automatically assigned using keyword-based classification.
4. The question and metadata are stored in the SQLite database.

### Similar Question Search

1. The search query is converted into a TF-IDF vector.
2. Stored question vectors are retrieved.
3. Cosine similarity is calculated between the query and stored questions.
4. Results are ranked according to similarity score.
5. Top matching questions are displayed to the user.

All AI/ML processing runs locally within the FastAPI backend using open-source libraries.

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

**Evelin Rose M S**
MCA Student
