#  
"""En esta linea declaramos la variable pesos para pedirle al usuario
que inserte la cantidad de pesos que decea convertir """
dolares = input("Cuantos pesos Dolares tienes?: ")
"""Le damos un tipo de dato a la variable pesos"""
dolares =  float(dolares)
"""Instanciamos el valor de dolar en comparacion al peso"""
valor_peso = 0.00022
"""Aplicamos la operacion logica al codigo"""
pesos = dolares / valor_peso
"""Instanciamos la cantidad de decimales que deseamos en el resultado"""
pesos = round (pesos,2)
"""convertimos la variable a un tipo de dato String"""
pesos = str (pesos)
"""Imprimimos dos strings y en el centro la variable dolares con el resultado
, la cantidad de doloares """
print("Tienes $" + pesos + " Pesos colombianos")
