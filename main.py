#!/usr/bin/env python3
import sys, os, json
# Check to make sure we are running the correct version of Python
assert sys.version_info >= (3,7), "This script requires at least Python 3.7"

# The game and item description files (in the same folder as this script)
game_file = 'game.json'
item_file = 'item.json'
inventory: ""
moves = 0

# Load the contents of the files into the game and items dictionaries. You can largely ignore this
# Sorry it's messy, I'm trying to account for any potential craziness with the file location
def load_files():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
        with open(os.path.join(__location__, game_file)) as json_file: game = json.load(json_file)
        with open(os.path.join(__location__, item_file)) as json_file: items = json.load(json_file)
        return (game,items)
    except:
        print("There was a problem reading either the game or item file.")
        os._exit(1)


def render(game,items,current,moves):
    c = game[current]
    
    print("\n\n{} Moves".format(moves))
    print("\n\nYou are at the " + c["name"])
    print(c["desc"])

    print("\nAvailable exits: ")
    for e in c["exits"]:
        print(e["exit"].lower())

def get_input():
    response = input("\nWhat do you want to do? ")
    response = response.upper().strip()
    return response



def update(game,items,current,response):

    if response == "INVENTORY":
        print("You are carrying:")
        if len(inventory) == 0:
            print("Nothing")
        else:
            for i in inventory:
                print(i.lower())
        return current

    c = game[current]
    for e in c["exits"]:
        if response == e["exit"]:
            return e["target"]

    for item in c["items"]:
        if response == "GET " or "TAKE " or "PICK UP " + items["items"]:
            print(item["take"])
            return current
    

    if response[0:3] == "GET" or "TAKE" or "PICK UP":
        print("You can't take that.")
    elif response in ["NOTH","SOUTH","EAST","WEST","NW","NE","SE","SW","UP","DOWN"]:
        print("You can't go that way.")
    else: 
        print("I don't understand what you are trying to do.")

    return current
    



# The main function for the game
def main():
    current = 'START'  # The starting location
    end_game = ['CLOUDS']  # Any of the end-game locations
    moves = 0

    (game,items) = load_files()

    while True:
        render(game,items,current,moves)
        if current in end_game:
            break

        response = get_input()

        if response == "QUIT" or response == "Q":
            break #break out of the while loop

        current = update(game,items,current,response)
        moves += 1

    print("I hope you enjoyed playing! See you next time.")
    print("You completed the game in {} moves.".format(moves))

# run the main function
if __name__ == '__main__':
    main()