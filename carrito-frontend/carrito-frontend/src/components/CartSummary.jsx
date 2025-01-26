import React, {useContext, useState} from "react";
import { CartContext } from "../components/context/CartContext";
import API from "../api"

export const CartSummary = () => {

    const [cart, setCart] = useContext(CartContext);
    const [shippingOptions, setShippingOptions] = useState([]);
  
    const quantity = cart.reduce((acc, current) => {
      return acc + current.quantity;
    }, 0 );

    const totalPrice = cart.reduce((acc, current) => {
      return acc + current.quantity * current.price;
    }, 0 );

    const fetchShippingOptions = () => {
      API.post("/cart/shipping-options", { cart_total: totalPrice })
        .then((response) => {
          setShippingOptions(response.data.shipping_options);
        })
        .catch((error) => {
          console.error("Error fetching shipping options:", error);
        });
    };

  return(
    <div className="cart-container">
      <div>
        <div>Products in cart: {quantity}</div>
        <div>Total: ${totalPrice}</div>
        <button onClick={fetchShippingOptions}>Get Shipping Options</button>
        {shippingOptions.length > 0 && (
          <ul>
            {shippingOptions.map((option, index) => (
              <li key={index}>
                {option.method}: ${option.cost.toFixed(2)}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}