import pandas as pd
import numpy as np
from IPython.display import display, HTML
import requests
from bs4 import BeautifulSoup 
import pandas as pd
import re

def request_url (url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def labels (soup):
    dict_recipes = {}
    for i in soup.find_all('h2'):
        key = i.get_text().strip()
        value = ""
        next_node = i.next_sibling
        while next_node and next_node.name != 'h2':
            if next_node.name is not None:
                value += next_node.get_text().strip() + " "
            next_node = next_node.next_sibling
        dict_recipes[key] = value.strip()
    return dict_recipes

def scrapping1(dict_recipes):
    new_dict = {}
    for key, value in dict_recipes.items(): 
        ingredients_index = value.find("Ingredientes")
        if ingredients_index != -1:
            elaboration_index = value.find("Elaboración")
        if elaboration_index != -1:
            value = value[ingredients_index:elaboration_index]
        else:
            value = value[ingredients_index:]
    else:
        value = dict_recipes[key]
    new_dict[key] = value

def scrapping2():
    for key, value in dict_recipes.items():
        ingredients_index = value.find("Ingredientes")
        if ingredients_index != -1:
            dict_recipes[key] = value[ingredients_index:]
        else:
            dict_recipes[key] = ""
        elaboracion_index = dict_recipes[key].find("Elaboración")
        if elaboracion_index != -1:
            dict_recipes[key] = dict_recipes[key][:elaboracion_index]
    return dict_recipes

def scrapping3():
    remove_recipes=['6. Birria tacos','7. Salsa rosa','8. Rollos de canela','9. Tablas de nachos','10. Tablas de mantequilla']
    [dict_recipes.pop(x,None) for x in remove_recipes]
    return dict_recipes

def scrapping4():
    desired_words = ['huevos', 'queso', 'bicarbonato', 'avena', 'canela', 'plátano', 'chía', 'sal', 'nueces', 'arándanos', 'naranja', 'pasta', 'queso parmesano', 'pimienta', 'ajo', 'chile', 'orégano', 'aceite', 'chocolate', 'mantequilla', 'azúcar', 'harina', 'levadura', 'canela', 'agua', 'vainilla']
    new_dict = {}
    for key, value in dict_recipes.items():
        words = []
        for word in value.split():
            word = word.strip().strip(',.')
            if word.lower() in desired_words:
                words.append(word)
        new_dict[key] = ' '.join(words)
    return new_dict

def scrapping5():
    for key, value in new_dict.items():
        words = value.upper().split()
        words = ", ".join([word.upper() for word in words])
        new_dict[key] = words
    return new_dict

