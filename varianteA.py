def suma_lista(lista):
    return sum(lista)

def inverso_palabra(cadena):
    return cadena[::-1]

# Función para calcular la suma de los números pares en una lista
def suma_pares(lista):
    return sum(num for num in lista if num % 2 == 0)

if __name__ == "__main__":
    # 1. Suma de los elementos de una lista
    lista = [1, 2, 3, 4, 5]
    print("Suma de los elementos de la lista:", suma_lista(lista))

    # 2. Inversión de una cadena
    palabra = "animal"
    print("Inverso de la palabra:", inverso_palabra(palabra))

    # 3. Suma de los números pares en una lista ingresada por el usuario
    numeros = [int(x) for x in input("Ingrese una lista de números separados por espacio: ").split()]
    print("La suma de los números pares en la lista es:", suma_pares(numeros))

    # 4. Creación de un diccionario representando un libro y agregando un nuevo campo
    libro = {
        "título": "El nombre del viento",
        "autor": "Patrick Rothfuss",
        "año de publicación": 2007
    }
    libro["género"] = "Fantasía"
    print("Información del libro:")
    for clave, valor in libro.items():
        print(clave + ":", valor)
