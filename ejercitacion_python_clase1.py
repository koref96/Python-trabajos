# 1. Declaración de variables y constantes
edad = 28                           # número
nombre = "Kore"                     # cadena de texto (string)
esta_estudiando = True              # booleano

# Declaración de constantes
PI = 3.14                           # número
PAIS = "Mexico"                     # cadena de texto (string)

# 2. Leer valores por teclado
edad = int(input("Introduce tu edad: "))     # leer un número entero
nombre = input("Introduce tu nombre: ")      # leer una cadena de texto
esta_estudiando = input("¿Estás estudiando? (sí/no): ").lower() == "sí"  # leer y convertir a booleano

# 3. Tipos de datos
Cantidad_de_libros = 10             # número (int)
titulo_libro = "El principito"      # cadena de texto (string)
es_interesante = True              # booleano (bool)
temas = ["aventura", "fantasía", "filosofía"]  # lista
autor = {                           # diccionario
    "nombre": "Antoine de Saint-Exupery",
    "Nacionalidad": "Francesa"
}

# Convertir tipos de datos
edad_str = str(edad)               # convertir número a cadena de texto
Cantidad_de_libros_float = float(Cantidad_de_libros)  # convertir entero a número de punto flotante

# 4. Imprimir resultados en la consola
print("Nombre:", nombre)
print("Edad:", edad)
print("¿Está estudiando?:", esta_estudiando)
print("Constante PI:", PI)
print("Constante País:", PAIS)
print("Cantidad de libros:", Cantidad_de_libros)
print("Título del libro:", titulo_libro)
print("¿Es interesante?:", es_interesante)
print("Temas del libro:", temas)
print("Autor del libro:", autor)
print("Edad (como cadena de texto):", edad_str)
print("Cantidad de libros (como float):", Cantidad_de_libros_float)