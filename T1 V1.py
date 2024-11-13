def greet(name, last_name="NO TIENE APELLIDO"):
    print("Hola", name, last_name )
greet("Nashla", "Quezada")
greet ("JUAN")
greet(last_name="Quezada", name= "Nashla")

def add(a, b):
    return a+b

def substract(a,b):
    return a-b

def multiply(a,b):
    return a*b 

def divide(a,b):
    return a/b 

def calculator():

    while True:
        print ("seleccione una operacion")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicar")
        print("4. Division")
        print("5. Salir")

        option = (input("ingrese su opcion(1,2,3,4,5): "))

        if option == "5":
            print("Saliendo de la Calculadora")
            break

        if option in ["1","2","3","4"]:
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))

            if option == "1":
                print("La Suma es: ", add(num1, num2))
            elif option == "2":
                print("La Resta es: ", substract(num1, num2))
            elif option == "3":
                print("La Multiplicación es: ", multiply(num1, num2))
            elif option == "4":
                print("La División es: ", divide(num1, num2))

        else: 
            print("Opcion no valida, por favor intenta de nuevo")

calculator()


