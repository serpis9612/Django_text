#def run():
#    pass

#num = 2
#i = 0
#while i <= 19:
#    i += 1
#    print(num ** i) 
#print ("Programa Terminado")

#if __name__ == "__main__":
#    run()

def run():
    LIMITE = 1000000
    contador = 0 
    potencia_2 = 2**contador
    while potencia_2 < LIMITE:
        print("2 elevado a " + str (contador)+" es igual a: "+ str( potencia_2))
        contador = contador + 1
        potencia_2 = 2 ** contador 

if __name__ == "__main__":
    run()


    


