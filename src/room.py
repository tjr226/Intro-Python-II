# Implement a class to hold room information. This should have name and
# description attributes.

import textwrap

class Room:
    def __init__(self, room_name, room_description, room_items=[], n_to=None, s_to=None, e_to=None, w_to=None):
        self.room_name = room_name
        self.room_description = textwrap.fill(room_description, 200)
        self.room_items = room_items
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to

    # represents player getting an item
    def item_get(self, item):
        if item in self.room_items:
            self.room_items.remove(item)
            return True
            # no notification here. Player is told item was added to inventory in Player Class
        else:
            print(f"{item} not in this room.")
            return False


    def __str__(self):
        s = "*****\n\n"
        s += f"Current room: {self.room_name}\n\n{self.room_description}\n\n"
        
        s += f"Action options: (i)nventory, (get ITEM), (drop ITEM)\n\n"
        s += f"Room items: "
        # printing items has same code structure in room.py and adventure_funcs.py
        room_items = []
        for item in self.room_items:
            room_items.append(item.name)
        s += f"{room_items} \n\n"
        s += f"Movement options: \n\n"
        if self.n_to:
            s += f"(N)orth: {self.n_to.room_name}\n"
        if self.s_to:
            s += f"(S)outh: {self.s_to.room_name}\n"
        if self.e_to:
            s += f"(E)ast: {self.e_to.room_name}\n"
        if self.w_to:    
            s += f"(W)est: {self.w_to.room_name}\n"
        return s
