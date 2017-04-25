import pygame as p
import constants
from block import Block

class Room():
    def __init__(self):
        self.id = None
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.block_list = p.sprite.Group()
        self.enemy_list = p.sprite.Group()
        self.background = None

class Room0(Room):
    def __init__(self):
        super().__init__()
        self.id = 0
        self.left = None
        self.right = 1
        self.up = None
        self.down = None

        i = 0
        while i <= constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i,0)))
            self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            self.block_list.add(Block(pos = (0, i+64)))
            i += 64

class Room1(Room):
    def __init__(self):
        super().__init__()
        self.id = 1
        self.left = 0
        self.right = 2
        self.up = None
        self.down = None

        i = 0
        while i <= constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i,0)))
            self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            i += 64

class Room2(Room):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.left = 1
        self.right = 3
        self.up = None
        self.down = None

        i = 0
        while i < constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i,0)))
            self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            #self.block_list.add(Block(pos = (constants.SCREEN_WIDTH-64, i+64)))
            i += 64

class Room3(Room):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.left = 2
        self.right = None
        self.up = None
        self.down = None

        i = 0
        while i < constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i,0)))
            #self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            self.block_list.add(Block(pos = (constants.SCREEN_WIDTH-64, i+64)))
            if i <= 172:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            i += 64

class Room4(Room):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.left = None
        self.right = None
        self.up = 3
        self.down = None

        i = 0
        while i < constants.SCREEN_WIDTH:
            #self.block_list.add(Block(pos = (i,0)))
            #self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            self.block_list.add(Block(pos = (constants.SCREEN_WIDTH-64, i+64)))
