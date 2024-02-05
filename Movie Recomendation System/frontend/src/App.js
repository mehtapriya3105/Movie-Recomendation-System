// App.js
import React, { useState } from 'react';
import './App.css';
import './components/Navbar'
function App() {
  const [movieName, setMovieName] = useState('');
  const [recommendations, setRecommendations] = useState([]);

  const handleInputChange = (e) => {
    setMovieName(e.target.value);
  };

  const handleSearch = async () => {
    // Make a request to FastAPI backend with movieName
    const response = await fetch(`http://localhost:8000/recommendations/${movieName}`);
    const data = await response.json();
    
    // Update recommendations state
    setRecommendations(data);
  };

  return (
    <>

    <div className="App">
      <h1>Movie Recommendation Engine</h1>
      <input type="text" value={movieName} onChange={handleInputChange} />
      <button onClick={handleSearch}>Get Recommendations</button>

      <div>
        <h2>Recommendations</h2>
        <ul>
        {Object.keys(recommendations).map((key) => (
      <li key={key}>{recommendations[key]}</li>
    ))}
        </ul>
      </div>
    </div>
    </>
  );
  
}

export default App;
