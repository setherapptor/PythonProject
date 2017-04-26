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
        self.background = None

#Complete
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

#Complete
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
            if i >= 320 and i <= 448:
                self.block_list.add(Block(pos = (704, i)))
            i += 64
        self.block_list.add(Block(pos = (320, 384)))
        self.block_list.add(Block(pos = (512, 256)))

#Complete
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
            if i <= 192 or i >= 512:
                self.block_list.add(Block(pos = (i,0)))
            if i >= 320 and i <= 448:
                self.block_list.add(Block(pos = (0, i)))
                self.block_list.add(Block(pos = (constants.SCREEN_WIDTH-64, i)))
            if i <= 256 or i >= 448:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            i += 64
        self.block_list.add(Block(pos = (640,192), moving = (2,640,256,0,0,0)))
        self.block_list.add(Block(pos = (64,384)))


class Room3(Room):
    def __init__(self):
        super().__init__()
        self.id = 3
        self.left = 2
        self.right = None
        self.up = None
        self.down = 4

        i = 0
        while i < constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i,0)))
            self.block_list.add(Block(pos = (constants.SCREEN_WIDTH-64, i+64)))
            if i <= 448:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            if i >= 320:
                self.block_list.add(Block(pos = (0,i)))
            i += 64
        self.block_list.add(Block(pos = (64,384)))

class Room4(Room):
    def __init__(self):
        super().__init__()
        self.id = 4
        self.left = None
        self.right = None
        self.up = 3
        self.down = 5

        i = 0
        while i < constants.SCREEN_WIDTH:
            if i <= 384:
                self.block_list.add(Block(pos = (i,0)))
            #self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            self.block_list.add(Block(pos = (448, i)))
            if i > 128:
                self.block_list.add(Block(pos = (320,i)))
            if i != 384:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            i += 64
        self.block_list.add(Block(pos = (512,384), moving = (2,704,512,0,0,0)))
        self.block_list.add(Block(pos = (0,256), moving = (4,192,0,0,0,0)))

class Room5(Room):
    def __init__(self):
        super().__init__()
        self.id = 5
        self.left = None
        self.right = None
        self.up = 4
        self.down = None

        i = 0
        while i < constants.SCREEN_WIDTH:
            if i != 384:
                self.block_list.add(Block(pos = (i, 0)))
            self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            if i >= 64 and i <= 640:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-128)))
            if i >= 128 and i <= 576:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-192)))
            i += 64

class Room6(Room):
    def __init__(self):
        super().__init__()
        self.id = 6
        self.left = 5
        self.right = None
        self.up = None
        self.down = None
