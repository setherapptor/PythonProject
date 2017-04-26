import pygame as p
from item import Item
from block import Block
from player import Player
from room import *
import color

class Game():

  def __init__(self):
      self.rooms = []
      room = Room0()
      self.rooms.append(room)
      room = Room1()
      self.rooms.append(room)
      room = Room2()
      self.rooms.append(room)
      room = Room3()
      self.rooms.append(room)
      room = Room4()
      self.rooms.append(room)
      room = Room5()
      self.rooms.append(room)
      self.current_room = self.rooms[0]
      self.blocks = p.sprite.Group()
      self.blocks = p.sprite.Group()
      self.sprites = p.sprite.Group()
      self.player = Player(pos = (200,200))
      self.sprites.add(self.player)
      self.blocks = self.current_room.block_list
      #self.blocks.add(Block(pos = (400,300)))
      #self.blocks.add(Block(pos = (0, 500)))
      #self.blocks.add(Block(pos = (64, 436)))
      #self.blocks.add(Block(pos = (100,100),moving = (4,800,0,0,0,0)))
      #self.blocks.add(Block(pos = (200,200),moving = (0,0,0,3,600,0)))
      #self.blocks.add(Block(pos = (0,0),moving = (4,800,0,3,600,0)))
      self.paused = False
      for block in self.blocks:
        block.followers = self.sprites

  def handle_events(self):
    #event handling here
    for event in p.event.get():
      print(event)
      if event.type == p.QUIT:
        return True
      elif event.type == p.KEYDOWN:
        if event.key == p.K_SPACE:
          self.player.jump_start()
        elif event.key == p.K_a or event.key == p.K_LEFT:
          self.player.left = True
        elif event.key == p.K_d or event.key == p.K_RIGHT:
          self.player.right = True
        elif event.key == p.K_ESCAPE:
          self.paused = not self.paused
      elif event.type == p.KEYUP:
        if event.key == p.K_SPACE:
          self.player.jump_stop()
        elif event.key == p.K_a or event.key == p.K_LEFT:
          self.player.left = False
        elif event.key == p.K_d or event.key == p.K_RIGHT:
          self.player.right = False

    return False

  def logic(self):
    #Logic goes here
    #Player goes too far right
    if self.player.rect.x > constants.SCREEN_WIDTH:
        if self.current_room.right != None:
            self.current_room = self.rooms[self.current_room.right]
        self.player.rect.x = 0
        #self.player.rect.y -= 1
    #Player goes too far left
    if self.player.rect.x < 0:
        if self.current_room.left != None:
            self.current_room = self.rooms[self.current_room.left]
        self.player.rect.x = constants.SCREEN_WIDTH
    #Player goes too far down
    if self.player.rect.y > constants.SCREEN_HEIGHT:
        if self.current_room.down != None:
            self.current_room = self.rooms[self.current_room.down]
        self.player.rect.y = 0
    #Player goes too far up
    if self.player.rect.y < 0:
        if self.current_room.up != None:
            self.current_room = self.rooms[self.current_room.up]
        self.player.rect.y = constants.SCREEN_HEIGHT


    self.blocks = self.current_room.block_list
    for block in self.blocks:
      block.followers = self.sprites
    if self.paused == False:
      self.player.blocks = self.blocks # Get player from list first
      self.sprites.update()
      self.blocks.update()

  def draw_frame(self, screen):
    #Drawing goes here
    if self.paused == False:
      screen.fill(color.BLACK)
      #Change above line to get background

      self.sprites.draw(screen)
      self.blocks.draw(screen)

      p.display.flip()
