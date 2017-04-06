import pygame as p
from item import Item

class Block(Item):

  def __init__(self, pos=(0,0), moving=[0,0,0,0,0,0]):
    super().__init__(pos=pos, img = p.image.load('block.jpeg'))
    self.moving = moving
    
  def update(self):
    #for moving, no player or enemy dertection yet
    if self.moving[0] > 0:
      if self.rect.x < self.moving[1]:
        self.rect.x += self.moving[0]
      else:
        self.moving = (-self.moving[0],self.moving[1],self.moving[2],self.moving[3],self.moving[4],self.moving[5])
    elif self.moving[0] < 0:
      if self.rect.x > self.moving[2]:
        self.rect.x += self.moving[0]
      else:
        self.moving = (-self.moving[0],self.moving[1],self.moving[2],self.moving[3],self.moving[4],self.moving[5])
        
    if self.moving[3] > 0:
      if self.rect.y < self.moving[4]:
        self.rect.y += self.moving[3]
      else:
        self.moving = (self.moving[0],self.moving[1],self.moving[2],-self.moving[3],self.moving[4],self.moving[5])
    elif self.moving[3] < 0:
      if self.rect.y > self.moving[5]:
        self.rect.y += self.moving[3]
      else:
        self.moving = (self.moving[0],self.moving[1],self.moving[2],-self.moving[3],self.moving[4],self.moving[5])
      
    
  