if __name__ == "__main__":
    suma = 0
    while True:
        print("*"*20, " BIENVENIDO ", "*"*20)
        print("1. Insertar un número para sumar.")
        print("2. Mostrar la suma total.")
        print("3. Salir.")
        print("*"*54)
        opcion = input("Digite una opción: ")

        if opcion == "1":
            numero = int(input("Digite el número a sumar: "))
            suma = suma + numero
        elif opcion == "2":
            print("La suma total es: {}".format(suma))
        elif opcion == "3":
            break
        else:
            print("Opción incorrecta. Intente nuevamente!!!")
    
