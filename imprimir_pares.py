def imprimir_pares(numero):
    for i in range(1, numero+2):
        if (i) % 2 == 0:
            print(i, end=" ")
            
if __name__ == "__main__":
    numero = int(input("Digite el número: "))
    imprimir_pares(numero)
