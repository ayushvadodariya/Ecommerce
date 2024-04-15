import React, { useEffect } from "react";
import { useState } from "react";
import ItemCard from "./components/ItemCard";
import axios from "axios";

function Shop() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // // setProducts([1, 1, 1]);
    // const products = [
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    //   { name: "tshirt", price: "2000", description: "hellloo" },
    // ];
    // setProducts(products);
    async function getProducts() {
      const response = await axios.get("/api/v1/product");
      setProducts(response.data);
    }
    try {
      getProducts();
    } catch (error) {
      console.log(`Problem to fetch data from server ${error}`);
    }
  }, []);

  return (
    <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 xl:grid-cols-5 gap-4 p-2">
      {products.map((item, index) => {
        return (
            <ItemCard key={index} item={item} />
        );
      })}
    </div>
  );
}

export default Shop;
