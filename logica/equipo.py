import pokemon

class Equipo:

    def __init__(self,nombre_equipo,diccionario_de_equipos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos):
        
        self.nombre_equipo = nombre_equipo
        self.pokemons = []

        for nombre_pokemon,movimientos in diccionario_de_equipos[nombre_equipo].items():
                self.pokemons.append(pokemon.Pokemon(nombre_pokemon,movimientos,diccionario_datos_poke,diccionario_detalle_mov,tabla_tipos))

        self.poke_activo = self.pokemons[0]

    def elegir_pokemon(self,nombre_pokemon):
        """
        Te permite elegir un pokemon, se utiliza cuando se inicia el juego y cada vez que
        un pokemon muere
        """
        for poke in self.pokemons:
            if poke.nombre_pokemon == nombre_pokemon:
                self.poke_activo = poke
    
    def estan_vivos(self):
        """
        Revisa si algun pokemon del equipo sigue vivo
        """
        for poke in self.pokemons:
            if poke.vivo():
                return True
        
        return False
    
    