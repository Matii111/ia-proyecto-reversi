import functions
def prinTab(tablero, turno):			#La funcion 'prinTab' es para imprimir el tablero 
	creaTabLetras(tablero)			    #en un formato comprensible para el usuario,
	numTablero = 1						#dentro se llama a la funcion 'creaTabLetras'
	contadorEnI = 0						#con para crear la primera linea de letras,
	for i in tablero:					#ademas separa los posibles movimientos dependiendo
		print(numTablero,end="  ")	    #del color 0 para blancas 1 para negras
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
		print("",numTablero,end=" ")
		print("\n")
		contadorEnI+=1
		numTablero+=1		
	letras = 65
	print("  ",end=" ")
	for i in range(len(tablero)):		
		print(chr(letras),end="  ")			
		letras+=1
	print("\n")


def creaTabLetras(tablero):     	    #Esta funcion crea una linea de letras similiar a
	letras = 65							#la del ajedrez, como se menciona anteriormente
	print("  ",end=" ")					#la funcion 'prinTab' y esta solo cumplen el objetivo
	for i in range(len(tablero)):		#de hacer mas intuitivo el juego
		print(chr(letras),end="  ")			
		letras+=1
	print("\n")

def mostrarMovDisponibles(tablero,movDisponibles,color): #Funcion que muestra en pantalla los movimientos
	if(color == 1):										 #disponibles y/o validos
		movDisp = 3
	else:
		movDisp = 4
	for i in movDisponibles:
		posInicio = i[0]
		posColumna= i[2]
		tablero[posColumna][posInicio] = movDisp

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

