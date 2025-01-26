import React from "react";
import { NavLink } from "react-router-dom";

function Navbar() {
  return (
    <nav className="p-4 border-b bg-white shadow-md ">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        {/* Логотип */}
        <div className="text-xl font-bold text-blue-600">Ona-Care</div>

        {/* Навигация */}
        <div className="flex space-x-6">
       
        </div>

        {/* Кнопки */}
        <div className="flex items-center space-x-4">
          <a href="#" className="text-sm text-gray-600 hover:text-black">
            Log in
          </a>
          <button className="px-4 py-2 text-sm bg-blue-500 text-white rounded-lg hover:bg-blue-600">
            Sign up
          </button>
        </div>
      </div>
    </nav>
  );
}

export default Navbar;
