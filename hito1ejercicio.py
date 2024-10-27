'''A través de un menú solicitaremos alusuario que tipo de figura quiere mostrar (1-Cuadrado|2-Rectángulo), si la opción no escorrecta, se mostrará mensaje de error y se volverá a solicitar hasta que se correcta.  Si ha seleccionada un cuadrado, pediremos su lado y mostraremos la figura, su área yperímetroSi ha seleccionada un rectángulo, pediremos base y altura y mostraremos la figura, su área y perímetro'''


menu=""

#Utilizamos un bucle while para mostrar el menu

while True:
    menu = int(input("Mostrar menu : 1-Cuadrado y 2-Rectangulo: "))
#Utilizamos condiciones para saber lo que sucede en cada uno de los casos.
    if menu == 1:
        lado = int(input("Dime el lado del cuadrado: "))
        print(f"EL area del cuadrado es {lado * lado }")
        print(f"El perimetro es {(lado*4)}")
        for estrella in range (lado):
            print("*" * lado)
    elif menu == 2:
        base = int(input("Dime la base del rectagulo: "))
        altura = int(input("Dime la altura del rectangulo: "))
        print (f"El area del rectangulo es {base * altura}")
        print (f"El area del perimetro es {base*2 + altura*2}")
        for i in range (altura):
            print(f"*"*base)
#En la ultima condion añadimos al break al ingresar el numero tres que nos saca del bucle
    elif menu == 3:
        break
#Si el numero es distinto a todos los de las condiciones no indica que hay un error y que ingrese otro numero
    else :
        print ("Error introduce un numero valido: ")