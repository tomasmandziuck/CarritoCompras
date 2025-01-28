import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { CartContext } from "../components/context/CartContext";
import { useAuth } from "../components/context/AuthContext"; 

  /**
   * Displays the navigation bar with links to the store and cart.
   * Also shows the total number of items in the cart.
   */
  
export const Navbar = () => {

  const [cart] = useContext(CartContext); 
  const { token, logout } = useAuth();  

  const quantity = cart.reduce((acc, current) => {
    return acc + current.quantity;
  }, 0);

  

  const navStyles = {
    color: "#fff",
    listStyle: "none",
    textDecoration: "none",
  };

  return (
    <nav>
      <Link to="/" style={navStyles}>
        <h2>Store</h2>
      </Link>

      <ul className="nav-list">
        <Link to="/cart" style={navStyles}>
          <li>
            Cart items: <span className="cart-count">{quantity}</span>
          </li>
        </Link>

        {/* Show "Cerrar Sesión" if the user is authenticated */}
        {token ? (
          <li>
            <button onClick={logout} style={{ background: "red", color: "white", border: "none", cursor: "pointer" }}>
              Cerrar Sesión
            </button>
          </li>
        ) : (
          // Show "Iniciar Sesión" if user is not authenticated
          <Link to="/login" style={navStyles}>
            <li>Iniciar Sesión</li>
          </Link>
        )}
        <Link to="/register" style={navStyles}>
            <li>Registrarse</li>
          </Link>
      </ul>
    </nav>
  );
};
