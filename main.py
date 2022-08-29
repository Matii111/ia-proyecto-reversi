import reversiGUI	

tablero = []
fichasNegras = []
fichasBlancas= []
reversiGUI.creaTab(tablero,8)
reversiGUI.creaTab(fichasBlancas,8)
reversiGUI.creaTab(fichasNegras,8)


reversiGUI.insertar(tablero,0,4,5)
reversiGUI.insertar(tablero,1,4,4)

reversiGUI.insertar(tablero,0,5,4)
reversiGUI.insertar(tablero,1,5,5)

reversiGUI.prinTab(tablero)
#print(tablero)

