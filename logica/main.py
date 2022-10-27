import gamelib
import batalla
import equipo
import busquedas
import carga

POKE_WIDTH = 200

def comprobar_si_pokemon_murio(e,diccionario_equipos):
    """
    Comprueba si el pokemon murio 
    """

    if e.poke_activo.vivo() == False:
        nombre_pokemon = gamelib.input(f"{e.poke_activo.nombre_pokemon} está muerto, elije otro pokemon: ")
        while busquedas.determinar_si_pokemon_esta_en_el_equipo(e.nombre_equipo,nombre_pokemon,diccionario_equipos) == False:
            nombre_pokemon = gamelib.input("No tienes ese pokemon disponible en este equipo, prueba otro: ")
                    
        e.elegir_pokemon(nombre_pokemon)

def inicializar(diccionario_equipos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos):
    """
    Recibe todas las estructuras de datos con la informacion necesaria para inicializar
    el programa y con eso crea los equipos.
    Pregunta que equipos y pokemones queres utilizar al inciar
    """
    nombre_e1 = gamelib.input("Equipo 1: ")
    while busquedas.determinar_si_equipo_existe(nombre_e1,diccionario_equipos) == False:
        nombre_e1 = gamelib.input("No tienes ningún equipo con ese nombre, prueba otro: ")

    nombre_e2 = gamelib.input("Equipo 2: ")
    while busquedas.determinar_si_equipo_existe(nombre_e2,diccionario_equipos) == False:
        nombre_e2 = gamelib.input("No tienes ningún equipo con ese nombre, prueba otro: ")

    e1 = equipo.Equipo(nombre_e1,diccionario_equipos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos)
    e2 = equipo.Equipo(nombre_e2,diccionario_equipos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos)

    nombre_pokemon1 = gamelib.input("Pokemon 1: ")
    while busquedas.determinar_si_pokemon_esta_en_el_equipo(nombre_e1,nombre_pokemon1,diccionario_equipos) == False:
        nombre_pokemon1 = gamelib.input("No tienes ese pokemon en este equipo, prueba otro: ")

    nombre_pokemon2 = gamelib.input("Pokemon 2: ")
    while busquedas.determinar_si_pokemon_esta_en_el_equipo(nombre_e2,nombre_pokemon2,diccionario_equipos) == False:
        nombre_pokemon2 = gamelib.input("No tienes ese pokemon en este equipo, prueba otro: ")

    e1.elegir_pokemon(nombre_pokemon1)
    e2.elegir_pokemon(nombre_pokemon2)

    return e1,e2

def mostrar_campo_batalla(equipo1, equipo2):
    """
    Muestra el campo de batalla con funciones de gamelib
    """
    gamelib.draw_rectangle(50,30,950,670, fill='white')
    gamelib.draw_text("Pulsa 1,2 y 3 en orden para jugar", 250, 80, size=12, bold=True, fill='green')

    gamelib.draw_text(equipo1.nombre_equipo, 120, 480, size=18, bold=True, fill='gray')
    gamelib.draw_image("imgs/trainer1.gif", 70, 530)

    gamelib.draw_text(equipo2.nombre_equipo, 820, 110, size=18, bold=True, fill='gray')
    gamelib.draw_image("imgs/trainer2.gif", 770, 160)

    mostrar_pokeballs(equipo1, 90, 505)
    mostrar_pokeballs(equipo2, 790, 135)

    mostrar_hp(equipo1.poke_activo, 250, 460, POKE_WIDTH)
    gamelib.draw_image(equipo1.poke_activo.imagen, 250, 480)
    mostrar_hp(equipo2.poke_activo, 550, 120, POKE_WIDTH)
    gamelib.draw_image(equipo2.poke_activo.imagen, 550, 140)
    
def mostrar_hp(poke, x, y, width):
    """
    Genera una barra de vida que cambia de color cuanto menor sea el hp del pokemon
    """
    porcentaje_restante = poke.hp / poke.hp_total
    if porcentaje_restante > 0.7:
        color = "green"
    elif 0.2 < porcentaje_restante <= 0.7:
        color = "yellow"
    else:
        color = "red"
    gamelib.draw_text(f"Hp: {poke.hp}", x, y-15, size=15, bold=True, fill='black')
    gamelib.draw_rectangle(x, y, x + width, y + 10, fill='gray')
    gamelib.draw_rectangle(x, y, x + (width * porcentaje_restante), y + 10, fill=color)

def mostrar_pokeballs(equipo, x_inicial, y):
    """
    Muestra un pokeball por cada pokemon del equipo. Se pone gris si el pokemon está muerto
    """
    for i, poke in enumerate(equipo.pokemons):
        if poke.vivo():
            gamelib.draw_image("imgs/pokeball.gif", x_inicial + i * 20, y)
        if not  poke.vivo():
            gamelib.draw_image("imgs/pokeball_gray.gif", x_inicial + i * 20, y)

def main():
    
    gamelib.resize(1000,700)

    diccionario_datos_poke = carga.crear_diccionario_datos_poke()
    diccionario_equipos = carga.crear_diccionario_equipos()
    diccionario_detalle_mov = carga.crear_diccionario_detalle_movimientos()
    tabla_tipos = carga.crear_tabla_tipos()

    e1,e2 = inicializar(diccionario_equipos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos)
    turno = 0

    b = batalla.Batalla(e1,e2)
    
    while gamelib.is_alive():

        gamelib.draw_begin()
        
        mostrar_campo_batalla(e1,e2)
        
        if not e1.estan_vivos():
            gamelib.say(f"{e2.nombre_equipo} a ganado!")
            break
        if not e2.estan_vivos():
            gamelib.say(f"{e1.nombre_equipo} a ganado")
            break

        if e1.poke_activo.vivo() == False or e2.poke_activo.vivo() == False:
            turno = 0
        
        comprobar_si_pokemon_murio(e1,diccionario_equipos)
        comprobar_si_pokemon_murio(e2,diccionario_equipos)
        
        gamelib.draw_end()

        ev = gamelib.wait()

        if not ev:
            break
    
        if ev.type == gamelib.EventType.KeyPress and ev.key == "1":
            if turno == 0:
                b.preguntar_movimientos()
                turno = 1
            
        if ev.type == gamelib.EventType.KeyPress and ev.key == "2":
            if turno == 1:
                b.turno_primero()
                turno = 2

        if ev.type == gamelib.EventType.KeyPress and ev.key == "3":
            if turno == 2:
                b.turno_segundo()
                b.terminar_turno()
                turno = 0

        if ev.type == gamelib.EventType.KeyPress and ev.key == 'Escape':
            break
    
gamelib.init(main)