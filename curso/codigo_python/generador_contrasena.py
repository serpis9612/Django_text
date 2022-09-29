def run():
    import random

    def generar_password():
        capital_letters = ["A", "B", "C", "D", "E", "F", "G"]
        lowercase_letters = ["a", "b", "c", "d", "e", "f", "g"]
        simbolos = ["!", "#", "$", "&", "/", "(", ")"]
        numeros =["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        caracteres = capital_letters + lowercase_letters + simbolos + numeros

        contrasena = []

        for i in range(15):
            caracter_random = random.choice(caracteres)
            contrasena.append(caracter_random)

        contrasena = "".join(contrasena)
        return contrasena



    contrasena = generar_password()
    print("Tu nueva contrasena es: " + contrasena)


if __name__ == "__main__":
    run()