import pygame as p
from item import Item

class Player(Item):

  def __init__(self, pos=(0,0)):
    img = []#Load all images here
    super().__init__(pos=pos,img=img)
    self.fallen = 0
    self.jump = 0
    self.shot = 0
    self.dead = 0
    self.hurt = 0
    self.xvel = 0
    self.yvel = 0 
  
  def update(self):
    self.rect.x += self.xvel
    self.rect.y += self.yvel
  
  
    
    