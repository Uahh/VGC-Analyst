import json

class PokemonData:
    def __init__(self) -> None:
        self.moves = {}
        with open('./data/moves.json') as json_file:
            moves = json.load(json_file)

        self.pokemon_types = {}
        with open('./data/pokemon_types.json') as json_file:
            self.pokemon_types = json.load(json_file)
                
        self.pokemon = {}
        with open('./data/pokemon.json') as json_file:
            self.pokemon = json.load(json_file)

        self.types = {}
        with open('./data/types.json') as json_file:
            self.types = json.load(json_file)

    def get_pokemon_type(self, id):
        pass


    def get_move(self, name):
        name = name.lower().replace(' ', '-')
        result = None
        for move in self.moves:
            if move['identifier'] == name:
                result = move
                break
        return result

    def get_move_type(self, name):
        move = self.get_move(name)
        if move:
            return self.types[move['type_id']]
        print('Move not found: ' + name)
        return None

    def get_move_power(self, name):
        move = self.get_move(name)
        if move:
            return move['power']
        print('Move not found: ' + name)
        return None
