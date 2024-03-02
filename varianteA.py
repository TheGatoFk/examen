"""
Variante A:
1. Escribe una función en Python que reciba una lista como parámetro y devuelva la suma de todos los 
elementos de la lista. 
2. Define una función llamada "inverso_palabra" que reciba una cadena como parámetro y devuelva la 
cadena invertida. Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp". 
3. Escribe un programa que pida al usuario una lista de números y luego imprima la suma de los números 
pares en la lista. 
4. Crea un diccionario en Python que represente un libro, con claves como "título", "autor" y "año de 
publicación". Luego, escribe un código que agregue un nuevo campo al diccionario, como "género", y 
lo imprima.

"""

print("\n\t  Menu Principal.\n")
print("Ejercicio1\nEjercicio2.\nEjercicio3\nEjercicio4.\nSalir. ")

try:
    opc = int(input("\nIngrese una opcion (1-5): "))
    if opc == 1:
        # Función para calcular la suma de los elementos de una lista
        def suma_lista(lista):
            return sum(lista)
        
        lista = [1, 2, 3, 4, 5]
        print("Suma de los elementos de la lista:", suma_lista(lista))
        
    elif opc == 2:
        # Función para invertir una palabra
        def inverso_palabra(cadena):
            lista = list(cadena)
            lista.reverse()
            return ''.join(lista)
        
        palabra = "animal"
        print("Inverso de la palabra:", inverso_palabra(palabra))
        
    elif opc == 3:
        # Función para calcular la suma de los números pares en una lista
        def suma_pares(lista):
            suma = 0
            numeros = input("Ingrese una lista de números separados por espacio: ").split()
            for num in numeros:
                if int(num) % 2 == 0:
                    suma += int(num)
            return suma
        
        numeros=0
        
        print("La suma de los números pares en la lista es:", suma_pares(numeros))
        
    elif opc == 4:
        # Creación de un diccionario representando el libro "El Señor Presidente"
        libro = {
            "título": "El Señor Presidente",
            "autor": "Miguel Ángel Asturias",
            "año de publicación": 1989,
            "país": "Guatemala"
        }
        libro["género"] = "Novela"
        print("Información del libro:")
        for clave, valor in libro.items():
            print(clave + ":", valor)
        
    elif opc == 5:
        print("Saliendo del programa...")
    else:
        print("Opción incorrecta. Por favor, ingrese un número del 1 al 5.")

except ValueError:
    print("Opción incorrecta. Por favor, ingrese un número del 1 al 5.")
