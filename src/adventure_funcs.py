def wrongDir():
    print("\nYou can't go that way, please pick another direction.\n")

def showRoom(player_room):
    print(player_room)

def showInventory(inventory):
    print(f"Your items: {inventory}")

def quitGame():
    print("You have quit the game.")

def getMovement():
    return input("What direction will you move in next?").strip()

