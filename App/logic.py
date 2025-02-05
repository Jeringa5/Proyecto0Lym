import random

robot={"posicion_x":1, "posicion_y":1, "orientacion":0}
# Orientacion -> 0=arriba(norte), 90=derecha(este), 180=abajo(sur), 270=izquierda(oeste)

def crear_matriz(x:int):
    """Genera una matriz de un tamaño dado por el usuario con una cierta cantidad de obstaculos puestos
    de manera aleatoria

    Args:
        x (int): Numero de casillas de la cual se desea crear la matriz cuadrada

    Returns:
        matriz (list): Matriz creada con la cantidad de obstaculos aleatorios
    """
    matriz=[]
    # 0 -> Libre
    # 1 -> Obstaculo
    for i in range(x):
        fila = []
        for j in range(x):
            valor = random.choices([0, 1], weights=[85, 15])[0] #85% un 0 y 15% un 1
            fila.append(valor)
        matriz.append(fila)
    return matriz

def asignar_variable(variable):
    
    return variable

def goto(robot, matriz, eje_x:int, eje_y:int):
    
    return robot, matriz

def move(robot, matriz, pasos:int):
    
    return robot, matriz

def turn(robot, matriz, grados:int):
    
    return robot, matriz

def face(robot, matriz, orientacion:int):
    
    return robot, matriz

def put(robot, matriz, cantidad:int, tipo:str):
    
    return robot, matriz

def pick(robot, matriz, cantidad:int, tipo:str):
    
    return robot, matriz

def move_to(robot, matriz, casillas, direccion):

    return robot, matriz

def move_in(robot, matriz, casillas, orientacion):

    return robot, matriz

def jump_to(robot, matriz, casillas, direccion):

    return robot, matriz

def jump_in(robot, matriz, casillas, orientacion):

    return robot, matriz