import React, { createContext, useState, useContext } from "react";
import API from "../../api";

// Crear el contexto
const AuthContext = createContext(null);

// Proveedor de autenticación
export const AuthProvider = ({ children }) => {
  const [token, setToken] = useState(localStorage.getItem("token") || null);

  // Función para iniciar sesión
  const login = async (email, password) => {
    try {
      const response = await API.post("/auth/login", { email, password });
      const newToken = response.data.access_token;

      // Guardar token en estado y localStorage
      setToken(newToken);
      localStorage.setItem("token", newToken);
    } catch (error) {
      console.error("Error al iniciar sesión:", error.response?.data?.message || error.message);
    }
  };

  // Función para cerrar sesión
  const logout = () => {
    setToken(null);
    localStorage.removeItem("token");
  };

  return (
    <AuthContext.Provider value={{ token, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

// Hook personalizado para usar el contexto
export const useAuth = () => useContext(AuthContext);
