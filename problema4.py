import os

def ejemplo4():
    class Cuenta:
        def __init__(self):
            self.titular="edsel"
            self.cantidad= 20000000

        def imprimir(self):
            print(f"Nombre del Titular : {self.titular}")
            print(f"Cantidad : {self.cantidad}\n")

    class CajaAhorro(Cuenta):
        def __init__(self):
            super().__init__()
            
        def mostrarCajaAhorro(self):
            super().imprimir()

    class PlazoFijo(Cuenta):
        def __init__(self):
            super().__init__()
            self.plazo ="cinco meses"
            self.interes = 1.2
        
        def importeInteres(self):
            self.importe = (self.cantidad*self.interes)/100
            return self.importe

        def mostrarDatos(self):
            self.intereses = self.importeInteres()
            print("\n**** Datos del titular**** \n")
            super().imprimir()
            print(f"EL plazo de pago es de {self.plazo}")
            print(f"La cuota de Interes es del {self.interes}")
            print(f"El total de intereses es de: {self.intereses}\n")


    def mostrarDatosFinales():
        inter =PlazoFijo()
        inter.mostrarDatos()

    def mostrarCaja():
        caja =CajaAhorro()
        caja.mostrarCajaAhorro()

    def imprimirCuenta():
        cuenta1 = Cuenta()
        cuenta1.imprimir()

    print("")

    def opciones():
        os.system("pause")
        os.system("cls")

        while(True):
          
            print("Servicio de  Estado de Cuenta")
            print("¿Que deseas hacer?")
            print("1. Imprimir datos cuenta Inicial")
            print("2. Mostrar Caja de Ahorro")
            print("3. Mostrar Estado de cuenta final")
            print("4. salir")
            print("por favor elige una opción")
            

            opc = int(input("ingresa una opcion? => "))
            if opc==1:
                imprimirCuenta()
            elif opc==2:
                mostrarCaja()
            elif opc==3:
                mostrarDatosFinales()
            elif opc==4:
                print("Bendiciones")
                break
            else:
                print("Opción incorrecta, Regresando al Menu principal.... \n")
                break
            os.system("pause")
            os.system("cls")
    opciones()