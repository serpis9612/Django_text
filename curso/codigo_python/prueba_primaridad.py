# def es_primo(numero):
#     contador = 0 

#     for i in range(1, numero + 1):
#         if i == 1 or i == numero:
#             continue
#         if numero % i == 0:
#             contador += 1
#     if contador == 0:
#         return True
#     else: 
#         return False

# def run():
#     numero = int(input("Escribe un numero: "))
#     if es_primo(numero):
#         print("Es primo")
#     else:
#         print("No es primo")

# if __name__ == "__main__":
#     run()
def run():

    numero = int(input("Digite un numero: "))
    numero2= numero - 1
    factorial = 1
    if numero2 != 0:
        for i in range(1,numero2+1):
            factorial=factorial*i    
    teoremadewilson = factorial+1
    teoremadewilson= teoremadewilson % numero    
    if teoremadewilson == 0:
        print("Es primo ")
    else:
        print("No es Primo ")

if __name__=="__main__":
    run()

