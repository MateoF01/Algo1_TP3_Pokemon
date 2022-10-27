import csv

def crear_diccionario_datos_poke():
    """
    Crea y devuelve un diccionario con los datos del archivos "pokemones.csv"
    """
    diccionario_poke = {}

    with open ("pokemons.csv") as p:

        lector = csv.DictReader(p,delimiter=';')        
    
        for fila in lector:
            numero = int(fila["numero"])
            imagen = fila["imagen"]
            nombre = fila["nombre"]
            tipos = fila["tipos"]
            hp = fila["hp"]
            ataque = fila["atk"]
            defensa = fila["def"]
            spa = fila["spa"]
            spd = fila["spd"]
            spe = fila["spe"]

            diccionario_poke[nombre] = (numero,imagen,nombre,tipos,hp,ataque,defensa,spa,spd,spe) 

        return diccionario_poke

def crear_diccionario_detalle_movimientos():
    """
    Crea y devuelve un diccionario con la informacion del archivo "detalle_movimientos.csv"
    """
    diccionario = {}

    with open ("detalle_movimientos.csv") as m:
        lector = csv.DictReader(m,delimiter=",")

        for fila in lector:
            nombre_movimiento = fila["nombre"]
            categoria = fila["categoria"]
            objetivo = fila["objetivo"]
            pp = fila["pp"]
            poder = fila["poder"]
            tipo = fila["tipo"]
            stats = fila["stats"]

            diccionario[nombre_movimiento] = (nombre_movimiento,categoria,objetivo,pp,poder,tipo,stats)
        
    return diccionario

def crear_diccionario_equipos():
    """
    Crea y devuelve un diccionario con los datos del archivo "equipos.csv"
    """
    diccionario = {}
    
    with open("equipos.csv") as archivo_equipos:
        lector = csv.DictReader(archivo_equipos,delimiter=";")

        for fila in lector:
            nombre_equipo = fila["nombre_equipo"]
            pokemon = fila["pokemon"]
            movimientos = fila["movimientos"]

            if nombre_equipo not in diccionario:
                diccionario[nombre_equipo] = {}
            
            diccionario[nombre_equipo][pokemon] = movimientos
    
    return diccionario

def crear_tabla_tipos():
    """
    Crea y devuelve una tabla que contiene los multiplicadores de los ataques de los pokemons 
    a partir del archivo "tabla_tipos.csv"
    """
    matriz = []
    matriz.append(["Types","Bug","Dark","Dragon","Electric","Fairy","Fighting","Fire","Flying","Ghost","Grass","Ground","Ice","Normal","Poison","Psychic","Rock","Steel","Water"])
    
    with open ("tabla_tipos.csv") as tt:
        lector =  csv.DictReader(tt,delimiter=";")

        for fila in lector:
            tipos = fila["Types"]
            bug = fila["Bug"]
            dark = fila["Dark"]
            dragon = fila["Dragon"]
            electric = fila["Electric"]
            fairy = fila["Fairy"]
            fighting = fila["Fighting"]
            fire = fila["Fire"]
            flying = fila["Flying"]
            ghost = fila["Ghost"]
            grass = fila["Grass"]
            ground = fila["Ground"]
            ice = fila["Ice"]
            normal = fila["Normal"]
            poison = fila["Poison"]
            psychic = fila["Psychic"]
            rock = fila["Rock"]
            steel = fila["Steel"]
            water = fila["Water"]

            matriz.append([tipos,bug,dark,dragon,electric,fairy,fighting,fire,flying,ghost,grass,ground,ice,normal,poison,psychic,rock,steel,water])

    return matriz





