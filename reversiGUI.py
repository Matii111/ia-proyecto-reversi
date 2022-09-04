import functions
import os
def reversi(opcion):	
	print("╔═══════════════════════════════════════╗")
	print("║                                    _  ║\
		 \n║                                   (_) ║\
		 \n║  _ __  ___ __   __ ___  _ __  ___  _  ║\
		 \n║ | '__|/ _ \\\ \ / // _ \| '__|/ __|| | ║\
		 \n║ | |  |  __/ \ V /|  __/| |   \__ \| | ║\
		 \n║ |_|   \___|  \_/  \___||_|   |___/|_| ║")
	print("║                                       ║")
	print("║                                       ║")
	print("╚═══════════════════════════════════════╝")			
	print("╔",end="══════════════╦═════════════╦══════════╗\n")
	print("║Fichas blancas║Fichas negras║Dificultad║")		
	print("╠",end="══════════════╬═════════════╬══════════╣\n")
	print("  0              0                -   ")		
	print("╚",end="══════════════╩═════════════╩══════════╝\n")
	print("╔═══════════════════════════════════════╗")			
	for i in range(2):
		
		if(i ==1):
			print("║Ingrese la dificultad del juego:       ║\n",end="")
			print("║FACIL    ",end="                              ║\n")
			print("║MEDIO    ",end="                              ║\n")
			print("║DIFICIL    ",end="                            ║\n")
			print("║Ingrese el tamano del tablero  :       ║\n",end="")
			print("║8x8    ",end="                                ║\n")
			print("║6x6    ",end="                                ║\n")
	print("╚═══════════════════════════════════════╝")			

def prinTab(tablero, turno, dificultad):

	fichas_blancas = contadorFichas(tablero,1)
	fichas_negras = contadorFichas(tablero,2)	
	print(tablero)
	print("╔═══════════════════════════════════════╗")
	print("║                                    _  ║\
		 \n║                                   (_) ║\
		 \n║  _ __  ___ __   __ ___  _ __  ___  _  ║\
		 \n║ | '__|/ _ \\\ \ / // _ \| '__|/ __|| | ║\
		 \n║ | |  |  __/ \ V /|  __/| |   \__ \| | ║\
		 \n║ |_|   \___|  \_/  \___||_|   |___/|_| ║")
	print("║                                       ║")
	print("║                                       ║")
	print("╚═══════════════════════════════════════╝")	
	print("╔",end="══════════════╦═════════════╦══════════╗\n")
	print("║Fichas blancas║Fichas negras║Dificultad║")		
	print("╠",end="══════════════╬═════════════╬══════════╣\n")
	print(" ",fichas_blancas,"            ",fichas_negras,"           ",dificultad,"   ")		
	print("╚",end="══════════════╩═════════════╩══════════╝\n")
	print("╔═══════════════════════════════════════╗")		
	creaTabLetras(tablero)			    
	numTablero = 1						
	contadorEnI = 0						
	for i in tablero:					
		if(len(tablero)==8):			
			print("║    ",numTablero,end="  ")	    
		else:
			print("║       ",numTablero,end="  ")	    
		for j in i:			
			if(j==1):		
				print("▀",end="  ")
			elif(j==2):
				print("♦",end="  ")		
			elif(j==3 and turno == 1):	
				print("X",end="  ")
			elif(j==4 and turno == 2):	
				print("X",end="  ")
			elif(j==9):	
				print(9,end="  ")
			else:
				print("○",end="  ")
		if(len(tablero)==8):
			print(numTablero,"     ║",end=" ")
		else: 
			print(numTablero,"        ║",end=" ")
		print("\n")
		contadorEnI+=1
		numTablero+=1		
	letras = 65
	
	for i in range(len(tablero)):	
		if(i == 0 and len(tablero)==8):
			print("║        ",end="")
		if(i == 0 and len(tablero)==6):
			print("║           ",end="")
		print(chr(letras),end="  ")	
		
		letras+=1
	if(len(tablero)==8):
		print("       ║")		
	else:
		print("          ║")		
	print("╚═══════════════════════════════════════╝")
	print("\n")


def creaTabLetras(tablero):     	    #Esta funcion crea una linea de letras similiar a
	letras = 65							#la del ajedrez, como se menciona anteriormente
	if(len(tablero)==8):
		print("║       ",end=" ")					#la funcion 'prinTab' y esta solo cumplen el objetivo
	else:
		print("║          ",end=" ")
	for i in range(len(tablero)):		#de hacer mas intuitivo el juego
		print(chr(letras),end="  ")			
		letras+=1
	if(len(tablero)==8):
		print("       ║\n")
	else:
		print("          ║\n")
	

def mostrarMovDisponibles(tablero,movDisponibles,color,sentido): #Funcion que muestra en pantalla los movimientos
	if(color == 1):	   	  								         #disponibles y/o validos
		movDisp = 3
	else:
		movDisp = 4
	for i in movDisponibles:
		posInicio = i[0]
		posTermino= i[1]
		posColumna= i[2]
		if(sentido==1):
			tablero[posColumna][posInicio] = movDisp	
		elif(sentido==-1):
			tablero[posColumna][posTermino] = movDisp
		
def contadorFichas(tablero,color):
	cont = 0
	for i in tablero:
		for j in i:
			if (j == color):
				cont +=1
	return cont





	#Movimientos iniciales posibles

"""
	tablero[2][3] = 4	#Blancas
	tablero[3][2] = 4
	tablero[5][4] = 4
	tablero[4][5] = 4

	tablero[4][2] = 3   #Negras
	tablero[2][4] = 3
	tablero[5][3] = 3
	tablero[3][5] = 3
	tablero[3][5] = 3
"""

	
"""	Falta aniadir:
	1.- Menu de inicio : 
		~	Que tenga la dificultad	
		~	Tablero de 6x6 u 8x8
		~	Comando para entrar y salir

	2.- Movimientos de las piezas:

		~ 	Funcion de reemplazar piezas

		~	Funcion que recorra horizontal, vertical y diagonalmente si es que hay algun 
			movimiento posible
		
		~	Funcion de contador de piezas, se parte con dos piezas cada uno y se debe 
			mostrar el conteo de las piezas de cada color
		
		~   Funcion que muestre en pantalla todos los movimientos posibles	 	

	Simbologia:

		~ ■ -> Blancas
		~ • -> Espacios vacios
		~ X -> Movimientos disponibles
		~ ♦ -> Negras
		
		~ 1 -> Blancas
		~ 0 -> Espacios vacios
		~ 3 -> Movimientos disponibles blancas
		~ 4 -> Movimientos disponibles negras
		~ 2 -> Negras
"""		

