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

#funcionalidad 2

def mostrar_catalogo(libros):
    if not libros:
        print("El catálogo está vacío.")
        return

    for libro in libros:
        print(
            f"• {libro['titulo']} — {libro['autor']} — {libro['genero']} —"
            f" {libro['estado']}"
        )


mostrar_catalogo(catalogo)

#funcionalidad 3

def anadir_libro():
    """Añade un nuevo libro al catálogo."""

    print("\n--- Funcionalidad 3: Añadir un libro ---")

    titulo = input("Introduce el título del libro: ").strip()
    autor = input("Introduce la autoría del libro: ").strip()
    genero = input("Introduce el género del libro: ").strip()

    # Comprobar que los campos no estén vacíos
    if not titulo or not autor or not genero:
        print("Error: todos los campos son obligatorios.")
        return

    # Crear el nuevo libro con estado pendiente
    nuevo_libro = {
        "titulo": titulo,
        "autor": autor,
        "genero": genero,
        "estado": "pendiente"
    }

    # Añadir el libro al catálogo
    catalogo.append(nuevo_libro)

    print("\nLibro añadido correctamente.")
    print("Título:", nuevo_libro["titulo"])
    print("Autor:", nuevo_libro["autor"])
    print("Género:", nuevo_libro["genero"])
    print("Estado:", nuevo_libro["estado"])


anadir_libro()


#Funcionalidade 4

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

#Funcionalidade 5

#Numero total de libros
total_libros = len(catalogo)
print(f"Total de libros en el catalogo: {total_libros}")
#Status de lecturas
pendientes = sum(1 for libro in catalogo if libro["estado"] == "pendiente")
terminados = sum(1 for libro in catalogo if libro["estado"] == "terminado")
leyendo = sum(1 for libro in catalogo if libro["estado"] == "leyendo")
print(f"Libros pendientes: {pendientes}")
print(f"Libros terminados: {terminados}")
print(f"Libros en lectura: {leyendo}")