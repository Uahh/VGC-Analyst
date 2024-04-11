import requests
import data
from copy import deepcopy
from bs4 import BeautifulSoup

class TypeAnalysis:
    def __init__(self, team_url):
        self.type_dict = {
            'normal': {
                'id': 1,
                'no_effect': ['ghost'],
                'super_effective': ['rock', 'steel'],
                'not_very_effective': []
            },
            'fire': {
                'id': 2,
                'no_effect': [],
                'super_effective': ['grass', 'ice', 'bug', 'steel'],
                'not_very_effective': ['fire', 'water', 'rock', 'dragon']
            },
            'water': {
                'id': 3,
                'no_effect': [],
                'super_effective': ['fire', 'ground', 'rock'],
                'not_very_effective': ['water', 'grass', 'dragon']
            },
            'electric': {
                'id': 4,
                'no_effect': ['ground'],
                'super_effective': ['water', 'flying'],
                'not_very_effective': ['electric', 'grass', 'dragon']
            },
            'grass': {
                'id': 5,
                'no_effect': [],
                'super_effective': ['water', 'ground', 'rock'],
                'not_very_effective': ['fire', 'grass', 'bug', 'flying', 'posion', 'dragon']
            },
            'ice': {
                'id': 6,
                'no_effect': [],
                'super_effective': ['grass', 'ground', 'flying', 'dragon'],
                'not_very_effective': ['fire', 'water', 'ice', 'steel']
            },
            'fighting': {
                'id': 7,
                'no_effect': ['ghost'],
                'super_effective': ['normal', 'ice', 'rock', 'dark', 'steel'],
                'not_very_effective': ['posion', 'flying', 'psychic', 'bug', 'fairy']
            },
            'posion': {
                'id': 8,
                'no_effect': ['steel'],
                'super_effective': ['grass', 'fairy'],
                'not_very_effective': ['posion', 'ground', 'rock', 'ghost']
            },
            'ground': {
                'id': 9,
                'no_effect': ['flying'],
                'super_effective': ['fire', 'electric', 'rock', 'posion', 'steel'],
                'not_very_effective': ['grass', 'bug']
            },
            'flying': {
                'id': 10,
                'no_effect': [],
                'super_effective': ['grass', 'fighting', 'bug'],
                'not_very_effective': ['electric', 'rock', 'steel']
            },
            'psychic': {
                'id': 11,
                'no_effect': ['dark'],
                'super_effective': ['fighting', 'posion'],
                'not_very_effective': ['psychic', 'steel']
            },
            'bug': {
                'id': 12,
                'no_effect': [],
                'super_effective': ['grass', 'psychic', 'dark'],
                'not_very_effective': ['fire', 'fighting', 'posion', 'flying', 'ghost', 'steel', 'fairy']
            },
            'rock': {
                'id': 13,
                'no_effect': [],
                'super_effective': ['fire', 'ice', 'flying', 'bug'],
                'not_very_effective': ['fighting', 'ground', 'steel']
            },
            'ghost': {
                'id': 14,
                'no_effect': ['normal'],
                'super_effective': ['psychic', 'ghost'],
                'not_very_effective': ['dark']
            },
            'dragon': {
                'id': 15,
                'no_effect': ['fairy'],
                'super_effective': ['dragon'],
                'not_very_effective': ['steel']
            },
            'dark': {
                'id': 16,
                'no_effect': [],
                'super_effective': ['psychic', 'ghost'],
                'not_very_effective': ['fighting', 'dark', 'fairy']
            },
            'steel': {
                'id': 17,
                'no_effect': [],
                'super_effective': ['ice', 'rock', 'fairy'],
                'not_very_effective': ['fire', 'water', 'electric', 'steel']
            },
            'fairy': {
                'id': 18,
                'no_effect': [],
                'super_effective': ['fighting', 'dragon', 'dark'],
                'not_very_effective': ['fire', 'ground', 'steel']
            },
        }
        team = []
        r = requests.get(team_url)
        soup = BeautifulSoup(r.text)
        pokes = soup.findAll('article')

        for poke in pokes:
            img_path = poke.findAll('img')[0]['src']
            poke = poke.findAll('pre')[0]
            cur_pokemon = poke.text.split('\n')
            temp_pokemon = deepcopy(data.pokemon_dict)

            temp_pokemon['name'] = cur_pokemon[0].split('@')[0].strip()
            temp_pokemon['tera_type'] = cur_pokemon[3].split(':')[1].strip()
            temp_pokemon['id'] = img_path.split('/')[-1].split('-')[0]
            temp_pokemon['move_1']['name'] = cur_pokemon[4][2:].strip()
            temp_pokemon['move_2']['name'] = cur_pokemon[5][2:].strip()
            temp_pokemon['move_3']['name'] = cur_pokemon[6][2:].strip()
            temp_pokemon['move_4']['name'] = cur_pokemon[7][2:].strip()
            temp_pokemon['move_1']['type'] = data.get_move_type(
                temp_pokemon['move_1']['name'])
            temp_pokemon['move_2']['type'] = data.get_move_type(
                temp_pokemon['move_2']['name'])
            temp_pokemon['move_3']['type'] = data.get_move_type(
                temp_pokemon['move_3']['name'])
            temp_pokemon['move_4']['type'] = data.get_move_type(
                temp_pokemon['move_4']['name'])
            temp_pokemon['move_1']['power'] = data.get_move_power(
                temp_pokemon['move_1']['name'])
            temp_pokemon['move_2']['power'] = data.get_move_power(
                temp_pokemon['move_2']['name'])
            temp_pokemon['move_3']['power'] = data.get_move_power(
                temp_pokemon['move_3']['name'])
            temp_pokemon['move_4']['power'] = data.get_move_power(
                temp_pokemon['move_4']['name'])

            type_conut = 1
            for type in data.pokemon_types:
                if temp_pokemon['id'] == type['pokemon_id']:
                    temp_pokemon['pokemon_type_' +
                                str(type_conut)] = data.types[int(type['type_id']) - 1]['identifier']
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

    def atk_result(type_list):
        no_effect = []
         super_effective = []
          not_very_effective = []
           for type in type_list:
                if type == 'normal':
                    no_effect.append('ghost')
                    not_very_effective.append('rock', 'steel')
                if type == 'fire':
                    super_effective.append('grass', 'ice', 'bug', 'steel')
                    not_very_effective.append(
                        'fire', 'water', 'rock', 'dragon')
                if type == 'water':
                    super_effective.append('fire', 'ground', 'rock')
                    not_very_effective.append('water', 'grass', 'dragon')
                if type == 'electric':
                    no_effect.append('ground')
                    super_effective.append('water', 'flying')
                    not_very_effective.append('electric', 'grass', 'dragon')
                if type == 'grass':
                    super_effective.append('water', 'ground', 'rock')
                    not_very_effective.append(
                        'fire', 'grass', 'bug', 'flying', 'posion', 'dragon')
                if type == 'ice':
                    super_effective.append(
                        'grass', 'ground', 'flying', 'dragon')
                    not_very_effective.append('fire', 'water', 'ice', 'steel')
                if type == 'fighting':
                    no_effect.append('ghost')
                    super_effective.append(
                        'normal', 'ice', 'rock', 'dark', 'steel')
                    not_very_effective.append(
                        'posion', 'flying', 'psychic', 'bug', 'fairy')
                if type == 'posion':
                    no_effect.append('steel')
                    super_effective.append('grass', 'fairy')
                    not_very_effective.append(
                        'posion', 'ground', 'rock', 'ghost')
                if type == 'ground':
                    no_effect.append('flying')
                    super_effective.append(
                        'fire', 'electric', 'rock', 'posion', 'steel')
                    not_very_effective.append('grass', 'bug')
                if type == 'flying':
                    super_effective.append('grass', 'fighting', 'bug')
                    not_very_effective.append('electric', 'rock', 'steel')
                if type == 'psychic':
                    no_effect.append('dark')
                    super_effective.append('fighting', 'posion')
                    not_very_effective.append('psychic', 'steel')
                if type == 'bug':
                    super_effective.append('grass', 'psychic', 'dark')
                    not_very_effective.append(
                        'fire', 'fighting', 'posion', 'flying', 'ghost', 'steel', 'fairy')
                if type == 'rock':
                    super_effective.append('fire', 'ice', 'flying', 'bug')
                    not_very_effective.append('fighting', 'ground', 'steel')
                if type == 'ghost':
                    no_effect.append('normal')
                    super_effective.append('psychic', 'ghost')
                    not_very_effective.append('dark')
                if type == 'dragon':
                    no_effect.append('fairy')
                    super_effective.append('dragon')
                    not_very_effective.append('steel')
                if type == 'dark':
                    super_effective.append('psychic', 'ghost')
                    not_very_effective.append('fighting', 'dark', 'fairy')
                if type == 'steel':
                    super_effective.append('ice', 'rock', 'fairy')
                    not_very_effective.append(
                        'fire', 'water', 'electric', 'steel')
                if type == 'fairy':
                    super_effective.append('fighting', 'dragon', 'dark')
                    not_very_effective.append('fire', 'ground', 'steel')

            print(no_effect)
            print(super_effective)
            print(not_very_effective)
