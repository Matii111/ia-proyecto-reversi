def prinTab(tablero):					#La funcion 'prinTab' es para imprimir el tablero 
	creaTabLetras(tablero)			    #en un formato comprensible para el usuario,
	numTablero = 1						#dentro se llama a la funcion 'creaTabLetras'
	contadorEnI = 0						#con para crear la primera linea de letras
	for i in tablero:	
		print(numTablero,end="  ")				
		for j in i:			
			if(j==1):		
				print("▀",end="  ")
			elif(j==2):
				print("•",end="  ")
			else:
				print("X",end="  ")
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

def creaTab(tablero,dimension):    	 	#Crea una lista de listas que funcionara como mapa
	for i in range(dimension):			#de coordenadas, tanto para el tablero como para cada
		tablero.append([])				#color
		for j in range(dimension):		
			tablero[i].append(0)


def insertar(tablero,color,posicion_x,posicion_y): #Pide los valores del tablero, el color 
												   #y la posicion de la pieza insertar
	x=0
	y=0
	for i in tablero:				
		for j in i:			
			if((posicion_x-1)==y ):
				if(color == 0):
					i[(posicion_y-1)]=1		
				else:
					i[(posicion_y-1)]=2		
		x+=1		
		y+=1
	return tablero


	
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
		~ • -> Negras
		~ X -> Movimientos disponibles

"""		

