def run():
    # numero = input("Escribre un numero: ") 
    # for i in range(1,11): 
    #     numero = int(numero)
    #     print (numero * i)
    LIMITE = 100 
    contador = 0 
    input("Bienvenido al programa de tablas de multiplicar")
    numero = input("Escribre el numero del que necesita la tabla: ")
    cantidaddeoperaciones = input("Escriba la cantidad de operaciones que desea realizar: ")    
    cantidaddeoperaciones = int(cantidaddeoperaciones)
    cantidaddeoperaciones = cantidaddeoperaciones + 1       
    while contador < LIMITE:        
        contador = contador + 1
        if contador < cantidaddeoperaciones:            
            numero = int(numero)     
            print (contador * numero)                   
            continue
                          
       

if __name__ == "__main__":
    run()