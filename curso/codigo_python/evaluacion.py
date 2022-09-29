


def run():
    # num_1 = int(input("Escoje un entero: "))
    # num_2 = int(input("Escoje un entero: "))
    # if num_1 > num_2:
    #     print("El primer numero es mayor que el segundo")
    # elif num_1 < num_2:
    #     print( "El segundo numero es el mayor que el primero")
    # else:
    #     print("Los dos numeros son iguales")
    nombre_1 = input("Cual es el nombre del primer chico: ")
    nombre_2 = input("Cual es el nombre del segundo chico: ")
    edad_1 = int(input("Cual es la edad del primer chico: "))
    edad_2 = int(input("Cual es la edad de segundo chico: "))
    if edad_1 > edad_2:
        print(nombre_1 + " Es Mayor que " + nombre_2)
    elif edad_1 < edad_2:
        print(input( nombre_2 + " Es mayor que " + nombre_1 ))
    else:
        print(nombre_1 + " y " + nombre_2 + " Tienen la misma edad" )




if __name__ == "__main__":
    run()