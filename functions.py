import reversiGUI
def insertar(tablero,color,posicion_y,posicion_x): #Pide los valores del tablero, el color 												   
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
	
def comprobarMov(tablero,color):
	movVertical=0
	movHorizont=0
	movDisponibles =  []
	posInicio  = 0
	posTermino = 0
	posColumna = 0	
	if(color == 1):
		piezaContraria=2
		posOcupada    =3
	elif(color ==2): 
		piezaContraria=1
		posOcupada    =4
	for i in tablero:		
		for j in i:
			if(j == piezaContraria	): 			
				if(tablero[movVertical][movHorizont-1]==0  and 
					tablero[movVertical][movHorizont+1]== color  													
					):												  		
					if(comprobarFinal(i,color,1) != False):		  
						posInicio 	  = movHorizont-1
						posTermino = comprobarFinal(i,color,1)	 														
						posColumna 	    = movVertical
						movDisponibles.append([posInicio,(posTermino*-1),posColumna])							
						comprobarLinea(movDisponibles,tablero,color,1)
						reversiGUI.mostrarMovDisponibles(tablero,movDisponibles,color,1)
				"""
				elif(j == piezaContraria     and
					tablero[movVertical][movHorizont+1] == 0 	and			  #comprueba si la posicion siguiente esta vacia
					tablero[movVertical][movHorizont-1]== color
					):

					if(comprobarFinal(i,color,-1) != False):		
						posInicio = (comprobarFinal(i,color,-1)-1)
						posTermino = movHorizont+1
						posColumna = movVertical				
						movDisponibles.append([posInicio,(posTermino),posColumna])								
						comprobarLinea(movDisponibles,tablero,color,-1)				
						reversiGUI.mostrarMovDisponibles(tablero,movDisponibles,color,-1)	
				"""

			movHorizont+=1				
		movHorizont =0
		movVertical+=1
	return movDisponibles

def comprobarFinal(lista,color,sentido):		#recorre inversamente la lista hasta encontrar una 
	if(color == 1):						#pieza del color contrario y retorna su posicion o
		colorContrario = 2 								#un 'false' si no la hay
	else:
		colorContrario= 1
	if(sentido==-1):
		contador= 0		
	if(sentido==1):
		contador= -1		
	for i in lista:				
		if(lista[contador] == color ):		
			return contador
		if(lista[contador] == colorContrario):
			return False
		contador-=1 * sentido

def comprobarLinea(movDisponibles,tablero,color,sentido):	   # determina si una linea es apta para ser llenada	
	for i in movDisponibles:
		if(color ==1):
			c=2
		else:
			c=1
		posInicio = i[0]
		posTermino= i[1]
		posColumna= i[2]
		contPosicion = posInicio+2	
								
		while(contPosicion<(posTermino)):               #comprueba si se llego desde la pos  inicial a final
			if(tablero[posColumna][contPosicion] == c):								
				contPosicion +=1
				if(contPosicion != posTermino):
					movDisponibles.remove(i)		     					
			else:
				break		
			contPosicion +=1		
	return movDisponibles
			


	

