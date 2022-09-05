import reversiGUI

#insertar rellena la posicion indicada con el color correspondiente, una posicion
#rellena con un 1 indica una ficha blanca, el 2 es para las fichas negras
def insertar(tablero,color,posicion_y,posicion_x): 											   
	x=0											   
	y=0											   
	for i in tablero:							   					
		for j in i:						
			if((posicion_x-1)==y ):
				if(color == 1):
					i[(posicion_y-1)]=1							
				else:
					i[(posicion_y-1)]=2		
		x+=1		
		y+=1
	
#creaTab es la lista de listas que dentro del codigo representa el tablero, los 
#espacios vacios son representados con un 0
def creaTab(tablero,dimension):    	 	
	for i in range(dimension):			
		tablero.append([])				
		for j in range(dimension):		
			tablero[i].append(0)			
	
#comprobarMov es un conjunto de acciones que recorren la lista desde el una ficha con
#el fin de comprobar todos los movimientos   posibles  retornando una lista de listas 
#de ellos, estas listas poseen 3 valores siendo el primero  y  el segundo la posicion
#de inicio y termino del movimiento, respectivamente y el tercer valor es la fila en 
#la que se realiza el movimiento
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

#comprobarFinal recorre inversamente una fila especifica de   la   lista,   ayuda   a         
#comprobarMov a cumplir con su tarea senialando el punto de termino de un  movimiento
def comprobarFinal(lista,color,sentido):		
	if(color == 1):						
		colorContrario = 2 				
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

#comprobarLinea determina si es que es valido  rellenar  un movimiento desde el punto
#de inicio hasta el punto final, tambien ayuda a comprobarMov a cumplir  su  objetivo
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
								
		while(contPosicion<(posTermino)):               
			if(tablero[posColumna][contPosicion] == c):								
				contPosicion +=1
				if(contPosicion != posTermino):
					movDisponibles.remove(i)		     					
			else:
				break		
			contPosicion +=1		
	return movDisponibles
			
#verificarMov es para comprobar el movimiento ingresado por un jugador retorna 'true'
#o 'false' dependiendo si el input aplica para ser un movimiento o no
def verificarMov(mov,tamanio,movDisponibles):
	listaPos = ["A","B","C","D","E","F","G","H"]
	contador =0	
	if(len(mov)==2):
		for i in mov:
			contador +=1		
			if(contador == 1):
				i = i.upper()			
				if(i in listaPos):
					posicion_x = ord(i)-65				
			if(contador == 2):			
				posicion_y = int(i)-1
		if(posicion_y>=0 and posicion_y<=tamanio):		
			for i in movDisponibles:			
				return posicion_x == i[0] and posicion_y ==i[2]
	else:
		return False





	


	

