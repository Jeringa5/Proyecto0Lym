robot={"posicion_x":1, "posicion_y":1, "orientacion":0}
# Orientacion -> 0=arriba(norte), 90=derecha(este), 180=abajo(sur), 270=izquierda(oeste)

def crear_matriz(x:int):
    matriz=[]
    for i in range(x):
        fila = []  # Fila vacía
        for j in range(x):
            fila.append(0)  # Agregar un 0 a la fila
        matriz.append(fila)
    return matriz

def asignar_variable(variable):
    
    return variable

def goto(robot, matriz, eje_x:int, eje_y:int):
    
    return robot, matriz

def mover(robot, matriz, pasos:int):
    
    return robot, matriz

def girar(robot, matriz, grados:int):
    
    return robot, matriz

def orientar(robot, matriz, orientacion:int):
    
    return robot, matriz

def colocar(robot, matriz, cantidad:int, tipo:str):
    
    return robot, matriz

def recoger(robot, matriz, cantidad:int, tipo:str):
    
    return robot, matriz

def mover_hacia(robot, matriz, casillas, direccion):

    return robot, matriz

def mover_en(robot, matriz, casillas, orientacion):

    return robot, matriz

def saltar_hacia(robot, matriz, casillas, direccion):

    return robot, matriz

def saltar_en(robot, matriz, casillas, orientacion):

    return robot, matriz