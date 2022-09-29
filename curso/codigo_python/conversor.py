menu =   """
Bienvenido al conversor de monedas
1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos
Elige una opcion
""" 
opcion = input (menu)

if opcion == "1":
    pesos = input("Cuantos pesos colombianos tienes?: ")
    #Le damos un tipo de dato a la variable pesos"""
    pesos =  float(pesos)
    #Instanciamos el valor de dolar en comparacion al peso"""
    valor_dolar = 4871
    #Aplicamos la operacion logica al codigo"""
    dolares = pesos / valor_dolar
    #Instanciamos la cantidad de decimales que deseamos en el resultado"""
    dolares = round (dolares,2)
    #convertimos la variable a un tipo de dato String"""
    dolares = str (dolares)
    #Imprimimos dos strings y en el centro la variable dolares con el resultado
    # la cantidad de doloares """
    print("Tienes $" + dolares + " dolares")
elif opcion == "2":
    pesos = input("Cuantos pesos Argentinos tienes?: ")
    #Le damos un tipo de dato a la variable pesos"""
    pesos =  float(pesos)
    #Instanciamos el valor de dolar en comparacion al peso"""
    valor_dolar = 140.45
    #Aplicamos la operacion logica al codigo"""
    dolares = pesos / valor_dolar
    #Instanciamos la cantidad de decimales que deseamos en el resultado"""
    dolares = round (dolares,2)
    #convertimos la variable a un tipo de dato String"""
    dolares = str (dolares)
    #Imprimimos dos strings y en el centro la variable dolares con el resultado
    # la cantidad de doloares """
    print("Tienes $" + dolares + " dolares")
elif opcion == "3":
    pesos = input("Cuantos pesos Mexicanos tienes?: ")
    #Le damos un tipo de dato a la variable pesos"""
    pesos =  float(pesos)
    #Instanciamos el valor de dolar en comparacion al peso"""
    valor_dolar = 20.00
    #Aplicamos la operacion logica al codigo"""
    dolares = pesos / valor_dolar
    #Instanciamos la cantidad de decimales que deseamos en el resultado"""
    dolares = round (dolares,2)
    #convertimos la variable a un tipo de dato String"""
    dolares = str (dolares)
    #Imprimimos dos strings y en el centro la variable dolares con el resultado
    # la cantidad de doloares """
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingresa una opcion correcta por favor")


#En esta linea declaramos la variable pesos para pedirle al usuario
#que inserte la cantidad de pesos que decea convertir 

