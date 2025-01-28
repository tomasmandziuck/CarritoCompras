import React, { useState, useEffect } from "react";
import API from "../api";
import { Product } from "./Product";


/**
 * Displays a list of products, allowing users to add items to their cart.
 */

export const ProductList = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    API.get("/products").then((response) => setProducts(response.data));
  }, []);
  console.log(products)
  return (
    <div className="product-list">
      {products.map((product) => (
        <Product key={product.id} {...product} />
      ))}
    </div>
  );
};
