import React, { useContext } from "react";
import { Link } from "react-router-dom";
import { CartContext } from "../components/context/CartContext";
import { useAuth } from "../components/context/AuthContext"; // Importar el contexto de autenticación

export const Navbar = () => {
  const [cart] = useContext(CartContext); // Estado del carrito
  const { token, logout } = useAuth();   // Estado y función del contexto de autenticación

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
        {/* Link al carrito */}
        <Link to="/cart" style={navStyles}>
          <li>
            Cart items: <span className="cart-count">{quantity}</span>
          </li>
        </Link>

        {/* Mostrar "Cerrar Sesión" si el usuario está autenticado */}
        {token ? (
          <li>
            <button onClick={logout} style={{ background: "red", color: "white", border: "none", cursor: "pointer" }}>
              Cerrar Sesión
            </button>
          </li>
        ) : (
          // Mostrar "Iniciar Sesión" si el usuario no está autenticado
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
