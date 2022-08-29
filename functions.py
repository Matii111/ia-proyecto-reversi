def insertar(tablero,color,posicion_x,posicion_y): #Pide los valores del tablero, el color 												   
	x=0											   #y la posicion de la pieza insertar,
	y=0											   #para las blancas color = 1 para las 
	for i in tablero:							   #negras cualquier otro 						
		for j in i:			
			if((posicion_x-1)==y ):
				if(color == 1):
					i[(posicion_y-1)]=1							
				else:
					i[(posicion_y-1)]=2		
		x+=1		
		y+=1
	

def creaTab(tablero,dimension):    	 	#Crea una lista de listas que funcionara como mapa
	for i in range(dimension):			#de coordenadas, tanto para el tablero como para cada
		tablero.append([])				#color
		for j in range(dimension):		
			tablero[i].append(0)			
	
	#Movimientos iniciales posibles

	tablero[2][3] = 4	#Negras
	tablero[3][2] = 4
	tablero[5][4] = 4
	tablero[4][5] = 4

	tablero[4][2] = 3   #Blancas
	tablero[2][4] = 3
	tablero[5][3] = 3
	tablero[3][5] = 3
	tablero[3][5] = 3

def comprobarMov(tablero,color):
	h=0
	v=0
	if(color == 1):
		c=2
	else: 
		c=1

	for i in tablero:
		for j in i:
			#Comprueba si hay movimientos disponibles a la derecha
			if(j==c and tablero[h][v] == 0 and tablero[h][v+2] == color):											
				tablero[h][v] = 9
				comprobarSiguiente(i,color,v+2)								
		v+=1
		h+=1

#Comprueba si los valores a la dereche de un numero son continuos

def comprobarSiguiente(lista,color,coorInicio):		
	cont = 0
	if( color == 0 ):
		c = 1
	else:
		c= 2

	for i in lista:				
		if(i == lista[coorInicio] and lista[-2] == c):		
			lista[coorInicio] = color
		cont+=1
		if(cont>coorInicio):
			coorInicio+=1	




