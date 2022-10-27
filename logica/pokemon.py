import busquedas
import gamelib

HP_BASE = 110

class Pokemon:
    
    def __init__(self,nombre_pokemon,movimientos,diccionario_dato_poke,diccionario_detalle_mov,tabla_tipos):
          
        self.nombre_pokemon = nombre_pokemon
        self.movimientos = movimientos

        self.diccionario_detalle_mov = diccionario_detalle_mov
        self.diccionario_dato_poke = diccionario_dato_poke
        self.tabla_tipos = tabla_tipos
        
        numero,imagen,_,tipos,hp,ataque,defensa,spa,spd,spe = busquedas.devolver_datos_pokemon(nombre_pokemon,self.diccionario_dato_poke)

        self.numero_pokemon = numero
        self.imagen = imagen
        self.tipos = tipos
        self.hp = int(hp) + HP_BASE
        self.hp_total = int(hp) + HP_BASE
        self.ataque = int(ataque)
        self.defensa = int(defensa)
        self.velocidad = int(spe)
        self.ataque_especial = int(spa)
        self.defensa_especial = int(spd)

        self.stab = 1
        self.mdt = 1

    def STAB(self,nombre_pokemon,movimiento):
        """
        Determina si se realiza el multiplicador del movimientos STAB
        """
        if busquedas.determinar_si_movimiento_y_pokemon_coinciden(nombre_pokemon,movimiento,self.diccionario_detalle_mov,self.diccionario_dato_poke):
            self.stab = 1.5 
        else:
            self.stab = 1

    def modificador_defensor(self,tipo_mov_atacante,tipo_defensor):
        """
        Determina que tan efectivo es un ataque
        """
        self.mdt = float(busquedas.devolver_multiplicador_tipos(tipo_mov_atacante,tipo_defensor,self.tabla_tipos)) #MDT (Modificador de tipos)
        
    def atacar_physical(self,movimiento,oponente):
        """
        Calcula el daño que le hace un ataque physical al oponente y le resta la vida correspondiente
        al mismo
        """

        self.STAB(self.nombre_pokemon,movimiento)
        tipo_movimiento = busquedas.devolver_tipo_movimiento(movimiento,self.diccionario_detalle_mov)
        self.modificador_defensor(tipo_movimiento,oponente.tipos)
        
        poder_base = int(busquedas.devolver_poder_base(movimiento,self.diccionario_detalle_mov))

        daño_base = (15 * poder_base * (self.ataque / oponente.defensa) / 50) * self.stab * self.mdt
            
        oponente.hp -= daño_base
        oponente.hp = round(oponente.hp,2)

    def atacar_special(self,movimiento,oponente):
        """
        Calcula el daño que le hace un ataque special al oponente y le resta la vida correspondiente
        al mismo
        """

        self.STAB(self.nombre_pokemon,movimiento)

        tipo_movimiento = busquedas.devolver_tipo_movimiento(movimiento,self.diccionario_detalle_mov)
        self.modificador_defensor(tipo_movimiento,oponente.tipos)

        poder_base = int(busquedas.devolver_poder_base(movimiento,self.diccionario_detalle_mov))

        daño_base = (15 * poder_base * (self.ataque_especial / oponente.defensa_especial) / 50) * self.stab * self.mdt
        
        oponente.hp -= daño_base
        oponente.hp = round(oponente.hp,2)

    def movimiento_status_modificador(self,movimiento,oponente):
        """
        Determina que stat es modificada por el movimientos, y si debe afectar al oponente
        o al atacante
        """
        objetivo,stats = busquedas.determinar_objetivo_y_devolver_stats(movimiento,self.diccionario_detalle_mov)
        
        if objetivo == "normal":
            for stat in stats:
                if stat == "spe":
                    oponente.velocidad = (oponente.velocidad / 2)
                    gamelib.say(f"Se redujo la velocidad de {oponente.nombre_pokemon} a la mitad")
                if stat == "atk":
                    oponente.ataque = (oponente.ataque / 2)
                    oponente.ataque_especial = (oponente.ataque_especial / 2)
                    gamelib.say(f"Se redujo el ataque de {oponente.nombre_pokemon} a la mitad")
                if stat == "def":
                    oponente.defensa = (oponente.defensa / 2)
                    oponente.defensa_especial = (oponente.defensa_especial / 2)
                    gamelib.say(f"Se redujo la defensa de {oponente.nombre_pokemon} a la mitad")
                if stat == "":
                    gamelib.say(f"Usaste un movimiento que no hace nada, jaja saludos")

        if objetivo == "self":
            for stat in stats:
                if stat == "spe":
                    self.velocidad = (self.velocidad * 2)
                    gamelib.say(f"Se multiplico la velocidad de {self.nombre_pokemon} por 2")
                if stat == "atk":
                    self.ataque = (self.ataque * 2)
                    self.ataque_especial = (self.ataque_especial * 2)
                    gamelib.say(f"Se multiplico el ataque de {self.nombre_pokemon} por 2")
                if stat == "def":
                    self.defensa = (self.defensa * 2)
                    self.defensa_especial = (self.defensa_especial * 2)
                    gamelib.say(f"Se multiplico la defensa de {self.nombre_pokemon} por 2")
                if stat == "":
                    gamelib.say(f"Usaste un movimiento que no hace nada, jaja saludos")
        
        if objetivo == "all":
            pass

    def movimiento_curacion(self):
        """
        Recupera la mitad de la vida del pokemon
        """
        self.hp += (self.hp_total // 2)
        self.hp = round(self.hp,2)
        if self.hp >= self.hp_total:
            self.hp = self.hp_total 

    def determinar_movimiento(self,movimiento,oponente):
        """
        Determina de que categoria es el movimiento para luego realizarlo
        """
        categoria = busquedas.determinar_categoria_de_movimiento(movimiento,self.diccionario_detalle_mov)
        
        if categoria == "Physical":
            self.atacar_physical(movimiento,oponente)

            gamelib.say(f"{self.nombre_pokemon} realiza {movimiento} con STAB: x{self.stab} y efectividad x{self.mdt}")

        if categoria == "Special":
            self.atacar_special(movimiento,oponente)

            gamelib.say(f"{self.nombre_pokemon} realiza {movimiento} con STAB: x{self.stab} y efectividad x{self.mdt}")

        if categoria == "Status":
            if busquedas.determinar_si_mov_es_de_curacion(movimiento,self.diccionario_detalle_mov) == True:
                self.movimiento_curacion()

                gamelib.say(f"{self.nombre_pokemon} se curó")

            else:
                self.movimiento_status_modificador(movimiento,oponente)

    def vivo(self):
        """
        Comprueba si el pokemon está vivo
        """
        if self.hp <= 0:
            self.hp = 0
            return False
        return True







        




