from room import Room
from player import Player
from adventure_funcs import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    ["Sword", "Bow"]),

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

# Make a new player object that is currently in the 'outside' room.
    
newPlayer = Player(room['outside'])

# print room at start, then print again whenever you get to a new room

showRoom(newPlayer.room)

while True:

    playerMovement = getMovement()

    if playerMovement == "q":
        quitGame()
        break
    elif len(playerMovement) > 1:
        input_list = playerMovement.split(" ", 1)
        item_action = input_list[0]
        item_name = input_list[1]
        # Success messages in the next if/elif block
        # Failure messages in the Room and Player classes
        if item_action == "Get":
            if newPlayer.room.item_get(item_name) is True:
                newPlayer.inventory.append(item_name)
                print(f"{item_name} was added to your inventory.")
        elif item_action == "Drop":
            if newPlayer.drop_item(item_name) is True:
                newPlayer.room.room_items.append(item_name)
                print(f"{item_name} was dropped.")
    # check items
    elif playerMovement == "c":
        showInventory(newPlayer.inventory)
    # north
    elif playerMovement == "n":
        if newPlayer.room.n_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.n_to
            showRoom(newPlayer.room)
    # south
    elif playerMovement == "s":
        if newPlayer.room.s_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.s_to
            showRoom(newPlayer.room)
    # east
    elif playerMovement == "e":
        if newPlayer.room.e_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.e_to
            showRoom(newPlayer.room)
    # west
    elif playerMovement == "w":
        if newPlayer.room.w_to == None:
            wrongDir()
        else:
            newPlayer.room = newPlayer.room.w_to
            showRoom(newPlayer.room)
    # catching incorrect inputs
    else:
        print("\nNot a valid input. Please input n, s, e, w, or q.\n")
