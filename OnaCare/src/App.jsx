import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import CoreContent from "./CoreContent/CoreContent"; 
import About from "./CoreContent/About"; 
import Navbar from "./Components/Navbar"; 

function App() {
  return (
    <Router>
      {/* Навигация */}
      <Navbar />
      
      {/* Контент */}
      <Routes>
        <Route path="/" element={<CoreContent />} />
        <Route path="/new-page" element={<About />} />
      </Routes>
    </Router>
  );
}

export default App;
