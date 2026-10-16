catalogo = [
        {
            "titulo": "La casa del faro",
            "autor": "Ana Martín",
            "genero": "Misterio",
            "estado": "pendiente",
        },
        {
            "titulo": "Viaje a Marte",
            "autor": "Lucía Pérez",
            "genero": "Ciencia ficción",
            "estado": "terminado",
        },
        {
            "titulo": "El jardín de las sombras",
            "autor": "Carlos Ruiz",
            "genero": "Fantasía",
            "estado": "leyendo",
        },
        {
            "titulo": "Cartas desde el mar",
            "autor": "Marta Soler",
            "genero": "Romance",
            "estado": "pendiente",
        },
        {
            "titulo": "El último tren",
            "autor": "Jorge Vidal",
            "genero": "Novela negra",
            "estado": "terminado",
        },
    ]

def buscar_por_estado():
    estado_buscado = input(
        "Introduce el estado (pendiente, leyendo, terminado): "
    ).strip().lower()

    encontrados = 0

    for libro in catalogo:
        if libro["estado"] == estado_buscado:
            print("\nTítulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            print("Estado:", libro["estado"])
            encontrados += 1

    if encontrados == 0:
        print("No hay libros con ese estado.")
buscar_por_estado()
def buscar_por_estado():
    estado_buscado = input(
        "Introduce el estado (pendiente, leyendo, terminado): "
    ).strip().lower()

    encontrados = 0

    for libro in catalogo:
        if libro["estado"] == estado_buscado:
            print("\nTítulo:", libro["titulo"])
            print("Autor:", libro["autor"])
            print("Género:", libro["genero"])
            print("Estado:", libro["estado"])
            encontrados += 1

    if encontrados == 0:
        print("No hay libros con ese estado.")
buscar_por_estado()