import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import {
  BrowserRouter,
  Navigate,
  Route,
  RouterProvider,
  createBrowserRouter,
  createRoutesFromElements,
} from "react-router-dom";

import HomeLayout from "./pages/components/layout/HomeLayout.jsx";
import Home from "./pages/Home.jsx";
import Cart from "./pages/Cart.jsx";
import Shop from "./pages/Shop.jsx";
import Login from "./pages/Login.jsx";
import Signup from "./pages/Signup.jsx";
import AddProduct from "./pages/AddProduct.jsx";
import Product from "./pages/Product.jsx";

const user = localStorage.getItem('userId')

const router = createBrowserRouter(
  createRoutesFromElements(
    <Route path="/" element={<HomeLayout />}>
      <Route index element={user ? <Navigate to="home" /> : <Navigate to="login" />} />
      <Route path="/signup" element={<Signup/>} />
      <Route path="/login" element={<Login/>} />
      <Route path="/home" element={<Home />} />
      <Route path="/shop" element={<Shop/>} />
      <Route path="/product/:productId" element={<Product/>} />
      <Route path="/addProduct" element={<AddProduct/>} />
      <Route path="/cart" element={<Cart />} />
    </Route>
  )
);


ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
