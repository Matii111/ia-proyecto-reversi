
def prinTab(tablero):					#La funcion 'prinTab' es para imprimir el tablero 
	creaTabLetras(tablero)			    #en un formato comprensible para el usuario,
	numTablero = 1						#dentro se llama a la funcion 'creaTabLetras'
	contadorEnI = 0						#con para crear la primera linea de letras
	for i in tablero:	
		print(numTablero,end="  ")				
		for j in i:					
			print("0",end="  ")
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

def creaTab(tablero,dimension):
	for i in range(dimension):	
		tablero.append([])
		for j in range(dimension):		
			tablero[i].append(j)

	
tablero = []
creaTab(tablero,8)
prinTab(tablero)
#print(tablero).

