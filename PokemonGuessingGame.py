import imp
import sys
import os
import pokebase as pb
from random import randint
# pikatro = pb.SpriteResource('pokemon', 20, other= True, official_artwort=True)
# print(pikatro.path)

if __name__ == "__main__":
        GAME_MENU = True
        while GAME_MENU:
            print("======Welcome to Pokeman Guessing Game=====")
            r_num = randint(1,898)
            rdm_pkm_sprt = pb.SpriteResource('pokemon' ,r_num,other=True, official_artwork=True)
            rdm_pkm_resource = pb.APIResource('pokemon',r_num)
            os.system(f"tiv {rdm_pkm_sprt.path}")
            user_input = input("Please guess the name of the pokemon: ")
            while rdm_pkm_resource.name != user_input.lower():
                user_input = input("Wrong Answer! Please try again or type a to get the answer: ")
                if user_input != "a":
                    continue
                else:
                    print("The Answer is " + rdm_pkm_resource.name)
                    break
            if rdm_pkm_resource == user_input:
                print("Well done! You are a Pokemon Expert!")
            else:
                user_input2 = input("Press Enter to continue or q to quit:")
                if user_input2 == "q":
                    sys.exit()
                else:
                    print("\n")

            