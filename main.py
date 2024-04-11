import requests
import data
from copy import deepcopy
from bs4 import BeautifulSoup

team = []
super_effective = []
not_very_effective = []

r = requests.get('https://pokepast.es/7aaefb3db6d180b3')
soup = BeautifulSoup(r.text)
pokes = soup.findAll('article')

for poke in pokes:
    img_path = poke.findAll('img')[0]['src']
    poke = poke.findAll('pre')[0]
    cur_pokemon = poke.text.split('\n')
    temp_pokemon = deepcopy(data.pokemon_dict)
    move = poke.findAll('span')
    
    temp_pokemon['name'] = cur_pokemon[0].split('@')[0].strip()
    temp_pokemon['tera_type'] = cur_pokemon[3].split(':')[1].strip()
    temp_pokemon['id'] = img_path.split('/')[-1].split('-')[0]
    temp_pokemon['move_1']['name'] = cur_pokemon[4][2:].strip()
    temp_pokemon['move_2']['name'] = cur_pokemon[5][2:].strip()
    temp_pokemon['move_3']['name'] = cur_pokemon[6][2:].strip()
    temp_pokemon['move_4']['name'] = cur_pokemon[7][2:].strip()
    temp_pokemon['move_1']['type'] = data.get_move_type(temp_pokemon['move_1']['name'])
    temp_pokemon['move_2']['type'] = data.get_move_type(temp_pokemon['move_2']['name'])
    temp_pokemon['move_3']['type'] = data.get_move_type(temp_pokemon['move_3']['name'])
    temp_pokemon['move_4']['type'] = data.get_move_type(temp_pokemon['move_4']['name'])
    temp_pokemon['move_1']['power'] = data.get_move_power(temp_pokemon['move_1']['name'])
    temp_pokemon['move_2']['power'] = data.get_move_power(temp_pokemon['move_2']['name'])
    temp_pokemon['move_3']['power'] = data.get_move_power(temp_pokemon['move_3']['name'])
    temp_pokemon['move_4']['power'] = data.get_move_power(temp_pokemon['move_4']['name'])

    type_conut = 1
    for type in data.pokemon_types:
        if temp_pokemon['id'] == type['pokemon_id']:
            temp_pokemon['pokemon_type_' + str(type_conut)] = data.types[int(data['type_id']) - 1]['identifier']
            type_conut += 1

    team.append(temp_pokemon)


for pokemon in team:
    print(pokemon['name'])
    print(pokemon['tera_type'])
    print(pokemon['pokemon_type_1'])
    print(pokemon['pokemon_type_2'])
    print(pokemon['move_1']['name'])
    print(pokemon['move_1']['type'])
    print(pokemon['move_2']['name'])
    print(pokemon['move_2']['type'])
    print(pokemon['move_3']['name'])
    print(pokemon['move_3']['type'])
    print(pokemon['move_4']['name'])
    print(pokemon['move_4']['type'])
    print(pokemon['move_1']['power'])
    print(pokemon['move_2']['power'])
    print(pokemon['move_3']['power'])
    print(pokemon['move_4']['power'])
    print('')
