'''
CUESTION 3: Simular el funcionamiento de una cuenta bancaria (2.5 puntos): al iniciar el
programa, pediremos el saldo inicial de la cuenta (puede ser un número decimal), si el saldo es
menor que 0 se volverá a pedir hasta que sea correcto.
Posteriormente mostraremos un menú con las opciones, 1-ingresar dinero, 2-retirar dinero y
3- mostrar saldo y 4-salir, si la opción no es correcta se volver a pedir de nuevo hasta que sea
correcta. No se pueden ingresar cantidades negativas y no podemos retirar dinero si nos
quedamos en números rojos.
'''
saldo_inicial =-1
opciones_saldo = ""
contador_dinero = 0
contador_ingresardinero = 0
while saldo_inicial < 0:
    saldo_inicial = float(input("Introduce el saldo de tu cuenta:"))

while opciones_saldo !=5:
    opciones_saldo = int(input("Menu: 1-Ingresar dinero, 2-retirar dinero, 3-mostrar saldo, 4-estadistica, 5-salir:  "))
    if opciones_saldo in [1, 2, 3, 4, 5]:
        if opciones_saldo == 1:
            while True:
                ingresar_dinero = int(input("Cuanto dinero quieres ingresar:"))
                if ingresar_dinero > 0:
                    saldo_inicial = saldo_inicial + ingresar_dinero
                    contador_ingresardinero = contador_ingresardinero + 1
                    break
                else:
                    print("El numero no puede ser negativo")
        elif opciones_saldo == 2:
            while True:
                    retirar_dinero = int(input("Cuanto dinero quieres retirar:"))
                    if retirar_dinero > 0:
                        if retirar_dinero <= saldo_inicial:
                              saldo_inicial = saldo_inicial - retirar_dinero
                              contador_dinero = contador_dinero + 1
                              break           
                        else:
                            print("No puedes retirar dinero")
                    else:
                        print("El numero no puede ser negativo")
        elif opciones_saldo == 3:
            print(f"Mostrar:{saldo_inicial}")
        elif opciones_saldo == 4:
            print(f"{contador_dinero}")
            print(f"{contador_ingresardinero}")
        elif opciones_saldo == 5:
            print("Salir")

            


