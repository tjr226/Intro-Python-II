from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    ["Chair", "Table", "Brazier"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    ["Flag"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    ["Coin"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    ["Empty box"]),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main
#

# Make a new player object that is currently in the 'outside' room.

def wrongDir():
    print("\nYou can't go that way, please pick another direction.\n")

def showRoom():
    print(newPlayer.room)

def quitGame():
    print("You have quit the game.")

def getMovement():
    return input("What direction will you move in next?")
    
newPlayer = Player(room['outside'])

# print room at start, then print again whenever you get to a new room
showRoom()

while True:

    playerMovement = getMovement()

    if playerMovement == "q":
        quitGame()
        break
    # north
    elif playerMovement == "n":
        if newPlayer.room.n_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.n_to
            showRoom()
    # south
    elif playerMovement == "s":
        if newPlayer.room.s_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.s_to
            showRoom()
    # east
    elif playerMovement == "e":
        if newPlayer.room.e_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.e_to
            showRoom()
    # west
    elif playerMovement == "w":
        if newPlayer.room.w_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.w_to
            showRoom()
    # catching incorrect inputs
    else:
        print("\nNot a valid input. Please input n, s, e, w, or q.\n")
        





# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
