import pygame as p
from item import Item

class Player(Item):

  def __init__(self, pos=(0,0)):
    img = []
    super().__init__(pos=pos,img=img)
    self.fallen = 0
    self.jump = 0
    self.shot = 0
    self.dead = 0
    self.hurt = 0
  
  
    
    