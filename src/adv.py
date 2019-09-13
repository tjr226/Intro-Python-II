from room import Room
from player import Player
from item import Item
from adventure_funcs import *

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [Item("Sword"), Item("Bow")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    [Item("Flag")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    [Item("Coin")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    [Item("Empty box")]),
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

showRoom(newPlayer.current_room)

while True:

    playerMovement = getMovement()

    if playerMovement == "q":
        quitGame()
        break
    elif len(playerMovement) > 1:
        input_list = playerMovement.split(" ", 1)
        input_item_action = input_list[0]
        input_item_name = input_list[1]
        matching_item = None
        # Success messages in the next if/elif block
        # Failure messages in the Room and Player classes
        if input_item_action == "get":
            for item in newPlayer.current_room.room_items:
                if input_item_name == item.name:
                    matching_item = item

            if matching_item is not None:    
                newPlayer.inventory.append(matching_item)
                newPlayer.current_room.room_items.remove(matching_item)
                matching_item.on_take()
            else:
                print("That item is not in the room.")
            # extra code from when Inventory was a list of strings
            # if newPlayer.current_room.item_get(item_name) is True:
            #     newPlayer.inventory.append(item_name)
            #     print(f"{item_name} was added to your inventory.")
        elif input_item_action == "drop":
            for item in newPlayer.inventory:
                if input_item_name == item.name:
                    matching_item = item

            if matching_item is not None:
                newPlayer.inventory.remove(matching_item)
                newPlayer.current_room.room_items.append(matching_item)
                matching_item.on_drop()
            else:
                print("That item is not in your inventory.")
            # extra code from when Inventory was a list of strings
            # if newPlayer.drop_item(item_name) is True:
            #     newPlayer.current_room.room_items.append(item_name)
            #     print(f"{item_name} was dropped.")
        else:
            print("Instructions could not be processed.")
    # check items
    elif playerMovement == "i":
        player_items = []
        for item in newPlayer.inventory:
            player_items.append(item.name)
        print(f"Your inventory: {player_items}")
        # north
    elif playerMovement == "n":
        if newPlayer.current_room.n_to == None:
            wrongDir()
        else:
            newPlayer.current_room = newPlayer.current_room.n_to
            showRoom(newPlayer.current_room)
    # south
    elif playerMovement == "s":
        if newPlayer.current_room.s_to == None:
            wrongDir()
        else:
            newPlayer.current_room = newPlayer.current_room.s_to
            showRoom(newPlayer.current_room)
    # east
    elif playerMovement == "e":
        if newPlayer.current_room.e_to == None:
            wrongDir()
        else:
            newPlayer.current_room = newPlayer.current_room.e_to
            showRoom(newPlayer.current_room)
    # west
    elif playerMovement == "w":
        if newPlayer.current_room.w_to == None:
            wrongDir()
        else:
            newPlayer.current_room = newPlayer.current_room.w_to
            showRoom(newPlayer.current_room)
    # catching incorrect inputs
    else:
        print("\nNot a valid input. Please input n, s, e, w, or q.\n")
