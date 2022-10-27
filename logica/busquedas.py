TIPOS_DE_POKEMON = 18

def devolver_datos_pokemon(pokemon,diccionario_datos_pokemon):
    """
    Devuelve todos los parametros de un pokemon, recibe el nombre del pokemon y el diccionario
    con todos los datos
    """
    return diccionario_datos_pokemon[pokemon]

def determinar_si_equipo_existe(nombre_equipo,diccionario_equipos):
    """
    Determina si el equipo existe, recibe el nombre a comprobar y el diccionario con todos los 
    equipos
    """
    if nombre_equipo not in diccionario_equipos.keys():
        return False
    return True

def determinar_si_pokemon_esta_en_el_equipo(nombre_equipo,nombre_pokemon,diccionario_equipos):
    """
    Determina si el pokemon esta en el equipo que seleccionaste, recibe el nombre del equipo
    y del pokemon, junto con el diccionario de todos los equipos
    """
    if nombre_pokemon not in diccionario_equipos[nombre_equipo].keys():
        return False
    return True

def devolver_multiplicador_tipos(tipo_mov_ataque,tipos_pokemon_defensa,tabla_tipos):
    """
    Devuelve la efectividad de un ataque hacia un determinado pokemon
    recibe el tipo de mov del atacante, el tipo del pokemon a la defensa y la tabla de tipos
    """
    numero_columna = 0
    numero_fila = 0

    for atacante in tabla_tipos[0]:
        if atacante == tipo_mov_ataque:
            break
        else:
            numero_columna+=1

    for defensor in tabla_tipos[0]:
        if defensor in tipos_pokemon_defensa:
            break
        else:
            numero_fila += 1

    return tabla_tipos[numero_fila][numero_columna]

def determinar_categoria_de_movimiento(movimiento,diccionario_detalle_mov):
    """
    Devuelve la categoria del movimiento, recibe el movimiento y el diccionario con
    los detalles de cada movimiento
    """
    pos_categoria = 1
    return diccionario_detalle_mov[movimiento][pos_categoria]

def determinar_si_movimiento_y_pokemon_coinciden(pokemon,movimiento,diccionario_detalle_mov,diccionario_poke):
    """
    Determina si el tipo del movimiento y el del pokemon que lo realiza coinciden para realizar el 
    multiplicador de STAB, recibe el pokemon, movimiento, el diccionario con los detalles 
    de cada movimiento y el diccionario con los datos de los pokemones
    """
    pos_tipo_poke = 3
    pos_tipo_mov = 5
    if diccionario_poke[pokemon][pos_tipo_poke] == diccionario_detalle_mov[movimiento][pos_tipo_mov]:
        return True
    return False

def devolver_tipo_movimiento(movimiento,diccionario_detalle_mov):
    """
    Devuelve el tipo de movimiento, recibe el movimiento y el diccionario con los detalles 
    de cada movimiento
    """
    pos_tipo_mov = 5
    return diccionario_detalle_mov[movimiento][pos_tipo_mov]
    
def determinar_objetivo_y_devolver_stats(movimiento,diccionario_detalle_mov):
    """
    Devuelve el objetivo y las stats de un movimiento, recibe el movimiento y el diccionario con
    los detalles de cada movimiento
    """
    pos_objetivo = 2
    pos_stats = 6
    return diccionario_detalle_mov[movimiento][pos_objetivo], (diccionario_detalle_mov[movimiento][pos_stats]).split(";")

def determinar_si_mov_es_de_curacion(movimiento,diccionario_detalle_mov):
    """
    Determina si el movimiento es de curacion, recibe el movimiento y el diccionario con
    los detalles de cada movimiento
    """
    pos_objetivo = 2
    pos_stats = 6

    objetivo = diccionario_detalle_mov[movimiento][pos_objetivo]
    stats = diccionario_detalle_mov[movimiento][pos_stats]

    if objetivo == "self" and stats == "":
        return True
    
    return False

def devolver_poder_base(movimiento,diccionario_detalle_mov):
    """
    Devuelve el poder base del movimiento, recibe el movimiento y el diccionario con
    los detalles de cada movimiento
    """
    pos_poder = 4

    return diccionario_detalle_mov[movimiento][pos_poder]
