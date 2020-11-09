def mostrar_menu():
    print("********** BIENVENIDO AL MENÚ DE OPERACIONES **********")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. salir")

def ingresar_numeros():
    num1 = float(input("\nDigite el primer número: "))
    num2 = float(input("Digite el segundo número: "))
    return num1, num2

def sumar(num1, num2):
    return num1 + num2

def restar(num1, num2):
    return num1 - num2

def multiplicar(num1, num2):
    return num1 * num2

def dividir(num1, num2):
    try:
        division = num1 / num2
    except ZeroDivisionError as err:
        return err
    return division

if __name__ == "__main__":
    while(True):
        mostrar_menu()
        opcion = input("\nIngrese su opción: ")
        if opcion == "1":
            print("Quieres sumar!")
            num1, num2 = ingresar_numeros()
            print("El resultado de la suma es: {}\n".format(sumar(num1, num2)))
        elif opcion == "2":
            print("Quieres restar!")
            num1, num2 = ingresar_numeros()
            print("El resultado de la resta es: {}\n".format(restar(num1, num2)))
            restar(num1, num2)
        elif opcion == "3":
            print("Quieres multiplicar!")
            num1, num2 = ingresar_numeros()
            print("El resultado de la multiplicación es: {}\n".format(multiplicar(num1, num2)))
            multiplicar(num1, num2)
        elif opcion == "4":
            print("Quieres dividir. Recuerda que la división entre cero no está definida!")
            num1, num2 = ingresar_numeros()
            division = dividir(num1, num2)
            print("El resultado de la división es: {}\n".format(division))
        elif opcion == "5":
            print("Saliendo del programa!!!")
            break
        else:
            print("Opción incorrecta!")
    
