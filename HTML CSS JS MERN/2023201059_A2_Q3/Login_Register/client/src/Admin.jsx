import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './Admin.css';

function Admin() {
  const [questions, setQuestions] = useState([]);
  const [newQuestion, setNewQuestion] = useState('');
  const [newAnswer, setNewAnswer] = useState('');
  const [selectedQuestion, setSelectedQuestion] = useState('');
  const [selectedAnswer, setSelectedAnswer] = useState('');

  // Fetch questions from the server on component load
  useEffect(() => {
    // You need to replace this with your actual API endpoint for fetching questions
    axios.get('http://localhost:3001/questions')
      .then((response) => {
        setQuestions(response.data.questions);
      })
      .catch((error) => {
        console.error('Error fetching questions:', error);
      });
  }, []);

  // Function to add a new question to the database
  const addNewQuestion = () => {
    // You need to replace this with your actual API endpoint for adding questions
    axios.post('http://localhost:3001/questions', { question: newQuestion, answer: newAnswer })
      .then((response) => {
        setQuestions([...questions, response.data.question]);
        setNewQuestion('');
        setNewAnswer('');
      })
      .catch((error) => {
        console.error('Error adding question:', error);
      });
  };

  // Function to update an existing question and its answer
  const updateQuestion = () => {
    // You need to replace this with your actual API endpoint for updating questions
    axios.put(`http://localhost:3001/questions/${selectedQuestion}`, { answer: selectedAnswer })
      .then(() => {
        // Update the questions array with the updated question and answer
        setQuestions((prevQuestions) => {
          return prevQuestions.map((question) => {
            if (question === selectedQuestion) {
              return { question: selectedQuestion, answer: selectedAnswer };
            }
            return question;
          });
        });
        setSelectedQuestion('');
        setSelectedAnswer('');
      })
      .catch((error) => {
        console.error('Error updating question:', error);
      });
  };


  return (
    <div className="admin-container">
      <h2 className="admin-header">Admin Page</h2>
      <div className="add-question">
        <h3>Add New Question</h3>
        <input
          type="text"
          placeholder="New Question"
          value={newQuestion}
          onChange={(e) => setNewQuestion(e.target.value)}
        />
        <input
          type="text"
          placeholder="Answer"
          value={newAnswer}
          onChange={(e) => setNewAnswer(e.target.value)}
        />
        <button onClick={addNewQuestion}>Add</button>
      </div>
      <div className="edit-question">
        <h3>Edit Existing Question</h3>
        <select
          onChange={(e) => {
            const selected = e.target.value;
            setSelectedQuestion(selected);
            const answer = questions.find((q) => q.question === selected)?.answer || '';
            setSelectedAnswer(answer);
          }}
        >
          <option value="">Select a Question</option>
          {questions.map((question) => (
            <option key={question.question} value={question.question}>
              {question.question}
            </option>
          ))}
        </select>
        {selectedQuestion && (
          <div>
            <input
              type="text"
              placeholder="Answer"
              value={selectedAnswer}
              onChange={(e) => setSelectedAnswer(e.target.value)}
            />
            <button onClick={updateQuestion}>Update</button>
          </div>
        )}
      </div>
    </div>
  );
}

export default Admin;