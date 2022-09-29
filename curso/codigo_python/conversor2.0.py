def conversor(tipo_pesos, valor_dolar):
    pesos = input("Cuantos pesos" +tipo_pesos+ "tienes?: ")
    #Le damos un tipo de dato a la variable pesos"""
    pesos =  float(pesos)
    #Aplicamos la operacion logica al codigo"""
    dolares = pesos / valor_dolar
    #Instanciamos la cantidad de decimales que deseamos en el resultado"""
    dolares = round (dolares,2)
    #convertimos la variable a un tipo de dato String"""
    dolares = str (dolares)
    #Imprimimos dos strings y en el centro la variable dolares con el resultado
    # la cantidad de doloares """
    print("Tienes $" + dolares + " dolares")

menu =   """
Bienvenido al conversor de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
Elige una opcion
""" 

opcion = int(input (menu))

if opcion == 1:
    conversor("Colombianos", 4400)
elif opcion == 2:
    conversor("Argentinos", 140.45)
elif opcion == 3:
    conversor("Mexicanos", 20.00)
else:
    print("Ingresa una opcion correcta por favor")


#En esta linea declaramos la variable pesos para pedirle al usuario
#que inserte la cantidad de pesos que decea convertir 
