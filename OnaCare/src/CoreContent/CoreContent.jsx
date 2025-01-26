import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useState } from "react";
import Zerda from "../../public/zerda.webp";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import odin from "../../public/1.png";
import dva from "../../public/2.png";
import uch from "../../public/3.png";

function CoreContent() {
  const navigate = useNavigate(); // Правильное использование useNavigate
  
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 3000,
    arrows: true,
  };

  const slides = [
    { id: 1, src: odin, alt: "Slide 1" },
    { id: 2, src: dva, alt: "Slide 2" },
    { id: 3, src: uch, alt: "Slide 3" },
  ];

  const [activeLink, setActiveLink] = useState(null);

  const handleLinkClick = (index) => {
    setActiveLink(index);
  };

  return (
    <>
     

      <div className="container mx-auto p-4 max-w-6xl">
        <Slider {...settings}>
          {slides.map((slide) => (
            <div key={slide.id} className="px-2">
              <img
                src={slide.src}
                alt={slide.alt}
                className="w-[1100px] h-[300px] rounded-2xl shadow-lg items-center"
              />
            </div>
          ))}
        </Slider>
      </div>

      <div className="flex p-4">
        <div className="flex-row w-full max-w-6xl mx-auto flex border">
          <button
            onClick={() => navigate("/new-page")}
            className="flex-1 flex flex-col items-center justify-center p-6"
          >
            <img src={Zerda} alt="" className="w-40 h-40 rounded-xl" />
            <h3 className="text-2xl font-semibold text-gray-700">Я</h3>
            <p className="text-gray-500">Марина Тилляева</p>
          </button>

          <div className="flex-1 bg-white p-6 grid grid-cols-5 gap-4">
           
          <button className="bg-green-300 rounded-xl flex items-center justify-center text-xl font-semibold text-white py-2 border-2 border-green-700 ">
              1
            </button>
            <button className="bg-green-300 rounded-xl flex items-center justify-center text-xl font-semibold text-white py-2 border-2 border-green-700">
              2
            </button>
            <button className="bg-green-300 rounded-xl flex items-center justify-center text-xl font-semibold text-white py-2 border-2 border-green-700">
              3
            </button>
            <button className="bg-red-300 rounded-xl flex items-center justify-center text-xl font-semibold text-white py-2 border-2 border-red-700">
              4
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              5
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              6
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              7
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              8
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              9
            </button>
            <button className="bg-blue-100 rounded-xl flex items-center justify-center text-xl font-semibold text-blue-700 py-2">
              10
            </button>           
            <div className="col-span-5 text-center text-blue-700 font-medium text-lg">
              Визиты к Доктору 
            </div>

          </div>
        </div>
      </div>
    </>
  );
}

export default CoreContent;
