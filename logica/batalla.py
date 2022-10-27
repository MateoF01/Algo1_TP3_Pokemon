import gamelib
import random

class Batalla:

    def __init__(self,equipo1,equip2):
        self.equipo1 = equipo1
        self.equipo2 = equip2

        self.turno_equipo1 = False
        self.turno_equipo2 = False

        self.movimiento1 = ""
        self.movimiento2 = ""        
     
    def preguntar_movimientos(self):
        """
        Pregunta que movimientos realizara cada pokemon en el turno
        """
        
        self.movimiento1 = gamelib.input(f"Movimiento de {self.equipo1.poke_activo.nombre_pokemon}: ")
        while True:
            if self.movimiento1 not in self.equipo1.poke_activo.movimientos:
                self.movimiento1 = gamelib.input("No tienes ese movimientos, ingresa otro: ")
            else:
                break

        self.movimiento2 = gamelib.input(f"Movimiento de {self.equipo2.poke_activo.nombre_pokemon}: ")
        while True:
            if self.movimiento2 not in self.equipo2.poke_activo.movimientos:
                self.movimiento2 = gamelib.input("No tienes ese movimientos, ingresa otro: ")
            else:
                break
        
        if self.equipo1.poke_activo.velocidad > self.equipo2.poke_activo.velocidad:
            gamelib.say(f"{self.equipo1.poke_activo.nombre_pokemon} realiza su movimiento primero ")

        if self.equipo1.poke_activo.velocidad < self.equipo2.poke_activo.velocidad:
            gamelib.say(f"{self.equipo2.poke_activo.nombre_pokemon} realiza su movimiento primero ")
        
        if self.equipo1.poke_activo.velocidad == self.equipo2.poke_activo.velocidad:
            ganador = random.choice([self.equipo1,self.equipo2])
            gamelib.say(f"{ganador.poke_activo.nombre_pokemon} realiza su movimiento primero ")
        
    def turno_primero(self):
        """
        Determina que pokemon ataca primero dependiendo la velocidad de los mismos
        """
        if self.equipo1.poke_activo.velocidad > self.equipo2.poke_activo.velocidad:
            self.equipo1.poke_activo.determinar_movimiento(self.movimiento1,self.equipo2.poke_activo)
            self.turno_equipo2 = True

        elif self.equipo1.poke_activo.velocidad < self.equipo2.poke_activo.velocidad:
            self.equipo2.poke_activo.determinar_movimiento(self.movimiento2,self.equipo1.poke_activo)
            self.turno_equipo1 = True
        
        elif self.equipo1.poke_activo.velocidad == self.equipo2.poke_activo.velocidad:
            ganador = random.choice([self.equipo1,self.equipo2])
            
            if ganador == self.equipo1:
                self.equipo1.poke_activo.determinar_movimiento(self.movimiento1,self.equipo2.poke_activo)
                self.turno_equipo2 = True
            else:
                self.equipo2.poke_activo.determinar_movimiento(self.movimiento2,self.equipo1.poke_activo)
                self.turno_equipo1 = True       
    
    def turno_segundo(self):
        """
        Determina que pokemon ataca segundo dependiendo de quien atacó primero
        """
        if self.turno_equipo1 == True:
            self.equipo1.poke_activo.determinar_movimiento(self.movimiento1,self.equipo2.poke_activo)

        if self.turno_equipo2 == True:
            self.equipo2.poke_activo.determinar_movimiento(self.movimiento2,self.equipo1.poke_activo)

    def terminar_turno(self):
        """
        Reinicia el turno
        """
        self.turno_equipo1 = False
        self.turno_equipo2 = False
