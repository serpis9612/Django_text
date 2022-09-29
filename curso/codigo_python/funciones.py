#def imprimir_mensaje():
#    print ("Mensaje especial")
#    print ("Estoy aprendiento ha usar funciones")


#invocar una funcion
#imprimir_mensaje()
#imprimir_mensaje()
#imprimir_mensaje()

#def  conversacion(mensaje):
#   print("Hola")
#    print("Como estas")
#   print(mensaje)
#    print("Adios")


#opcion = input("Elige una opcion(1,2,3): ")
#if opcion == "1":
#        conversacion("Elejiste la Opcion 1")
#elif opcion == "2":
#        conversacion("Elejiste la Opcion 2")
#elif opcion == "3":
#        conversacion("Elejiste la Opcion 3")
#else:
#    print("Digite una opcion valida ")


# def suma (a,b):
#     print("Se suman 2 Numeros")
#     resultado = a + b
#     return resultado
# sumatoria = suma(2 , 4)
# print(sumatoria)

def suma (a , b):
    total = a + b
    print(f'Resultado: {total}')
    return total
        
suma(2,3)