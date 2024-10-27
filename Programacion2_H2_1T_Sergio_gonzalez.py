'''
CUESTIÓN 2: Juego de piedra papel o tijera (2,5 puntos). El usuario introduce un valor (1-
Piedra|2- Papel|3-Tijera), si no es correcto se volver a pedir de nuevo hasta que se correcta.
La “maquina” generará un valor aleatorio (de 1 a 3) para elegir piedra, papel o tijera. Al
finalizar, mostrará la opción del usuario y de la máquina e indicará si hemos ganado, perdido o
empatado.
'''

valor_usua = ""
valor_maquina = ""
contador_maquina=0
contador_usua=0
resultado_juego = ""
opciones= ["Piedra", "Papel", "Tijeras"]
#Nos genera un numero random
import random
#Utilizmos un bucle while para saber los diferentes tipo de opciones que tenemos en la lista
while contador_usua != 3 and contador_maquina !=3:
    valor_usua=int(input("Introduce un numero para estos valores 1-Piedra , 2-Papel ,3-tijera: "))
    valor_maquina=random.randint(1,3)
#Utilizamos una serie de condicones para saber las opciones qeu tiene el usuario.
    if valor_usua in (1,2,3):
        print(f"Esta es tu opcion: {opciones [valor_usua - 1]}")
        print(f"Esta es la opcion de la maquina: {opciones [valor_maquina - 1]}")
#Dentro de la condicion que hemos creado utilzmos dentro de ella para saber los diferenetes tipos de reusltados que tiene el usuario respecto de la maquina
#Agregamos contadores para saber cuantas vesces has ganado, empatado o perdido el usuario
        if (valor_usua == valor_maquina):
            resultado_juego = "Has empatado"
        elif (valor_usua == 1 and valor_maquina == 3):
            resultado_juego = "Has ganado"
            contador_usua = contador_usua + 1
        elif (valor_usua == 2 and valor_maquina == 1):
            resultado_juego = "Has ganado"
            contador_usua = contador_usua + 1
        elif (valor_usua == 3 and valor_maquina == 2):
            resultado_juego = "Has ganado"
            contador_usua = contador_usua + 1
        else:
            resultado_juego = "Has perdido"
            contador_maquina= contador_maquina + 1
#Imprimimos el reultado_juego para que nos aparezca en pantalla
        print(f"El resultado es: {resultado_juego}")
    else:
#Si el numero que ingresa no coincide con las opciones le saltara un aviso de error
        print(f"Error,vuelve a introducir un numero que este entre el 1,2 o 3")