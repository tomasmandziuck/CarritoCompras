import React, { createContext, useState } from "react";

export const CartContext = createContext(null);

/**
 * Provides cart state and functions for managing items in the cart.
 */

export const ShoppingCartProvider = ({ children }) => {
  const [cart, setCart] = useState([]);

  return (
  <CartContext.Provider value={[cart, setCart]}>
    {children}
  </CartContext.Provider>
  );
};