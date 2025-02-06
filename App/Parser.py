# Conjuntos para almacenar variables y procedimientos definidos
variables = set()
procedimientos = {}

def parse(archivo):
    """Funcion que analiza todas las lineas del archivo dado para evaluar si son validas o no, evalua 
    que tipo de linea es cada uno y llama a otra funcion para hacer esta verificacion

    Args:
        filas: archivo que contiene todas las filas a analizar

    Returns:
        bool: True si no se encontro ningun error, false de lo contrario
    """
    for fila in archivo:
        # Corregimos el formato y vemos que tipo de fila es cada fila
        fila = fila.strip()
        
        if fila.startswith('|') and fila.endswith('|'):
            parse_variables(fila)
            
        elif fila.startswith('proc'):
            parse_procedimiento(fila)
            
        elif fila:
            if not parse_instruccion(fila):
                print(f"Error de sintaxis en la línea: {fila}")
                return False
    return True


def parse_variables(fila):
    """Función que analiza y verifica si las variables estan bien definidas y las almacena en un set

    Args:
        fila: fila que contiene la variable que se desea examinar
        
        Ejemplo: | nom x y one |
    """
    # Se corrige el formato y verificamos que la variable dada este en minuscula y sea alfanumerica
    vars_encontradas = fila.strip('|').split()
    
    for var in vars_encontradas:
        if var[0].islower() and var.isalnum():
            variables.add(var)
        else:
            print(f"Nombre de variable inválido: {var}")


def parse_procedimiento(fila):
    """Funcion que analiza y verifica si los procedimientos estan bien definidas y a almacena en un diccionario

    Args:
        fila: fila que contiene el procedimiento que se desea examinar
        
        Ejemplo: proc putChips: n andBalloons: m
    """
    partes = fila.split()
    # Verificamos si esta bien definido y corregimos su formato elimando partes inecesarias para comprobar su gramatica
    if len(partes) >= 2 and partes[0] == 'proc':
        nombre_procedimiento = partes[1].rstrip(':')
        if nombre_procedimiento[0].islower() and nombre_procedimiento.isalnum():
            procedimientos[nombre_procedimiento] = []
        else:
            print(f"Nombre de procedimiento inválido: {nombre_procedimiento}")
    else:
        print(f"Definición de procedimiento inválida: {fila}")


def parse_instruccion(fila):
    """Funcion que analiza y verifica si las instrucciones dadas estan bien definidas, 
    tambien verifica asignaciones, comandos y llamadas a procedimientos

    Args:
        fila (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Verificamos si se trata de la asignacion de una variable previamente definida
    # Ejemplo: "c := n ."
    if ':=' in fila:
        partes = fila.split(':=') # ['c', 'n']
        if len(partes) == 2 and partes[0].strip() in variables:
            valor = partes[1].strip().rstrip('.') # n
            if valor.isdigit() or valor in variables:
                return True
            
    elif fila.endswith('.'):
        comando_completo = fila[:-1].strip().split()
        if not comando_completo:
            return False
        comando = comando_completo[0]

        # Instrucciones basicas reconocidas por el robot
        if comando == 'goto' and 'with:' in comando_completo:
            return True
        if comando == 'move' and ('toThe:' in comando_completo or 'inDir:' in comando_completo):
            return True
        if comando == 'turn' and any(d in comando_completo for d in ['#left', '#right', '#around']):
            return True
        if comando == 'face' and any(o in comando_completo for o in ['#north', '#south', '#west', '#east']):
            return True
        if comando in ['put', 'pick'] and 'ofType:' in comando_completo:
            return True
        if comando == 'jump' and ('toThe:' in comando_completo or 'inDir:' in comando_completo):
            return True
        if comando == 'nop':
            return True

        # Condicionales y bucles
        if comando == 'if' and 'then:' in comando_completo and 'else:' in comando_completo:
            return True
        if comando == 'while' and 'do:' in comando_completo:
            return True
        if comando == 'for' and 'repeat:' in comando_completo:
            return True

        # Buscamos en los procedimientos previamente guardados
        if comando in procedimientos:
            return True
    return False