import React, { createContext, useState, useContext } from "react";
import API from "../../api";

const AuthContext = createContext(null);

  /**
   * Provides authentication state and functions.
   */

export const AuthProvider = ({ children }) => {

  const [token, setToken] = useState(localStorage.getItem("token") || null);

  // Login function
  const login = async (email, password) => {
    try {
      const response = await API.post("/auth/login", { email, password });
      const newToken = response.data.access_token;

      // Save token and localstorage
      setToken(newToken);
      localStorage.setItem("token", newToken);
    } catch (error) {
      console.error("Error al iniciar sesión:", error.response?.data?.message || error.message);
    }
  };

  // Logout Function
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

// Hook to access authentication state and functions.
export const useAuth = () => useContext(AuthContext);
