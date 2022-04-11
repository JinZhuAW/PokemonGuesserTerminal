import sys
import os
import requests
from random import randint
import urllib.request

api_url = "https://pokeapi.co/api/v2/pokemon/"

def get_api_responds(index):
    search = api_url + str(index)
    response = requests.get(search)
    return response

def get_pokemon_name(response):
    name = response.json()["name"]
    return name

def get_pokemon_sprite_url(response,answer):
    if answer == True:
        url = response.json()["sprites"]["other"]["official-artwork"]["front_default"]
    else:
        url = response.json()["sprites"]["front_default"]
    return url


def save_sprite(url):
    filename = url.split('/')[-1]
    urllib.request.urlretrieve(url, filename)
    return filename

def show_image(response,answer):
    url = get_pokemon_sprite_url(response,answer)
    filename = save_sprite(url)
    os.system(f"tiv ./{filename}")
    return filename

def delete_image(filename):
    os.system(f"rm {filename}")

if __name__ == "__main__":
    GAME_MENU = True
    while GAME_MENU:
        print("======Welcome to Pokeman Guessing Game=====")
        r_num = randint(1,151)
        response = get_api_responds(r_num)
        name = get_pokemon_name(response)
        filename = show_image(response,False)
        user_input = input("Please guess the name of the pokemon: ")
        while name != user_input.lower():
            user_input = input("Wrong Answer! Please try again or type a to get the answer: ")
            if user_input != "a":
                continue
            else:
                show_image(response,True)
                print("The Answer is " + name)
                print("\n")
                break
        if name == user_input.lower():
            show_image(response,True)
            print("Well done! You are a Pokemon Expert!")
            print("\n")
        user_input2 = input("Press Enter to continue or q to quit:")
        if user_input2 == "q":
            delete_image(filename)
            sys.exit()
        else:
            delete_image(filename)
            print("\n")

            