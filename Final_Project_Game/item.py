import pygame as p

class Item(p.sprite.Sprite):

  def __init__(self, img=p.image.load('Images\\null.png'), pos=(0,0)):
    super().__init__()
    self.image = img
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    
    