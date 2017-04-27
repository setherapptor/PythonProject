#game.py
#Contains all the information needed to run the game

import pygame as p
from item import Item
from block import Block
from player import Player
from room import *
import color

class Game():

  def __init__(self):
      #Flag for if player finds secret room
      self.flag = 0

      #Initialize list of rooms
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
      room = Room6()
      self.rooms.append(room)
      room = Room7()
      self.rooms.append(room)
      room = Room8()
      self.rooms.append(room)
      room = Room9()
      self.rooms.append(room)
      room = Room10()
      self.rooms.append(room)
      room = Room11()
      self.rooms.append(room)
      room = Room12()
      self.rooms.append(room)
      room = Room13()
      self.rooms.append(room)
      #Initialize starting room
      self.current_room = self.rooms[0]
      #Initialize all the blocks and sprites
      self.blocks = p.sprite.Group()
      self.blocks = p.sprite.Group()
      self.sprites = p.sprite.Group()
      #Starting position for player
      self.player = Player(pos = (200,200))
      self.sprites.add(self.player)
      self.blocks = self.current_room.block_list
      self.paused = False
      for block in self.blocks:
        block.followers = self.sprites

  def handle_events(self):
    #Event handling here
    for event in p.event.get():
      #If statement to end game
      if event.type == p.QUIT:
        return True
      #Key press events
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
    if self.player.rect.x > constants.SCREEN_WIDTH - 16:
        if self.current_room.right != None:
            self.current_room = self.rooms[self.current_room.right]
            self.current_room.__init__()
        self.player.rect.x = -16
    #Player goes too far left
    if self.player.rect.x < -16:
        if self.current_room.left != None:
            self.current_room = self.rooms[self.current_room.left]
            self.current_room.__init__()
        self.player.rect.x = constants.SCREEN_WIDTH - 16
    #Player goes too far down
    if self.player.rect.y > constants.SCREEN_HEIGHT:
        if self.current_room.down != None:
            self.current_room = self.rooms[self.current_room.down]
            self.current_room.__init__()
        self.player.rect.y = 0
    #Player goes too far up
    if self.player.rect.y < 0:
        if self.current_room.up != None:
            self.current_room = self.rooms[self.current_room.up]
            self.current_room.__init__()
        self.player.rect.y = constants.SCREEN_HEIGHT

    #Player found secret room
    if self.current_room.id == 6:
        self.flag = 1
    elif self.current_room.id == 13:
        if self.flag == 1:
            self.current_room.update()
    #Update blocks if room changed
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
      screen.blit(self.current_room.background, dest = (0,0))

      self.sprites.draw(screen)
      self.blocks.draw(screen)

      p.display.flip()
