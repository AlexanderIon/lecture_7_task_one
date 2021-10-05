from pprint import pprint
import requests


class Superhero:

    def __init__(self, token):
        self.token = token
        self.url = 'https://superheroapi.com/api/' + token



    def get_id_character_by_name(self, name):
        name = name
        url = self.url+"/search/" + name
        response = requests.get(url=url, timeout=5)
        res = (response.json())
        list_res = res['results']
        return list_res[0]['id']


    def get_powerstats_character(self, id):
       id = id
       url = self.url + "/" + id + '/powerstats'
       response = requests.get(url=url, timeout=5)
       res = (response.json())
       return res


def list_parametrs_my_characters(list_of_heroes, param=all):
    list_parametrs = []
    for character in range(len(list_characters)):
        character = list_characters[character]
        list_powerstats = my.get_powerstats_character(my.get_id_character_by_name(character))
        if param == all:
            paramerts = list_powerstats
            list_hero = [character, paramerts]
            list_parametrs.append(list_hero)
        else:
            paramerts =list_powerstats[param]
            list_hero = [character, int(paramerts)]
            list_parametrs.append(list_hero)
    return list_parametrs


TOKEN = '2619421814940190'
my = Superhero(TOKEN)
list_characters = ['Hulk', 'Captain America', 'Thanos']
list_my_heroes_and_ability = list_parametrs_my_characters(list_characters, param='intelligence')
list_my_heroes_and_ability.sort(key=lambda i: i[1])
list_my_heroes_and_ability.reverse()
pprint(list_my_heroes_and_ability)














