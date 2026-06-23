import React, { useEffect, useState } from 'react';
import api from '../services/api';

const History = () => {
  const [history, setHistory] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHistory = async () => {
      try {
        const response = await api.get('/questions/history');
        setHistory(response.data);
      } catch (error) {
        console.error("Failed to fetch history", error);
      } finally {
        setLoading(false);
      }
    };
    fetchHistory();
  }, []);

  if (loading) {
    return <div className="loading">Loading history...</div>;
  }

  return (
    <div className="page-container">
      <div className="content-card glassmorphism">
        <h1 className="page-title">Your Question History</h1>
        <p>Review the questions you've asked and their automatically assigned topics.</p>
        
        <div className="history-list">
          {history.length === 0 ? (
            <div className="history-item">
              <span>No questions submitted yet. Try asking something in the Dashboard!</span>
            </div>
          ) : (
            history.map((q) => (
              <div key={q.id} className="history-item glassmorphism">
                <p className="history-text">"{q.text}"</p>
                <div className="history-meta mt-2">
                  <div className="tags-list">
                    <span className="tag small-tag">{q.topic}</span>
                  </div>
                  <span className="history-date">
                    {new Date(q.created_at).toLocaleDateString()}
                  </span>
                </div>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
};

export default History;
