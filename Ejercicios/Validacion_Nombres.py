"""
Este programa evalua si un nombre de usuario cumple con las siguientes condiciones:
1.- El nombre debe contener min 6 max 12 caracteres.
2.- Debe ser alfanumerico
3.- Si el nombre es menor que 6 caracteres, retorna  "El nombre de usuario debe contener al menos 6 
caracteres".
4.- Nombre de usuario con más de 12 caracteres, retorna el mensaje "El nombre de usuario no puede 
contener más de 12 caracteres".
5.- Nombre de usuario con caracteres distintos a los alfanuméricos, retorna el mensaje "El nombre 
de usuario puede contener solo letras y números".
6.- Nombre de usuario válido, retorna True.
"""
"""
def no_alfanumerico(name):

    invalid = ["."," ","|","°","!","#","´","$","%","&","/","(",")","=","?","'","¡","¿","]","}","{","[","-",",",":",";","_","*","@"]
    
    for letra in range(len(name)):
        if name[letra] in invalid:
            return True
    return False


def alfanumerico(name):
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    number_count = 0
    abc_count = 0
    
    for letra in range(len(name)):
        if name[letra] in numbers:
            number_count += 1
        elif name[letra] in abc:
            abc_count += 1
    
    if number_count > 0 and abc_count > 0:
        return True
    else:
        return False


def run():

    while True:

        name = input("Ingrese nombre de usuario: ").lower()
              

        if len(name) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres.")
        elif len(name) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres.")
        else:
            no_alfanumerico(name)
            alfanumerico(name)            

        if no_alfanumerico(name) == True:
            print("El nombre de usuario puede contener solo letras y números")        
        elif alfanumerico(name) == False:
            print("El nombre de usuario debe contener caracteres numericos y letras")
    
        if alfanumerico(name) == True and no_alfanumerico(name) == False:
            print("El usuario es valido!!!")      
"""
def run():

    while True:

        name = input("Ingrese nombre de usuario: ")
        
        if len(name) < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres.")
        elif len(name) > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres.")
        else:
            
            if name.isalnum():

                if name.isalpha() or name.isnumeric():
                    print("El nombre de usuario debe contener al menos una letra y almenos un numero!")
                else:
                    print("El usuario es valido!!!")

            else:
                print("El nombre de usuario puede contener solo letras y números")


if __name__ == '__main__':
    run()