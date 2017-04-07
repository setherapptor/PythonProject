import pygame as p
from item import Item
from block import Block
from player import Player
import color

class Game():
 
  def __init__(self):
      self.sprites = p.sprite.Group()
      self.player = p.sprite.Group()
      self.player.add(Player(pos = (0,0)))
      self.sprites.add(Item(pos = (400,300)))
      self.sprites.add(Block(pos = (400,300)))
      self.sprites.add(Block(pos = (100,100),moving = (4,800,0,0,0,0)))
      self.sprites.add(Block(pos = (200,200),moving = (0,0,0,3,600,0)))
      self.sprites.add(Block(pos = (0,0),moving = (4,800,0,3,600,0)))
      self.paused = False
      
  def handle_events(self):
    #event handling here
    for event in p.event.get():
      print(event)
      if event.type == p.QUIT:
        return True
      if event.type == p.MOUSEBUTTONDOWN:
        self.paused = not self.paused
    return False

  def logic(self):
    #Logic goes here
    if self.paused == False:
      self.sprites.update()
      self.player.blocks = self.sprites # Get plater from list first
      
      self.player.update()

  def draw_frame(self, screen):
    #Drawing goes here
    if self.paused == False:
      screen.fill(color.BLACK)
      
      self.sprites.draw(screen)
      self.player.draw(screen)
      
      p.display.flip()