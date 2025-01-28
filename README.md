# Carrito de compras - Aplicación de Comercio Electrónico

Una aplicación full-stack de comercio electrónico construida con React, Flask y Go, utilizando MongoDB como base de datos. La aplicación cuenta con autenticación de usuarios, listado de productos, funcionalidad de carrito de compras y cálculos de envío.

## Tecnologías Utilizadas

### Frontend
- React.js con React Router para el enrutamiento
- Context API para el manejo de estado (Contextos de Carrito y Autenticación)
- Axios para la comunicación con la API

### Backend
- Flask (Python) para la API principal
- Microservicio en Go para cálculos de envío
- MongoDB para almacenamiento de datos
- JWT para autenticación
- Flask-CORS para manejar el intercambio de recursos de origen cruzado

### Infraestructura
- Docker y Docker Compose para containerización y orquestación

## Características

- Registro y autenticación de usuarios
- Rutas protegidas para usuarios autenticados
- Listado de productos y gestión del carrito de compras
- Cálculo dinámico de costos de envío basado en el total del carrito
- Gestión de sesiones persistente usando JWT

## Endpoints de la API

### Autenticación
- `POST /auth/register` - Registrar nuevo usuario
  - Cuerpo: `{ "email": "usuario@ejemplo.com", "password": "contraseña" }`
- `POST /auth/login` - Iniciar sesión
  - Cuerpo: `{ "email": "usuario@ejemplo.com", "password": "contraseña" }`

### Productos
- `GET /products/` - Obtener todos los productos

### Carrito
- `POST /cart/shipping-options` - Calcular opciones de envío
  - Cuerpo: `{ "cart_total": 100.00 }`

### Servicio de Envíos (Go)
- `POST /shipping-options` - Obtener tarifas de envío basadas en el total del carrito
  - Cuerpo: `{ "cart_total": 100.00 }`

## Instalación y Configuración

### Requisitos Previos
- Docker y Docker Compose

### Ejecución con Docker Compose

1. Clonar el repositorio:
```bash
git clone https://github.com/tomasmandziuck/CarritoCompras.git
cd CarritoCompras
```

2. Construir y ejecutar los contenedores:
```bash
docker-compose up --build
```

Esto iniciará todos los servicios:
- Frontend: http://localhost:5173
- API Backend: http://localhost:5000
- Servicio de Envíos: http://localhost:8080
- MongoDB: localhost:27018


## Esquema de la Base de Datos

### Colección de Productos
```javascript
{
  "_id": ObjectId,
  "name": String,
  "price": Number,
  "imgurl": String
}
```

### Colección de Usuarios
```javascript
{
  "_id": ObjectId,
  "email": String,
  "password": String (hasheada)
}
```

## Arquitectura

La aplicación sigue una arquitectura de microservicios:
- El backend principal en Flask maneja la autenticación de usuarios y la gestión de productos
- Un microservicio separado en Go maneja los cálculos de envío
- El frontend en React se comunica con ambos servicios a través de APIs REST
- MongoDB almacena los datos de usuarios y productos
- Todos los servicios están containerizados y orquestados usando Docker Compose

## Características de Seguridad

- Hasheo de contraseñas usando Werkzeug
- Autenticación basada en JWT
- Rutas protegidas tanto en frontend como en backend
- Configuración de CORS para peticiones seguras entre orígenes
- Gestión de tokens de autenticación con almacenamiento local


