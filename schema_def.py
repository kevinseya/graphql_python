from ariadne import QueryType, MutationType

# Define objetos de tipo Query y Mutation
query = QueryType()
mutation = MutationType()

# Datos de ejemplo
productos = [
    {"id": 1, "nombre": "Producto A", "precio": 10.5},
    {"id": 2, "nombre": "Producto B", "precio": 20.0},
    {"id": 3, "nombre": "Producto C", "precio": 30.75},
]

nombres = [
    {"id": 1, "nombre": "NOMBRE A"},
    {"id": 2, "nombre": "NOMBRE B"},
    {"id": 3, "nombre": "NOMBRE C"},
]

# Resolver para obtener la lista de productos
@query.field("productos")
def resolve_productos(_, info):
    return productos

# Resolver para obtener la lista de nombres
@query.field("nombres")
def resolve_nombres(_, info):
    return nombres

# Resolver para crear un nuevo nombre
@mutation.field("crearNombre")
def resolve_crear_nombre(_, info, nombre):
    nuevo_nombre = {"id": len(nombres) + 1, "nombre": nombre}
    nombres.append(nuevo_nombre)
    return nuevo_nombre

# Asegúrate de exportar explícitamente
__all__ = ["query", "mutation"]
