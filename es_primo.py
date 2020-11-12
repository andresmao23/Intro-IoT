def es_primo(numero):
    contador = 0
    for i in range(1, numero):
        if (numero % i) == 0:
            contador += 1

    if contador <= 2:
        print("El número {} es primo!".format(numero))
    else:
        print("El número {} NO es primo!".format(numero))

if __name__ == "__main__":
    numero = int(input("Digite el número: "))
    es_primo(numero)
