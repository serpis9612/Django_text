objetivo = int(input("Escoje un entero: "))
respuesta = 0 

while respuesta ** 2 < objetivo:
    
    respuesta += 1
    
if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} notiene una raiz cuadrada exacta')