import json

moves = {}
with open('./data/moves.json') as json_file:
    moves = json.load(json_file)

pokemon_types = {}
with open('./data/pokemon_types.json') as json_file:
    pokemon_types = json.load(json_file)

pokemon = {}
with open('./data/pokemon.json') as json_file:
    pokemon = json.load(json_file)

types = {}
with open('./data/types.json') as json_file:
    types = json.load(json_file)

pokemon_dict = {
    'id': '',
    'name': '',
    'pokemon_type_1': '',
    'pokemon_type_2': '',
    'tera_type': '',
    'move_1': {
        'name': '',
        'type': '',
        'power': '',
    },
    'move_2': {
        'name': '',
        'type': '',
        'power': '',
    },
    'move_3': {
        'name': '',
        'type': '',
        'power': '',
    },
    'move_4': {
        'name': '',
        'type': '',
        'power': '',
    }
}


def get_move(name):
    name = name.lower().replace(' ', '-')
    result = None
    for move in moves:
        if move['identifier'] == name:
            result = move
            break
    return result


def get_move_type(name):
    move = get_move(name)
    if move:
        return types[int(move['type_id']) - 1]['identifier']
    print('Move not found: ' + name)
    return None


def get_move_power(name):
    move = get_move(name)
    if move:
        return move['power']
    print('Move not found: ' + name)
    return None
