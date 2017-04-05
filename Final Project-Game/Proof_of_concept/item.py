#Item class to be used 
import pygame as p

class Item():
  def __init__(self, img='null.png',visible=True, pos=(0,0)):
    self.img = p.image.load(img)
    self.visible = visible
    self.pos = pos
  
  def setImg(self, img):
    self.img = p.image.load(img)
    
  def getPos(self):
    return self.pos
  
  def setPos(self, pos):
    self.pos = pos
    
  def pushX(self, x):
    self.pos = (self.pos[0] + x, self.pos[1])
  
  def pushY(self, y):
    self.pos = (self.pos[0], self.pos[1] + y)
    
  def frame(self):#To be used in descendants, suppose to be called once per frame 
    pass
    
  def get_rect(self):
    return self.img.get_rect()
  
  def blit(self, screen):
    if self.visible:
      screen.blit(self.img, self.pos)