import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import './Chat.css';

function Chat() {
  const [chatHistory, setChatHistory] = useState([]);
  const [currentMessage, setCurrentMessage] = useState('');
  const [questions, setQuestions] = useState([]);
  const [selectedQuestion, setSelectedQuestion] = useState('');
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [showHistory, setShowHistory] = useState(false);

  // Fetch chat history from the server on component load
  useEffect(() => {
    // You need to replace this with your actual API endpoint for chat history
    axios.get('http://localhost:3001/chat/history')
      .then((response) => {
        setChatHistory(response.data.history);
      })
      .catch((error) => {
        console.error('Error fetching chat history:', error);
      });

    // Fetch questions from the server
    axios.get('http://localhost:3001/questions')
      .then((response) => {
        setQuestions(response.data.questions);
      })
      .catch((error) => {
        console.error('Error fetching questions:', error);
      });
  }, []);

  // Function to send a new message
  const sendMessage = () => {
    // You need to replace this with your actual API endpoint for sending messages
    axios.post('http://localhost:3001/chat/send', { message: currentMessage })
      .then((response) => {
        setChatHistory([...chatHistory, response.data.message]);
        setCurrentMessage('');
      })
      .catch((error) => {
        console.error('Error sending message:', error);
      });
  };

  // Function to handle question selection
  const handleQuestionSelect = (question) => {
    setSelectedQuestion(question);
    // You need to replace this with your actual API endpoint for fetching answers
    axios.get(`http://localhost:3001/answers/${question}`)
      .then((response) => {
        setSelectedAnswer(response.data.answer);
      })
      .catch((error) => {
        console.error('Error fetching answer:', error);
      });
  };

  // Function to toggle chat history visibility
  const toggleHistory = () => {
    setShowHistory(!showHistory);
  };

  return (
    <div className="chat-container">
      <h2 className="chat-header">Chat</h2>
      <div className="chat-buttons">
        <button className="toggle-history-button" onClick={toggleHistory}>Toggle History</button>
        <button className="clear-conversation-button" onClick={() => setChatHistory([])}>Clear Conversation</button>
        <button className="logout-button">
          <Link to="/logout">Logout</Link>
        </button>
      </div>
      {showHistory && (
        <div className="chat-history">
          <h3>Chat History</h3>
          <ul>
            {chatHistory.map((message, index) => (
              <li key={index}>{message}</li>
            ))}
          </ul>
        </div>
      )}
      <div className="ask-question">
        <h3>Ask a Question</h3>
        <select className="select-question-dropdown" onChange={(e) => handleQuestionSelect(e.target.value)}>
          <option value="">Select a Question</option>
          {questions.map((question) => (
            <option key={question} value={question}>
              {question}
            </option>
          ))}
        </select>
        {selectedQuestion && (
          <div className="selected-question-answer">
            <p>Question: {selectedQuestion}</p>
            <p>Answer: {selectedAnswer}</p>
          </div>
        )}
      </div>
      <div className="message-input">
        <input
          type="text"
          placeholder="Type your message"
          value={currentMessage}
          onChange={(e) => setCurrentMessage(e.target.value)}
        />
        <button className="send-button" onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}

export default Chat;

