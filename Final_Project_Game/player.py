import pygame as p
from item import Item

class Player(Item):

  def __init__(self, pos=(0,0)):
    img = [p.image.load("Images\\stand.png"),p.image.load("Images\\walk.png"),p.image.load("Images\\jump.png"),p.image.load("Images\\fall.png"),p.image.load("Images\\hurt.png"),p.image.load("Images\\dead.png")]#Load all images here
    super().__init__(pos=pos,img=img)
    self.fallen = 0
    self.jump = 0
    self.shot = 0
    self.dead = 0
    self.hurt = 0
    self.xvel = 0
    self.yvel = 0
    self.blocks = None
  
  def update(self):
    self.rect.x += self.xvel
    self.rect.y += self.yvel
    if not self.grounded():
      self.yvel += 1
  
  def grounded(self):
    self.rect.y += 2
    grounded_plats = p.sprite.spritecollide(self, self.blocks, False)
    self.rect.y -= 2
    
    if len(grounded_plats) > 0:
      return True
      
  
  
    
    