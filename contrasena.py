if __name__ == "__main__":
    password = "Mao12345"
    clave = input("Digite su clave: ")

    while clave != password:
        print("Clave incorrecta!!!")
        clave = input("Digite su clave: ")

    print("Has ingresado correctamente al sistema!!!")
