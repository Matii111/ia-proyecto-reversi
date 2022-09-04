import reversiGUI	
import functions
import os

tablero = []
fichasNegras = []
fichasBlancas= []
dificultades = ["FACIL","MEDIO","DIFICIL"]
tamanios = ["6x6","8x8"]
comenzar = "comenzar"
mov = ""
reversiGUI.reversi(0)

dificultad = input("Dificultad: ")
dificultad = dificultad.upper()
while(dificultad not in dificultades):
	dificultad = input("Dificultad: ")

tamanio = input("Tamano: ")
tamanio = tamanio.lower()
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
	##################################
if(tamanio == "6x6"):
	tamanio = 6
	#posiciones iniciales tablero 6x6 
	functions.creaTab(tablero,tamanio)
	functions.insertar(tablero,2,4,4) 
	functions.insertar(tablero,1,4,3)
	functions.insertar(tablero,2,3,3)
	functions.insertar(tablero,1,3,4)
	##################################

reversiGUI.reversi(1)
os.system ("clear")
reversiGUI.prinTab(tablero,2,dificultad)

comenzar = input("Escriba comenzar para mostar posiciones iniciales: \n")
comenzar = comenzar.lower()
while (comenzar != "comenzar"):
	os.system ("clear")
	reversiGUI.prinTab(tablero,2,dificultad)
	comenzar = input("Escribar comenzar para mostar posiciones iniciales: \n")
	comenzar = comenzar.lower()
a = functions.comprobarMov(tablero,2)
while(mov != "0"):
	os.system ("clear")
	reversiGUI.prinTab(tablero,2,dificultad)
	reversiGUI.mostrarMovDisponibles(tablero,a,2,0)
	print(a)
	mov = input("Ingrese un movimiento: \n")


