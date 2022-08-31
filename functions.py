import reversiGUI
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
def comprobarMov(tablero,color):
	h=0
	v=0
	movDisponibles =  []
	posInicio  = 0
	posTermino = 0
	posColumna = 0
	if(color == 1):
		piezaContraria=2
		posOcupada    =3
	else: 
		piezaContraria=1
		posOcupada    =4
	for i in tablero:		
		for j in i:				
			if(j == piezaContraria       and    				  #comprueba si la posicion actual es una pieza contraria
			   tablero[h][v-1]     ==      0   				      #comprueba si la posicion anterior esta vacia						  
				):												  		
				if(comprobarFinal(i,color,v+2) != False):		  
					posInicio 	  = v-1
					posTermino = comprobarFinal(i,color,v+2)	 														
					posColumna 	    = h
					movDisponibles.append([posInicio,(posTermino*-1),posColumna])
					comprobarLinea(movDisponibles,tablero,color)
					reversiGUI.mostrarMovDisponibles(tablero,movDisponibles,color)

			v+=1
				
		v=0
		h+=1	
	

	return movDisponibles


def comprobarFinal(lista,color,coorY):		#recorre inversamente la lista hasta encontrar una 
	if( color == 1 ):						#pieza del color contrario y retorna su posicion o
		c = 2 								#un 'false' si no la hay
	else:
		c= 1
	cont= -1
	for i in lista:				
		if(lista[cont] == color ):
			return cont
		elif(lista[cont] == c):
			return False
		cont-=1

def comprobarLinea(movDisponibles,tablero,color):	   # determina si una linea es apta para ser llenada
	for i in movDisponibles:
		if(color ==1):
			c=2
		else:
			c=1
		posInicio = i[0]
		posTermino= i[1]
		posColumna= i[2]
		contPosicion = posInicio+2
		contMovDispo =0 
		while(contPosicion<(posTermino)):               #comprueba si se llego desde la pos  inicial a final
			if(tablero[posColumna][contPosicion] == c):				
				contPosicion +=1
				continue
			else:
				break
		if(contPosicion != posTermino):
			movDisponibles.pop(contMovDispo)		     #si se llega a la pos final y existe aglo que no corresponde
		contMovDispo+=1									 #entre esos dos puntos, se elimina de la lista de movDisponibles
	return movDisponibles
			

	




