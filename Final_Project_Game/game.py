import pygame as p
from item import Item
from block import Block
import color

class Game():
 
  def __init__(self):
      self.sprites = p.sprite.Group()
      self.sprites.add(Item(pos = (400,300)))
      self.sprites.add(Block(pos = (400,300)))
      self.sprites.add(Block(pos = (100,100),moving = (8,800,0,0,0,0)))
      self.sprites.add(Block(pos = (200,200),moving = (0,0,0,6,600,0)))
      self.sprites.add(Block(pos = (0,0),moving = (8,800,0,6,600,0)))
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

  def draw_frame(self, screen):
    #Drawing goes here
    if self.paused == False:
      screen.fill(color.BLACK)
      
      self.sprites.draw(screen)
      
      p.display.flip()