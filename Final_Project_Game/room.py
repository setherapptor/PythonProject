#room.py
#Contains classes of every room in the room, as well as the parent class

import pygame as p
import constants
from block import Block

#Parent room class with basic data
class Room():
    def __init__(self):
        #Integer value of room
        self.id = None
        #References to adjacent rooms
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        #Initialize group of blocks
        self.block_list = p.sprite.Group()
        #Initialize default background
        self.background = p.image.load("Images\\default_background.png")

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
            if i >= 320 and i <= 448:
                self.block_list.add(Block(pos = (704, i)))
            i += 64
        self.block_list.add(Block(pos = (320, 384)))
        self.block_list.add(Block(pos = (512, 256)))

class Room2(Room):
    def __init__(self):
        super().__init__()
        self.id = 2
        self.left = 1
        self.right = 3
        self.up = 6
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
        self.block_list.add(Block(pos = (640,128), moving = (2,640,256,0,0,0)))
        self.block_list.add(Block(pos = (64,384)))
        self.block_list.add(Block(pos = (64, 448)))

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
        self.block_list.add(Block(pos = (64, 448)))

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
        self.left = 10
        self.right = 7
        self.up = 4
        self.down = None

        self.background = p.image.load("Images\\fork.png")

        i = 0
        while i < constants.SCREEN_WIDTH:
            if i != 384:
                self.block_list.add(Block(pos = (i, 0)))

            if i != 384 and i != 448:
                self.block_list.add(Block(pos = (0, i)))
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
        self.left = None
        self.right = None
        self.up = None
        self.down = 2

        self.background = p.image.load("Images\\secret_background.png")
        i = 0
        while i < constants.SCREEN_WIDTH:
            if i != 320 and i != 384:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            i += 64
        self.block_list.add(Block(pos = (320,constants.SCREEN_HEIGHT+64), moving = (0,0,0,2,576,320)))
        self.block_list.add(Block(pos = (384,constants.SCREEN_HEIGHT+64), moving = (0,0,0,2,576,320)))

class Room7(Room):
    def __init__(self):
        super().__init__()
        self.id = 7
        self.left = 5
        self.right = None
        self.up = 8
        self.down = None

        i = 0
        while i <= constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            if i != 64:
                self.block_list.add(Block(pos = (i, 0)))
            i += 64
        self.block_list.add(Block(pos = (384,448), moving = (0,0,0,1,448,256)))
        self.block_list.add(Block(pos = (256,192), moving = (2,320,128,0,0,0)))
        self.block_list.add(Block(pos = (64,256), moving = (0,0,0,2,256,0)))

class Room8(Room):
    def __init__(self):
        super().__init__()
        self.id = 8
        self.left = None
        self.right = None
        self.up = 9
        self.down = 7

        i = 0
        while i <= constants.SCREEN_WIDTH:
            self.block_list.add(Block(pos = (0, i)))
            if i != 64:
                self.block_list.add(Block(pos = (i, constants.SCREEN_HEIGHT-64)))
            if i >= 192:
                self.block_list.add(Block(pos = (i, 448)))
            if i >= 256:
                self.block_list.add(Block(pos = (i, 384)))
            if i >= 320:
                self.block_list.add(Block(pos = (i, 320)))
            if i >= 384:
                self.block_list.add(Block(pos = (i, 256)))
            if i >= 448:
                self.block_list.add(Block(pos = (i, 192)))
            if i >= 512:
                self.block_list.add(Block(pos = (i, 128)))
            if i >= 576:
                self.block_list.add(Block(pos = (i, 64)))
            i += 64
            self.block_list.add(Block(pos = (640, 0)))
            self.block_list.add(Block(pos = (704, 0)))

#Complete
class Room9(Room):
    def __init__(self):
        super().__init__()
        self.id = 9
        self.left = 13
        self.right = None
        self.up = None
        self.down = 8

        i = 0
        while i < 768:
            self.block_list.add(Block(pos = (i, 0)))
            self.block_list.add(Block(pos = (704, i)))
            if i != 512 and i != 576:
                self.block_list.add(Block(pos = (i, 512)))
            i += 64

class Room10(Room):
    def __init__(self):
        super().__init__()
        self.id = 10
        self.left = None
        self.right = 5
        self.up = 11
        self.down = None

        i = 0
        while i < 768:
            self.block_list.add(Block(pos = (0,i)))
            if i != 384 and i != 448:
                self.block_list.add(Block(pos = (704,i)))
            if i >= 64 and i <= 512:
                self.block_list.add(Block(pos = (320,i)))
            i += 64
        self.block_list.add(Block(pos = (256, 512), moving = (2,256,64,0,0,0)))
        self.block_list.add(Block(pos = (64,0), moving = (0,0,0,2,448,0)))

class Room11(Room):
    def __init__(self):
        super().__init__()
        self.id = 11
        self.left = None
        self.right = None
        self.up = 12
        self.down = 10

        i = 0
        while i < 768:
            if i != 320 and i != 384:
                self.block_list.add(Block(pos = (i, 0)))
            i += 64

        self.block_list.add(Block(pos = (320, 128), moving = (0,0,0,2,192,0)))
        self.block_list.add(Block(pos = (192, 192), moving = (2,256,64,0,0,0)))
        self.block_list.add(Block(pos = (512, 256), moving = (2,640,512,0,0,0)))
        self.block_list.add(Block(pos = (0, 320), moving = (2,128,0,0,0,0)))
        self.block_list.add(Block(pos = (384, 320), moving = (2,384,256,0,0,0)))
        self.block_list.add(Block(pos = (704, 448), moving = (2,640,512,0,0,0)))

        self.block_list.add(Block(pos = (0, 512)))
        self.block_list.add(Block(pos = (704, 512)))


class Room12(Room):
    def __init__(self):
        super().__init__()
        self.id = 12
        self.left = None
        self.right = 13
        self.up = None
        self.down = 11

        i = 0
        while i < 768:
            self.block_list.add(Block(pos = (448, i)))
            if i != 320 and i != 384:
                self.block_list.add(Block(pos = (i, 512)))
            i += 64

class Room13(Room):
    def __init__(self):
        super().__init__()
        self.id = 13
        self.left = 12
        self.right = 9
        self.up = None
        self.down = None
        self.background = p.image.load("Images\\win.png")

        i = 0
        while i < 768:
            self.block_list.add(Block(pos = (i, 0)))
            self.block_list.add(Block(pos = (i, 512)))
            i += 64

    #In case player finds the secret room
    def update(self):
        self.background = p.image.load("Images\\true_win.png")
