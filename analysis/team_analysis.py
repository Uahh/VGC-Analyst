import requests
import data_import
from copy import deepcopy
from bs4 import BeautifulSoup

class TeamAnalysis:
    def __init__(self, team_url, debug=False):
        self.team_url = team_url
        self.debug = debug
        self.pokemon_dict = {
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
            },
            'defense_type_dict': ''
        }
        self.all_type = ['normal', 'fire', 'water', 'electric', 'grass', 'ice', 'fighting', 'poison', 'ground', 'flying', 'psychic', 'bug', 'rock', 'ghost', 'dragon', 'dark', 'steel', 'fairy']
        self.attack_type_relationship_dict = {
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
                'not_very_effective': ['fire', 'grass', 'bug', 'flying', 'poison', 'dragon']
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
                'not_very_effective': ['poison', 'flying', 'psychic', 'bug', 'fairy']
            },
            'poison': {
                'id': 8,
                'no_effect': ['steel'],
                'super_effective': ['grass', 'fairy'],
                'not_very_effective': ['poison', 'ground', 'rock', 'ghost']
            },
            'ground': {
                'id': 9,
                'no_effect': ['flying'],
                'super_effective': ['fire', 'electric', 'rock', 'poison', 'steel'],
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
                'super_effective': ['fighting', 'poison'],
                'not_very_effective': ['psychic', 'steel']
            },
            'bug': {
                'id': 12,
                'no_effect': [],
                'super_effective': ['grass', 'psychic', 'dark'],
                'not_very_effective': ['fire', 'fighting', 'poison', 'flying', 'ghost', 'steel', 'fairy']
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
        self.defense_type_relationship_dict = {
            'normal': {
                'id': 1,
                'no_effect': ['ghost'],
                'super_effective': ['fighting'],
                'not_very_effective': []
            },
            'fire': {
                'id': 2,
                'no_effect': [],
                'super_effective': ['water', 'rock', 'rock'],
                'not_very_effective': ['fire', 'grass', 'ice', 'bug', 'steel', 'fairy']
            },
            'water': {
                'id': 3,
                'no_effect': [],
                'super_effective': ['electric', 'grass'],
                'not_very_effective': ['fire', 'water', 'ice', 'steel']
            },
            'electric': {
                'id': 4,
                'no_effect': [],
                'super_effective': ['ground'],
                'not_very_effective': ['electric', 'flying', 'steel']
            },
            'grass': {
                'id': 5,
                'no_effect': [],
                'super_effective': ['fire', 'ice', 'poison', 'flying', 'bug'],
                'not_very_effective': ['water', 'electric', 'grass', 'ground']
            },
            'ice': {
                'id': 6,
                'no_effect': [],
                'super_effective': ['fire', 'fighting', 'rock', 'steel'],
                'not_very_effective': ['ice']
            },
            'fighting': {
                'id': 7,
                'no_effect': [],
                'super_effective': ['flying', 'psychic', 'fairy'],
                'not_very_effective': ['bug', 'rock', 'dark']
            },
            'poison': {
                'id': 8,
                'no_effect': [],
                'super_effective': ['ground', 'psychic'],
                'not_very_effective': ['grass', 'fighting', 'poison', 'bug', 'fairy']
            },
            'ground': {
                'id': 9,
                'no_effect': ['electric'],
                'super_effective': ['water', 'grass', 'ice'],
                'not_very_effective': ['poison', 'rock']
            },
            'flying': {
                'id': 10,
                'no_effect': ['ground'],
                'super_effective': ['electric', 'ice', 'rock'],
                'not_very_effective': ['grass', 'fighting', 'bug']
            },
            'psychic': {
                'id': 11,
                'no_effect': [],
                'super_effective': ['bug', 'ghost', 'dark'],
                'not_very_effective': ['fighting', 'psychic']
            },
            'bug': {
                'id': 12,
                'no_effect': [],
                'super_effective': ['fire', 'flying', 'rock'],
                'not_very_effective': ['grass', 'fighting', 'ground']
            },
            'rock': {
                'id': 13,
                'no_effect': [],
                'super_effective': ['water', 'grass', 'fighting', 'ground', 'steel'],
                'not_very_effective': ['normal', 'fire', 'poison', 'flying']
            },
            'ghost': {
                'id': 14,
                'no_effect': ['normal', 'fighting'],
                'super_effective': ['ghost', 'dark'],
                'not_very_effective': ['poison', 'bug']
            },
            'dragon': {
                'id': 15,
                'no_effect': [],
                'super_effective': ['ice', 'dragon', 'fairy'],
                'not_very_effective': ['fire', 'water', 'electric', 'grass']
            },
            'dark': {
                'id': 16,
                'no_effect': ['psychic'],
                'super_effective': ['fighting', 'bug', 'fairy'],
                'not_very_effective': ['ghost', 'dark']
            },
            'steel': {
                'id': 17,
                'no_effect': [],
                'super_effective': ['fire', 'fighting', 'ground'],
                'not_very_effective': ['normal', 'grass', 'ice', 'flying', 'psychic', 'bug', 'rock', 'dragon', 'steel', 'fairy']
            },
            'fairy': {
                'id': 18,
                'no_effect': ['dragon'],
                'super_effective': ['poison', 'steel'],
                'not_very_effective': ['fighting', 'bug', 'dark']
            },
        }
        self.defense_type_dict = {
            'normal': 1,
            'fire': 1,
            'water': 1,
            'electric': 1,
            'grass': 1,
            'ice': 1,
            'fighting': 1,
            'poison': 1,
            'ground': 1,
            'flying': 1,
            'psychic': 1,
            'bug': 1,
            'rock': 1,
            'ghost': 1,
            'dragon': 1,
            'dark': 1,
            'steel': 1,
            'fairy': 1,
        }
        self.damage_dict = {
            'normal': 0,
            'fire': 0,
            'water': 0,
            'electric': 0,
            'grass': 0,
            'ice': 0,
            'fighting': 0,
            'poison': 0,
            'ground': 0,
            'flying': 0,
            'psychic': 0,
            'bug': 0,
            'rock': 0,
            'ghost': 0,
            'dragon': 0,
            'dark': 0,
            'steel': 0,
            'fairy': 0,
        }

    def team_format(self):
        team = []
        r = requests.get(self.team_url)
        soup = BeautifulSoup(r.text)
        pokes = soup.findAll('article')

        for pokemon in pokes:
            img_path = pokemon.findAll('img')[0]['src']
            pokemon = pokemon.findAll('pre')[0]
            cur_pokemon = pokemon.text.split('\n')
            for text in cur_pokemon:
                if 'Level:' in text:
                    cur_pokemon.remove(text)
            temp_pokemon = deepcopy(self.pokemon_dict)

            temp_pokemon['name'] = cur_pokemon[0].split('@')[0].strip()
            temp_pokemon['tera_type'] = cur_pokemon[2].split(':')[1].strip()
            temp_pokemon['id'] = img_path.split('/')[-1].split('-')[0]
            temp_pokemon['types'] = data_import.pokemon_types[temp_pokemon['id']]
            temp_pokemon['move_1']['name'] = cur_pokemon[3][2:].strip()
            temp_pokemon['move_2']['name'] = cur_pokemon[4][2:].strip()
            temp_pokemon['move_3']['name'] = cur_pokemon[5][2:].strip()
            temp_pokemon['move_4']['name'] = cur_pokemon[6][2:].strip()
            temp_pokemon['move_1']['type'] = data_import.get_move_type(temp_pokemon['move_1']['name'])
            temp_pokemon['move_2']['type'] = data_import.get_move_type(temp_pokemon['move_2']['name'])
            temp_pokemon['move_3']['type'] = data_import.get_move_type(temp_pokemon['move_3']['name'])
            temp_pokemon['move_4']['type'] = data_import.get_move_type(temp_pokemon['move_4']['name'])
            temp_pokemon['move_1']['power'] = data_import.get_move_power(temp_pokemon['move_1']['name'])
            temp_pokemon['move_2']['power'] = data_import.get_move_power(temp_pokemon['move_2']['name'])
            temp_pokemon['move_3']['power'] = data_import.get_move_power(temp_pokemon['move_3']['name'])
            temp_pokemon['move_4']['power'] = data_import.get_move_power(temp_pokemon['move_4']['name'])

            team.append(temp_pokemon)
        self.team = team
        if self.debug:
            for pokemon in team:
                print(pokemon['name'])
                print(pokemon['tera_type'])
                print(pokemon['types'])
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

    def defense_analysis(self):
        self.defense_type_analysis()
        self.very_defense_analysis()

    def defense_type_analysis(self):
        for pokemon in self.team:
            cur_damage_type_dict = deepcopy(self.defense_type_dict)
            type_1 = pokemon['types'][0]
            
            type_1_no_effect = self.defense_type_relationship_dict[type_1]['no_effect']
            type_1_super_effective = self.defense_type_relationship_dict[type_1]['super_effective']
            type_1_not_very_effective = self.defense_type_relationship_dict[type_1]['not_very_effective']
            for i in type_1_no_effect:
                cur_damage_type_dict[i] = 0
            for i in type_1_super_effective:
                cur_damage_type_dict[i] = 2
            for i in type_1_not_very_effective:
                cur_damage_type_dict[i] = 0.5
            
            type_2 = ''
            if len(pokemon['types']) > 1:
                type_2 = pokemon['types'][1]
                type_2_no_effect = self.defense_type_relationship_dict[type_2]['no_effect']
                type_2_super_effective = self.defense_type_relationship_dict[type_2]['super_effective']
                type_2_not_very_effective = self.defense_type_relationship_dict[type_2]['not_very_effective']
                for i in type_2_no_effect:
                    cur_damage_type_dict[i] = 0
                for i in type_2_super_effective:
                    cur_damage_type_dict[i] = 2 * cur_damage_type_dict[i]
                for i in type_2_not_very_effective:
                    cur_damage_type_dict[i] = 0.5 * cur_damage_type_dict[i]
            pokemon['defense_type_dict'] = cur_damage_type_dict
            
            if self.debug:
                for pokemon in self.team:
                    print(pokemon['name'])
                    print(pokemon['defense_type_dict'])
                    print('')
                
    def very_defense_analysis(self):
        double_resistance = deepcopy(self.damage_dict)
        quadruple_resistance = deepcopy(self.damage_dict)
        for pokemon in self.team:
            for type in pokemon['defense_type_dict'].keys():
                if pokemon['defense_type_dict'][type] == 0.5:
                    double_resistance[type] += 1
                if pokemon['defense_type_dict'][type] == 0 or pokemon['defense_type_dict'][type] == 0.25:
                    quadruple_resistance[type] += 1
        print(double_resistance)
        print(quadruple_resistance)
        for type in double_resistance.keys():
            if double_resistance[type] >= 3:
                print('Double resistance: ' + type)
        for type in quadruple_resistance.keys():
            if quadruple_resistance[type] >= 2:
                print('Quadruple resistance: ' + type)

    def move_analyze(self):
        for pokemon in self.team:
            moves_name = ['move_1', 'move_2', 'move_3', 'move_4']
            cur_damage_point_dict = deepcopy(self.defense_type_dict)
            for move in moves_name:
                move_name = pokemon[move]['name']
                move_type = pokemon[move]['type']
                move_power = pokemon[move]['power']
            
                move_type_no_effect = self.type_dict[move_type]['no_effect']
                move_type_super_effective = self.type_dict[move_type]['super_effective']
                move_type_very_effective = self.type_dict[move_type]['not_very_effective']
                for i in move_type_super_effective:
                    cur_damage_point_dict[i] = 2 * move_power
                for i in move_type_very_effective:
                    cur_damage_point_dict[i] = 0.5 * move_power
