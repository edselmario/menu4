import os
from problema1 import ejemplo1 
from problema2 import ejemplo2 
from problema3 import ejemplo3
from problema4 import ejemplo4



def menu():

    os.system("pause")
    os.system("cls")

    while(True):
        print(" ________________________________")
        print("|           Bienvenido           |")
        print("|                                |")
        print("|  1. ejercicio 1                |")
        print("|  2. ejercicio 2                |")
        print("|  3. ejercicio 3                |")
        print("|  4. ejercicio 4                |")
        print("|  5. salir                      |")
        print("|                                |")
        print("|   por favor elige una opción   |")
        print("|                                |")
        print("|________________________________|")
        print("")

        item = int(input("indicanos que deseas revisar? => "))
        print("")
        if item == 1:
            print("Has seleccionado el problema 1, estas atento? \n")
            ejemplo1()
        elif item == 2:
            print("Has seleccionado el problema 2, estas atento? \n")
            ejemplo2()
        elif item == 3:
            print("Has seleccionado el problema 3, estas atento? \n")
            ejemplo3()
        elif item == 4:
            print("Has seleccionado el problema 4, estas atento? \n")
            os.system("pause")
            os.system("cls")
            ejemplo4()
        elif item ==5:
            print("Hasta luego \n")
            break
        else:
            print("ups!... Opción incorrecta, Hasta luego \n")
            break
        os.system("pause")
        os.system("cls")


def main():
    menu()

if __name__ == "__main__":
    main()