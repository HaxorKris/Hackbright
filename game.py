import core
import pyglet
from pyglet.window import key
from core import GameElement
import sys

#### DO NOT TOUCH ####
GAME_BOARD = None
DEBUG = False
KEYBOARD = None
PLAYER = None
######################

GAME_WIDTH = 8
GAME_HEIGHT = 8

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Character(GameElement):
    IMAGE = "Princess"

    def next_pos(self, direction):
        if direction == "up":
            return (self.x, self.y-1)
        elif direction == "down":
            return (self.x, self.y+1)
        elif direction == "left":
#            GAME_BOARD.draw_msg("suck it, monkeys")
            return (self.x-1, self.y)
        elif direction == "right":
            return (self.x+1, self.y)

    def __init__(self):
        GameElement.__init__(self)
        self.inventory = []

class InventoryOracle(GameElement):
    IMAGE = "Cat"
    SOLID = True
    def interact(self, player):
        # iterate out of a list
        printable_list = []
        for item in player.inventory:
            printable_list.append(item.IMAGE)
        str = ","
        your_inventory = str.join(printable_list)
        
        GAME_BOARD.draw_msg("Hello! You have the following in your inventory: %s" % your_inventory)
        
       # print(player.inventory)


class Gem(GameElement):
    IMAGE = "BlueGem"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("Whooop dee fucking doo, monkey!")

class Chest(GameElement):
    IMAGE = "Chest"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("I'm rich, bitches!")

class DoorOpen(GameElement):
    IMAGE = "DoorOpen"
    SOLID = False

class ClosedDoor(GameElement):
    IMAGE = "DoorClosed"
    SOLID = True
    def interact(self, player):
        printable_list = []
        for item in player.inventory:
            printable_list.append(item.IMAGE)
        str = ","
        your_inventory = str.join(printable_list)

        
        if "Key" in your_inventory:
            GAME_BOARD.del_el(3, 3)
            GAME_BOARD.register(DoorOpen)
            GAME_BOARD.set_el(3, 3, DoorOpen)
            GAME_BOARD.draw_msg("Open Sesame")

            #IMAGE = "DoorOpen"
            #SOLID = False
        else:
            GAME_BOARD.draw_msg("The door is locked, sucker. Do you have a key?")
        
class Key(GameElement):
    IMAGE = "Key"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("Hooray! A key! You will need this.")


####   End class definitions    ####

def initialize():
#Put game initialization code here"""

    rock_positions = [
        (1, 1),
        (2, 1),
        (3, 1),
        (4, 1),
        (1, 2),
        (4, 2),
        (1, 3),
        (2, 3),
        (4, 3)
    ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    rocks[-1].SOLID = False
    for rock in rocks:
        print rock

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(5, 5, PLAYER)
    print PLAYER
   
    GAME_BOARD.draw_msg("This game needs shanking.")

    gem = Gem()
    GAME_BOARD.register(gem)
    GAME_BOARD.set_el(5, 1, gem)

    chest = Chest()
    GAME_BOARD.register(chest)
    GAME_BOARD.set_el(2, 2, chest)

    closed_door = ClosedDoor()
    GAME_BOARD.register(closed_door)
    GAME_BOARD.set_el(3, 3, closed_door)

    key = Key()
    GAME_BOARD.register(key)
    GAME_BOARD.set_el(6, 6, key)

    oracle_cat = InventoryOracle()
    GAME_BOARD.register(oracle_cat)
    GAME_BOARD.set_el(0, 7, oracle_cat)

    doorOpen = DoorOpen()
    GAME_BOARD.register(doorOpen)



def keyboard_handler():
    direction = None

    if KEYBOARD[key.UP]:
        GAME_BOARD.draw_msg("You pressed up")
        direction = "up"
    elif KEYBOARD[key.DOWN]:
        GAME_BOARD.draw_msg("WE'RE GONNA DIIIIIIE")
        direction = "down"
    elif KEYBOARD[key.RIGHT]:
        GAME_BOARD.draw_msg("damn right i'm right")
        direction = "right"
    elif KEYBOARD[key.LEFT]:
        GAME_BOARD.draw_msg("suck it, monkeys")
        direction = "left"
    elif KEYBOARD[key.SPACE]:
        GAME_BOARD.erase_msg()

    if direction:
        next_location = PLAYER.next_pos(direction)
        next_x = next_location[0]
        next_y = next_location[1]

        existing_el = GAME_BOARD.get_el(next_x, next_y)

        if existing_el:
            existing_el.interact(PLAYER)

        if existing_el is None or not existing_el.SOLID:
            GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
            GAME_BOARD.set_el(next_x, next_y, PLAYER)

#   print "The rist rock is at", (rock1.x, rock1.y)
#   print "The second rock is at", (rock2.x, rock2.y)
#   print "The third rock has gone all rebel and is now at", (rock3.x, rock3.y)
#   print "Rock 1 image", rock1.IMAGE
#   print "Rock 2 image", rock2.IMAGE
#   print "Rock 3 image", rock3.IMAGE
