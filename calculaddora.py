
def Suma(x, y):
    return x + y

def Resta(x, y):
    return x - y


def Multiplicacion(x, y):
    return x * y


def Dividicion(x, y):
    return x / y



salir = False

while not salir:
    print("¿Que operación desea hacer? :")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


    opcion = input("Ingresa el número de la operación que deseas. ")
    num1 = int(input("Ingrese el primer numero"))
    num2 = int(input("Ingrese el segundo numero"))
    if opcion == "1":
        print(Suma(num1,num2))
    elif opcion == "2":
        print(Resta(num1,num2))
    elif opcion == "3":
        print( Multiplicar(num1,num2))
    elif opcion == "4":
        print(Dividir(num1,num2))
    elif opcion == "5":
        salir = True
        
    else:
        print ("Has introducido una opción no válida, recuerda que las opciones son entre 1 y 5")
print ("Fin")