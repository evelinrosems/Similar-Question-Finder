import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import api from '../services/api';

const Dashboard = () => {
  const { user } = useContext(AuthContext);
  const [question, setQuestion] = useState('');
  const [similarQuestions, setSimilarQuestions] = useState([]);
  const [submittedTopic, setSubmittedTopic] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearchAndSubmit = async (e) => {
    e.preventDefault();
    if (!question.trim()) return;

    setLoading(true);
    setError('');
    setSimilarQuestions([]);
    setSubmittedTopic('');

    try {
      // 1. First, search for similar questions
      const searchRes = await api.post('/questions/search', { text: question });
      setSimilarQuestions(searchRes.data);

      // 2. Submit the new question to database (which assigns a topic)
      const submitRes = await api.post('/questions/', { text: question });
      setSubmittedTopic(submitRes.data.topic);
      
    } catch (err) {
      console.error(err);
      setError(err.response?.data?.detail || 'An error occurred during search or submission.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <div className="content-card glassmorphism">
        <h1 className="page-title">Find Similar Questions</h1>
        <p>Type a question below. We'll automatically assign a topic (Biology, Physics, Chemistry, Mathematics, or Computer Science) and find related queries from our database using Local AI Search.</p>
        
        <form onSubmit={handleSearchAndSubmit} className="search-form">
          <input
            type="text"
            className="search-input"
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            placeholder="E.g., How do cells divide?"
            required
          />
          <button type="submit" className="btn-primary search-btn" disabled={loading}>
            {loading ? 'Processing...' : 'Search & Submit'}
          </button>
        </form>

        {error && <div className="error-message mt-4">{error}</div>}

        {submittedTopic && (
          <div className="tags-container mt-4">
            <span className="tags-label">Assigned Topic:</span>
            <div className="tags-list">
              <span className="tag">{submittedTopic}</span>
            </div>
          </div>
        )}

        {similarQuestions.length > 0 && (
          <div className="results-container mt-4">
            <h3>Similar Questions Found:</h3>
            <div className="results-list">
              {similarQuestions.map((q) => (
                <div key={q.id} className="result-card glassmorphism">
                  <div className="result-header">
                    <span className="similarity-score">Similarity: {(q.score * 100).toFixed(1)}%</span>
                  </div>
                  <p className="result-text">"{q.text}"</p>
                  <div className="tags-list mt-2">
                    <span className="tag small-tag">{q.topic}</span>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
