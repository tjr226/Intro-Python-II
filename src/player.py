# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, room=None, inventory=[]):
        self.room = room
        self.inventory = inventory

    def drop_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return True
        else:
            print(f"{item} is not in your inventory.")
            return False



    