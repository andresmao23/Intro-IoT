if __name__ == "__main__":
    def cambiar_valor(a, b):
        aux = a
        a = b
        b = aux
        return a, b
    
    a = int(input("Digite el valor de a: "))
    b = int(input("Digite el valor de b: "))
    print("a vale {} y b vale {}".format(a, b))
    a, b = cambiar_valor(a, b)
    print("Ahora a vale {} y b vale {}".format(a, b))
