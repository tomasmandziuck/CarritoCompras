import React, {useContext} from "react";
import { CartContext } from "../components/context/CartContext";

export const CartSummary = () => {

    const [cart, setCart] = useContext(CartContext);
  
    const quantity = cart.reduce((acc, current) => {
      return acc + current.quantity;
    }, 0 );

    const totalPrice = cart.reduce((acc, current) => {
      return acc + current.quantity * current.price;
    }, 0 );

  return(
    <div className="cart-container">
      <div>
        <div>Products in cart: {quantity}</div>
        <div>Total: ${totalPrice}</div>
      </div>
    </div>
  )
}