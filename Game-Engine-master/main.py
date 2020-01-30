#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'


# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        return game
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,current):
    c = game[current]
    print("You are at the " + c["name"])
    print(c["desc"])

def get_input():
    response = input("What do you want to do? ")
    response = response.upper().strip()
    return response

def update(game,current,response):
    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]
    return current
    

# The main function for the game
def main():
    current = 'START'  # The starting location
    end_game = ['END']  # Any of the end-game locations

    game = load_files()

    while True:
        render(game,current)

        for e in end_game:
            if current == e:
                print("You win!")
                break #break out of the while loop

        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,current,response)

    print("Thanks for playing!")

# run the main function
if __name__ == '__main__':
	main()