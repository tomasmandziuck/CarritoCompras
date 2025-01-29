import axios from "axios";

// Frontend API Configuration 
const API = axios.create({
  baseURL: "http://localhost:5000",
});

// Include JWT token 
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default API;