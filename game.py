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
ENEMY = None
######################

GAME_WIDTH = 12
GAME_HEIGHT = 9

#### Put class definitions here ####
class Rock(GameElement):
    IMAGE = "Rock"
    SOLID = True

class Wall(GameElement):
    IMAGE = "TallWall"
    SOLID = True

class Water(GameElement):
    IMAGE = "Water"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You've found some lovely water")

class Character(GameElement):
    IMAGE = "Clown"

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

class Carmen(GameElement):
    IMAGE = "Carmen"
    SOLID = True

    def move(self, player):
        print "player is at: ", player.x, player.y
        print "I'm at ", self.x, self.y
#   if player.x > self.x
#   if player.x < self.x
#   if player.x == self.x

#def keyboard_handler():
#    if KEYBOARD[key.UP]:
#        GAME_BOARD.draw_msg("You pressed up")
#        next_y = PLAYER.y - 1
#        GAME_BOARD.del_el(PLAYER.x, PLAYER.y)
#        GAME_BOARD.set_el(PLAYER.x, next_y, PLAYER)



class Merchant(GameElement):
    IMAGE = "Boy"
    SOLID = True
    def interact(self, player):
        printable_list = []
        for item in player.inventory:
            printable_list.append(item.IMAGE)
        str = ","
        your_inventory = str.join(printable_list)
        if "GreenGem" in your_inventory:
            GAME_BOARD.draw_msg("You have my shiny! Here are some magic spores.")
            spores = Spores()
            GAME_BOARD.register(spores)
            GAME_BOARD.set_el(3, 6, spores)
            player.inventory.append(spores)
        # some way to add fertilizer to inventory
        else:
            GAME_BOARD.draw_msg("Where is my shiny? I need my shiny!")

#        GAME_BOARD.draw_msg("Whooop dee fucking doo, monkey!")

class GreenGem(GameElement):
    IMAGE = "GreenGem"
    SOLID = False
    def interact(self, player):
        player.inventory.append(self)
        GAME_BOARD.draw_msg("You found a green gem. This looks valuable.")

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
            door_open = DoorOpen()
            GAME_BOARD.del_el(2, 6)
            GAME_BOARD.register(door_open)
            GAME_BOARD.set_el(2, 6, door_open)
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

class UglyTree(GameElement):
    IMAGE = "UglyTree"
    SOLID = True

class Spores(GameElement):
    IMAGE = "Spores"
    SOLID = False

class ForestLord(GameElement):
    IMAGE = "ForestLord"
    SOLID = True

# class Clown(GameElement):
#     IMAGE = "Clown"
#     SOLID = True

####   End class definitions    ####

def initialize():
#Put game initialization code here"""

    rock_positions = [ 
        (0, 0),
        (1, 0),
        (2, 0), 
        (3, 0),
        (8, 0), 
        (9, 0),
        (10, 0), 
        (11, 0),
        (0, 1), 
        (0, 2),
        (0, 3),
        (0, 4),
        (0, 5),
        (0, 6),
        (0, 7),
        (0, 8), 
        (1, 8),
        (2, 8), 
        (3, 8),
        (4, 8),
        (5, 8),
        (6, 8),
        (7, 8),
        (8, 8),
        (9, 8),
        (10, 8),
        (11, 8),
        (11, 1),
        (11, 2),
        (11, 3),
        (11, 4),
        (11, 5),
        (11, 6),
        (11, 7),
        (1, 5),
        (2, 5),
        (2, 7)
        
    ]

    rocks = []
    for pos in rock_positions:
        rock = Rock()
        GAME_BOARD.register(rock)
        GAME_BOARD.set_el(pos[0], pos[1], rock)
        rocks.append(rock)

    # rocks[-1].SOLID = False
    # for rock in rocks:
    #     print rock

    global PLAYER
    PLAYER = Character()
    GAME_BOARD.register(PLAYER)
    GAME_BOARD.set_el(5, 5, PLAYER)
    print PLAYER
   
    GAME_BOARD.draw_msg("This game needs shanking.")

    green_gem = GreenGem()
    GAME_BOARD.register(green_gem)
    GAME_BOARD.set_el(7, 7, green_gem)

    chest = Chest()
    GAME_BOARD.register(chest)
    GAME_BOARD.set_el(10, 7, chest)

    closed_door = ClosedDoor()
    GAME_BOARD.register(closed_door)
    GAME_BOARD.set_el(2, 6, closed_door)

    key = Key()
    GAME_BOARD.register(key)
    GAME_BOARD.set_el(6, 6, key)

    oracle_cat = InventoryOracle()
    GAME_BOARD.register(oracle_cat)
    GAME_BOARD.set_el(10, 1, oracle_cat)

    merchant = Merchant()
    GAME_BOARD.register(merchant)
    GAME_BOARD.set_el(1, 6, merchant)

    # wall1 = Wall()
    # GAME_BOARD.register(wall1)
    # GAME_BOARD.set_el(1, 5, wall1)

    # wall2 = Wall()
    # GAME_BOARD.register(wall2)
    # GAME_BOARD.set_el(2, 5, wall2)

    # wall3 = Wall()
    # GAME_BOARD.register(wall3)
    # GAME_BOARD.set_el(2, 7, wall3)

    ugly_tree1 = UglyTree()
    GAME_BOARD.register(ugly_tree1)
    GAME_BOARD.set_el(4, 0, ugly_tree1)

    ugly_tree2 = UglyTree()
    GAME_BOARD.register(ugly_tree2)
    GAME_BOARD.set_el(5, 0, ugly_tree2)

    # ugly_tree3 = UglyTree()
    # GAME_BOARD.register(ugly_tree3)
    # GAME_BOARD.set_el(6, 0, ugly_tree3)

    ugly_tree4 = UglyTree()
    GAME_BOARD.register(ugly_tree4)
    GAME_BOARD.set_el(7, 0, ugly_tree4)

    ugly_tree5 = UglyTree()
    GAME_BOARD.register(ugly_tree5)
    GAME_BOARD.set_el(4, 1, ugly_tree5)

    ugly_tree6 = UglyTree()
    GAME_BOARD.register(ugly_tree6)
    GAME_BOARD.set_el(4, 2, ugly_tree6)

    ugly_tree7 = UglyTree()
    GAME_BOARD.register(ugly_tree7)
    GAME_BOARD.set_el(7, 1, ugly_tree7)

    ugly_tree8 = UglyTree()
    GAME_BOARD.register(ugly_tree8)
    GAME_BOARD.set_el(7, 2, ugly_tree8)

    water = Water()
    GAME_BOARD.register(water)
    GAME_BOARD.set_el(1, 1, water)


    # clown = Clown()
    # GAME_BOARD.register(clown)
    # GAME_BOARD.set_el(2, 2, clown)

    global ENEMY
    carmen = Carmen()
    GAME_BOARD.register(carmen)
    GAME_BOARD.set_el(6, 7, carmen)
    ENEMY = carmen

    forest_lord = ForestLord()
    GAME_BOARD.register(forest_lord)
    GAME_BOARD.set_el(6, 0, forest_lord)


#    GAME_BOARD.register(door_open)



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

        ENEMY.move(PLAYER)

#   print "The rist rock is at", (rock1.x, rock1.y)
#   print "The second rock is at", (rock2.x, rock2.y)
#   print "The third rock has gone all rebel and is now at", (rock3.x, rock3.y)
#   print "Rock 1 image", rock1.IMAGE
#   print "Rock 2 image", rock2.IMAGE
#   print "Rock 3 image", rock3.IMAGE
