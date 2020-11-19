#  Este programa verifica si una palabra u oracion en un palindromo

def run():
    word = input("Ingresa una palabra: ")
    word = word.replace(" ","")
    word = word.lower()

    inv_word = word[::-1]

    if word == inv_word:
        print("Es palindromo.")
    else:
        print("No es palindromo.")


if __name__ == '__main__':
    run()







