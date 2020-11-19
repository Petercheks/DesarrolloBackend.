# Este programa evalua un numero que ingresa el usuario y determina si es primo o no
def primalidad(num):
    contador = 0
    for i in range(num):
        if num%(i+1) == 0:
            contador += 1   
    
    if contador <= 2:
        return True
    else:
        return False


def run():
    print("Este programa evalua si un numero es  primo o no")
    while True:
        num = int(input("Ingrese un numero a evaluar: "))   
        if num >= 1:
            if primalidad(num) == True:
                print(f"El numero {num} es primo")
            else:
                print(f"El numero {num} no es primo")
        else:
            print(f"El numero {num} no es primo") 

    

if __name__ == '__main__':
    run()
