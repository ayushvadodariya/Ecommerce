import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function CartItem({ orderId }) {
  const navigate = useNavigate();
  console.log(`cart Item id${orderId}`);
  const [order, setOrder] = useState();
  const [quantity, setQuantity] = useState(0);
  const [sizes, setSizes] = useState();

  const [product, setProduct] = useState();
  const [totalPrice, setTotalPrice] = useState();
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState();

  const handleUp = async () => {
    try {
      const response = await axios.put(
        `/api/v1/order/increment_quantity/${order.id}`
      );
      setQuantity(response.data["new_quantity"]);
    } catch (error) {
      setError("Error increase contity");
    }
  };

  const handleDown = async () => {
    try {
      const response = await axios.put(
        `/api/v1/order/decrement_quantity/${order.id}`
      );
      setQuantity(response.data["new_quantity"]);
    } catch (error) {
      setError("Error increase contity");
    }
  };

  const handleOpenOrder = () => {
    navigate(`/product/${product.id}`);
  };

  useEffect(() => {
    setLoading(true);
    const fetchProduct = async () => {
      try {
        axios
          .get(`/api/v1/order/${orderId}`)
          .then((res) => {
            setOrder(res.data);
            console.log(`order is ${res.data}`);
            setQuantity(res.data.quantity);
            // Fetch product only after getting the order data
            axios
              .get(`/api/v1/product/${res.data.productId}`)
              .then((productRes) => {
                setProduct(productRes.data);
                console.log(`product is ${productRes.data}`);
                // const total = quantity * productRes.data.price;
                const quantityNum = parseInt(quantity, 10);
                const priceNum = parseFloat(productRes.data.price);
                const total = quantityNum * priceNum;
                // const total =
                // parseInt(quantity, 10) * parseFloat(productRes.data.price);

                console.log(`total is ${total}`);
                setTotalPrice(total);
                setLoading(false); // Set loading to false after fetching product
              })
              .catch((error) => {
                setError("Error fetching product details");
                setLoading(false); // Set loading to false in case of error
              });
          })
          .catch((error) => {
            setError("Error fetching order details");
            setLoading(false); // Set loading to false in case of error
          });
      } catch (error) {
        setError("Error fetching product details");
        setLoading(false); // Set loading to false in case of error
      }
    };
    fetchProduct();
  }, [orderId, quantity]); // Include orderId in the dependency array

  if (loading) return "loading.....";

  if (!order && !product) {
    return <h1> not find</h1>;
  }

  return (
    <tr>
      <td className="py-4">
        <div onClick={handleOpenOrder} className="flex items-center">
          <img
            className="h-16 w-16 mr-4"
            src={product.images[0]}
            alt="Product image"
          />
          <span className="font-semibold">
            {product.name.length > 15
              ? product.name.slice(0, 15) + "..."
              : product.name}
          </span>
        </div>
      </td>
      <td className="py-4">{product.price}</td>
      <td className="py-4">
        <div className="flex items-center">
          <button
            onClick={handleDown}
            className="border rounded-md py-2 px-4 mr-2"
          >
            -
          </button>
          <span className="text-center w-8">{order.quantity}</span>
          <button
            onClick={handleUp}
            className="border rounded-md py-2 px-4 ml-2"
          >
            +
          </button>
        </div>
      </td>
      <td className="py-4">{totalPrice}</td>
    </tr>
  );
}

export default CartItem;
