import reversiGUI	
import functions

tablero = []
fichasNegras = []
fichasBlancas= []



functions.creaTab(tablero,8)

#posiciones iniciales
functions.insertar(tablero,1,4,5)
functions.insertar(tablero,2,4,4)
functions.insertar(tablero,1,5,4)
functions.insertar(tablero,2,5,5)

#primera jugada negras
functions.insertar(tablero,2,1,2)
functions.insertar(tablero,2,2,3)
functions.insertar(tablero,2,3,4)


#primera jugada blancas
functions.insertar(tablero,1,1,5)
functions.insertar(tablero,1,2,5)
functions.insertar(tablero,1,3,5)

#functions.insertar(tablero,1,4,3)

a = functions.comprobarMov(tablero,1)
reversiGUI.prinTab(tablero,1)
print(functions.comprobarLinea(a,tablero,1))


print(tablero)
