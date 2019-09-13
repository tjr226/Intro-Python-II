def wrongDir():
    print("\nYou can't go that way, please pick another direction.\n")

def showRoom(player_room):
    print(player_room)

def showInventory(inventory):
    # printing items has same code structure in room.py and adventure_funcs.py
    item_list = []
    for item in inventory:
        item_list.append(item.name)
    print(f"Your items: {inventory}")

def quitGame():
    print("You have quit the game.")

def getMovement():
    return input("What direction will you move in next?").strip()

