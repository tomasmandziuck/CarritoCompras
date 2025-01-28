import React from "react";
import { Navbar } from "./components/NavBar";
import {ProductList} from "./components/ProductList"
import { CartSummary } from "./components/CartSummary";
import { Login } from "./components/Login";
import {Register} from "./components/Register";
import ProtectedRoute from "./components/ProtectedRoute";
import { ShoppingCartProvider } from "./components/context/CartContext";
import { AuthProvider } from "./components/context/AuthContext";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

export const App = () => {
  return (
    <AuthProvider>
      <ShoppingCartProvider>
        <Router>
        <Navbar/>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/" element={<ProductList/>}/>
          <Route path="/cart"
              element={
                <ProtectedRoute>
                  <CartSummary />
                </ProtectedRoute>
              }
            />
        </Routes>
      </Router>
      </ShoppingCartProvider>
    </AuthProvider>  
  );
};
