import pygame as p
from item import Item
from block import Block
from player import Player
import color

class Game():
 
  def __init__(self):
      self.blocks = p.sprite.Group()
      self.sprites = p.sprite.Group()
      self.player = Player(pos = (0,0))
      self.sprites.add(self.player)
      self.blocks.add(Item(pos = (400,300)))
      self.blocks.add(Block(pos = (400,300)))
      self.blocks.add(Block(pos = (0, 500)))
      self.blocks.add(Block(pos = (100,100),moving = (4,800,0,0,0,0)))
      self.blocks.add(Block(pos = (200,200),moving = (0,0,0,3,600,0)))
      self.blocks.add(Block(pos = (0,0),moving = (4,800,0,3,600,0)))
      self.paused = False
      
  def handle_events(self):
    #event handling here
    for event in p.event.get():
      print(event)
      if event.type == p.QUIT:
        return True
      elif event.type == p.MOUSEBUTTONDOWN:
        self.paused = not self.paused
      elif event.type == p.KEYDOWN:
        if event.key == p.K_SPACE:
          self.player.jump_start()
      elif event.type == p.KEYUP:
        if event.key == p.K_SPACE:
          self.player.jump_stop()
      
    return False

  def logic(self):
    #Logic goes here
    if self.paused == False:
      self.player.blocks = self.blocks # Get player from list first
      self.sprites.update()
      self.blocks.update()
      
  def draw_frame(self, screen):
    #Drawing goes here
    if self.paused == False:
      screen.fill(color.BLACK)
      
      self.sprites.draw(screen)
      self.blocks.draw(screen)
      
      p.display.flip()