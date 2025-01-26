import React from "react";
import { useAuth } from "../context/AuthContext";

export const LogoutButton = () => {
  const { logout } = useAuth();

  return <button onClick={logout}>Cerrar Sesión</button>;
};

export default LogoutButton;
