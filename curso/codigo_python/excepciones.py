def divide_elementos_de_lista(Lista, divisor):
    try:
        return [i / divisor for i in Lista]
    except ZeroDivisionError as e:
        print(e)
        return Lista


Lista = list (range(10))
divisor = 0


print(divide_elementos_de_lista(Lista, divisor))