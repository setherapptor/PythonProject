import pygame as p

class Item(p.sprite.Sprite):

  def __init__(self, pos=(0,0), img = p.Surface([1,1])):
    super().__init__()
    self.image = img
    self.rect = self.image.get_rect()
    self.rect.x = pos[0]
    self.rect.y = pos[1]
    self.img = img
    