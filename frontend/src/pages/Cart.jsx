import React, { useEffect, useState } from "react";
import axios from "axios";
import Product from "./Product";
import CartItem from "./components/cartItem";

function Cart() {
  const userId = localStorage.getItem("userId");

  const [cart, setCart] = useState();
  const [subTotal, setSubTotal] = useState();
  const [error, setError] = useState();

  useEffect(() => {
    const fetchProduct = async () => {
      try {
        console.log(`${userId}`);
        axios.get(`/api/v1/cart/${userId}`)
        .then((res)=>{
          setCart(res.data.cart_list);
          console.log(`${res.data.cart_list}`);
          console.log(`cart is ${cart}`);
          axios.post(`/api/v1/cart/total-price`, {
            "order_ids": res.data.cart_list
          }).then((res)=>{
            console.log(`sub total price is ${res.data.total_price}`);
            setSubTotal(res.data.total_price);
            setSubTotal();
          });

        });
      } catch (error) {
        setError("Error fetching product details");
      }
      // try {
      //   console.log(`${userId}`);
      //   const response = await axios.get(`/api/v1/cart/${userId}`);
      //   setCart(response.data.cart_list);
      //   console.log(`${response.data.cart_list}`);
      //   console.log(`cart is ${cart}`);
      //   const subtotalResponse = await axios.get(`/api/v1/cart/tota-price`, {
      //     "order_ids": response.data.cart_list
      //   });
      //   setSubTotal(response.data.total_price);
      // } catch (error) {
      //   setError("Error fetching product details");
      // }
    };

    fetchProduct();
  }, []);

  if (error) {
    return <p>{error}</p>;
  }

  if (!cart) {
    return <p>Loading...</p>;
  }
  return (
    <div className="bg-gray-100 h-screen py-8">
      <div className="container mx-auto px-4">
        <h1 className="text-2xl font-semibold mb-4">Shopping Cart</h1>
        <div className="flex flex-col md:flex-row gap-4">
          <div className="md:w-3/4">
            <div className="bg-white rounded-lg shadow-md p-6 mb-4">
              <table className="w-full">
                <thead>
                  <tr>
                    <th className="text-left font-semibold">Product</th>
                    <th className="text-left font-semibold">Price</th>
                    <th className="text-left font-semibold">Quantity</th>
                    <th className="text-left font-semibold">Total</th>
                  </tr>
                </thead>
                <tbody>
                  {!cart ? (
                    <></>
                  ) : (
                    cart.map((orderId, index) => (
                      <CartItem key={index} orderId={orderId} />
                    ))
                  )}
                </tbody>
              </table>
            </div>
          </div>
          <div className="md:w-1/4">
            <div className="bg-white rounded-lg shadow-md p-6">
              <h2 className="text-lg font-semibold mb-4">Summary</h2>
              <div className="flex justify-between mb-2">
                <span>Subtotal</span>
                <span>{subTotal}</span>
              </div>
              {/* <div className="flex justify-between mb-2">
                <span>Taxes</span>
                <span>$1.99</span>
              </div> */}
              <div className="flex justify-between mb-2">
                <span>Shipping</span>
                <span>free</span>
              </div>
              <hr className="my-2" />
              <div className="flex justify-between mb-2">
                <span className="font-semibold">Total</span>
                <span className="font-semibold">$21.98</span>
              </div>
              <button className="bg-blue-500 text-white py-2 px-4 rounded-lg mt-4 w-full">
                Checkout
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Cart;
