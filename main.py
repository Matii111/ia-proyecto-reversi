import reversiGUI	
import functions
import os

tablero      = []
fichasNegras = []
fichasBlancas= []
dificultades = ["FACIL","MEDIO","DIFICIL"]
tamanios     = ["6x6","8x8"]
comenzar     = "comenzar"
mov          = ""
comprobadorMov = 0

#ejecucion de tablero inicial
reversiGUI.reversi(0)

dificultad = input("Dificultad: ")
dificultad = dificultad.upper()
#dificultad = "FACIL"

#comprueba que se ingrese una dificultad disponible

while(dificultad not in dificultades):
	dificultad = input("Dificultad: ")

tamanio = input("Tamano: ")
tamanio = tamanio.lower()
#tamanio = "8x8"

#comprueba que se ingrese un tamanio disponible

while(tamanio not in tamanios):
	tamanio = input("Tamano: ")

if(tamanio == "8x8"):
	tamanio = 8
	#posiciones iniciales tablero 8x8 
	functions.creaTab(tablero,tamanio)
	functions.insertar(tablero,1,4,5) 
	functions.insertar(tablero,2,4,4)
	functions.insertar(tablero,1,5,4)
	functions.insertar(tablero,2,5,5)

if(tamanio == "6x6"):
	tamanio = 6
	#posiciones iniciales tablero 6x6 
	functions.creaTab(tablero,tamanio)
	functions.insertar(tablero,2,4,4) 
	functions.insertar(tablero,1,4,3)
	functions.insertar(tablero,2,3,3)
	functions.insertar(tablero,1,3,4)

reversiGUI.reversi(1)
os.system ("clear")

#se printea el primer tablero al jugador
reversiGUI.prinTab(tablero,2,dificultad)

comenzar = input("Escriba comenzar para mostar posiciones iniciales: \n")
comenzar = comenzar.lower()
#comenzar = "comenzar"

#al ingresar comenzar , comienza el juego y el primer movimiento lo tienen las negras, 
#mostrando sus posibles movimientos tanto en pantalla como en una lista de coordenadas

while (comenzar != "comenzar"):
	os.system ("clear")
	reversiGUI.prinTab(tablero,2,dificultad)
	comenzar = input("Escribar comenzar para mostar posiciones iniciales: \n")
	comenzar = comenzar.lower()

while(mov != "0"):
	os.system ("clear")
	if(comprobadorMov == 0):
		turno = 2
		comprobadorMov +=1
	else:
		comprobadorMov -=1
		turno = 1

	a = functions.comprobarMov(tablero,turno)
	reversiGUI.mostrarMovDisponibles(tablero,a,turno,0)	
	reversiGUI.prinTab(tablero,turno,dificultad)
	reversiGUI.movTabla(tablero,turno)

#comprobador de movimientos, tras cada movimiento ingresado se comprueba si es valido
#y en tal caso se pasa el turno al otro jugador

	mov = input("Ingrese un movimiento: \n")
	verificar = functions.verificarMov(mov,tamanio,a)
	while(verificar != True):
		os.system ("clear")			
		reversiGUI.prinTab(tablero,turno,dificultad)
		reversiGUI.movTabla(tablero,turno)
		mov = input("Movimiento no valido, ingrese uno correcto: \n")
		verificar = functions.verificarMov(mov,tamanio,a)

	posicion_x = ord(mov[0].upper())-64
	posicion_y = int(mov[1])

	functions.insertar(tablero,turno,posicion_x,posicion_y)