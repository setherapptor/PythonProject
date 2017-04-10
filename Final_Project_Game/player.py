import pygame as p
from item import Item
import constants

class Player(Item):

  def __init__(self, pos=(0,0)):
    self.images = [p.image.load("Images\\stand.png"),p.image.load("Images\\walk.png"),p.image.load("Images\\jump.png"),p.image.load("Images\\fall.png"),p.image.load("Images\\hurt.png"),p.image.load("Images\\dead.png")]#Load all images here
    super().__init__(pos=pos,img=p.image.load("Images\\stand.png"))
    self.fallen = 0
    self.jump = 0
    self.shot = 0
    self.dead = 0
    self.hurt = 0
    self.xvel = 0
    self.yvel = 0
    self.clock = 120
    self.blocks = None
  
  def update(self):
    self.rect.x += self.xvel
    self.rect.y += self.yvel
    self.clock -= 1
    
    if self.clock <= 0:
      self.clock = 120
    
    #Falling check
    if not self.grounded() and self.jump == 0:#IF not grounded and not mid jump
      if(self.clock % 5 == 0 or self.yvel == 0):#Calculate gravity
        self.yvel = min(constants.TERMINAL_VELOCITY, self.yvel + 1)
    else:
      self.yvel = min(0, self.yvel)#If falling, stop. Else: keep going(up)
      if self.jump > 0:
        self.yvel = -constants.JUMP_SPEED
    
    self.rect.y += self.yvel
    #Add check for head collision
    
    #Sprite Calculations (If multiple frames for a sprite, use % on the decay factor or on clock)
    if self.dead > 0:
      self.image = self.images[5]
      self.dead -= 1
    elif self.jump > 0:
      self.image = self.images[2]
      self.jump -= 1
    elif self.yvel > 0:
      self.image = self.images[3]
    elif not self.xvel == 0:
      self.image = self.images[1]
    else:
      self.image = self.images[0]
      
  
  def move_x(self):
  
  def jump_start(self):
    if self.grounded():
      self.jump = constants.JUMP_TIME
      
  def jump_stop(self):
    self.jump = 0
  
  def grounded(self):
    if not self.blocks == None:
      self.rect.y += 2
      grounded_plats = p.sprite.spritecollide(self, self.blocks, False)
      self.rect.y -= 2
      if len(grounded_plats) > 0:
        return True
      else:
        return False
    else:
      return False
  
  
    
    