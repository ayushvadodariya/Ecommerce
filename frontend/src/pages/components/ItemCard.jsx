import React, { useEffect } from "react";
import { useState } from "react";
import { useNavigate } from "react-router-dom";

function ItemCard({item}) {

  const navigate = useNavigate();
  const handleClick = ()=>{
    navigate(`/product/${item.id}`)
  }

  return (
    <div 
    onClick={handleClick}
    className="max-w-xs w-56 h-80 mx-auto rounded-md overflow-hidden shadow-md hover:shadow-lg">
      <div className=" relative border-l-amber-400 h-44">
        <img
          className="w-full h-full object-contain transition-transform duration-300 transform hover:scale-105"
          src={item.images[0]}
          alt="Product Image"
        />
      </div>
      <div className="p-4">
        <h3 className="text-lg font-medium mb-2 overflow-hidden" style={{
            display: "-webkit-box",
            WebkitLineClamp: 1,
            WebkitBoxOrient: "vertical",
          }}>{item.name}</h3>
        {/* <p className="text-gray-600 text-sm mb-4">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis vitae
          ante vel eros fermentum faucibus sit amet euismod lorem.
        </p> */}
        <p
          className="text-gray-600 text-sm mb-4 overflow-hidden"
          style={{
            display: "-webkit-box",
            WebkitLineClamp: 1,
            WebkitBoxOrient: "vertical",
          }}
        >
          {item.description}
        </p>
        <div className="flex items-center justify-between">
          <span className="font-bold text-lg">{`Rs. ${item.price}`}</span>
        </div>
      </div>
    </div>
  );
}

export default ItemCard;
