/*
import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');


  useEffect(() => {
    axios.get('http://localhost:8000/api/example/')
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error('API request failed', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>{message ? message : 'Loading...'}</p>
      </header>
    </div>
  );
}

export default App;
*/