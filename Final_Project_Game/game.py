import pygame as p
from item import Item
import color

class Game():
 
  def __init__(self):
      self.sprites = p.sprite.Group()
      self.sprites.add(Item(pos = (400,300)))

  def handle_events(self):
    #event handling here
    for event in p.event.get():
      print(event)
      if event.type == p.QUIT:
        return True
    return False

  def logic(self):
    #Logic goes here
    pass

  def draw_frame(self, screen):
    #Drawing goes here
    screen.fill(color.WHITE)
    
    self.sprites.draw(screen)
    
    p.display.flip()