# Proyecto GraphQL en Python

Este proyecto implementa una API GraphQL utilizando **Flask** y **Ariadne** para definir esquemas y resolvers.

## Estructura del Proyecto

- `schema_def.py`: Define los resolvers para **Query** y **Mutation**.
- `app.py`: Configura el servidor Flask y expone el endpoint `/graphql`.

## Requisitos

Asegúrate de tener instalado **Python 3.x** y las siguientes dependencias:

```bash
pip install Flask Ariadne
```
Aquí tienes el README.md en formato Markdown para tu proyecto de GraphQL en Python:

# Proyecto GraphQL en Python

Este proyecto implementa una API GraphQL utilizando **Flask** y **Ariadne** para definir esquemas y resolvers.

## Estructura del Proyecto

- `schema_def.py`: Define los resolvers para **Query** y **Mutation**.
- `app.py`: Configura el servidor Flask y expone el endpoint `/graphql`.

## Requisitos

Asegúrate de tener instalado **Python 3.x** y las siguientes dependencias:

```bash
pip install Flask Ariadne
```
## Definición del Esquema

El esquema GraphQL se define en el archivo app.py e incluye las siguientes operaciones:
Tipos
```bash
    Producto:
        id: ID del producto.
        nombre: Nombre del producto.
        precio: Precio del producto.
    Nombre:
        id: ID del nombre.
        nombre: Nombre propio.
```
Operaciones
```bash
    Query:
        productos: Devuelve la lista de productos.
        nombres: Devuelve la lista de nombres.

    Mutation:
        crearNombre(nombre: String!): Crea un nuevo nombre y lo añade a la lista.
```
## Ejecución del Servidor

1. Clona el repositorio y navega al directorio del proyecto:

git clone <https://github.com/kevinseya/graphql_python.git)>

2. Instala las dependencias:
```bash
pip install Flask Ariadne
```
3. Ejecuta el servidor:
```bash
    python app.py
```
El servidor estará disponible en http://localhost:5000/graphql.

## Interfaz GraphiQL

Puedes acceder a GraphiQL, una interfaz interactiva para hacer consultas GraphQL, visitando:
```bash
http://localhost:5000/graphql
```
Ejemplo de Consultas
Obtener Productos
```bash
query {
  productos {
    id
    nombre
    precio
  }
}
```
Obtener Nombres
```
query {
  nombres {
    id
    nombre
  }
}
```
Crear un Nombre
```bash
mutation {
  crearNombre(nombre: "Nuevo Nombre") {
    id
    nombre
  }
}
```
