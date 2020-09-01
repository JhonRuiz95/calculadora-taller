
def Suma(a, b):
    return a + b

def Resta(a, b):
    return a - b


def Multiplicacion(a, b):
    return a * b


def Dividicion(a, b):
    return a / b



salir = False

while not salir:
    print("¿Que operación desea hacer? :")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


    opcion = input("Ingresa el número de la operación que deseas. ")
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    if opcion == "1":
        print("el resultado es: ")
        print(Suma(num1,num2))
    elif opcion == "2":
        print("el resultado es: ")
        print(Resta(num1,num2))
    elif opcion == "3":
        print("el resultado es: ")
        print( Multiplicacion(num1,num2))
    elif opcion == "4":
        print("el resultado es: ")
        print(Dividicion(num1,num2))
    elif opcion == "5":
        salir = True
        
    else:
        print ("Has introducido una opción no válida, recuerda que las opciones son entre 1 y 5")
print ("Fin")