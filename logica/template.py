import gamelib

POKE_WIDTH = 300

def mostrar_campo_batalla(equipo1, equipo2):
    gamelib.draw_rectangle(50,30,950,670, fill='white')

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
    for i, poke in enumerate(equipo.pokemons):
        if poke.vivo():
            gamelib.draw_image("imgs/pokeball.gif", x_inicial + i * 20, y)
        if poke.vivo():
            gamelib.draw_image("imgs/pokeball_gray.gif", x_inicial + i * 20, y)
