import pygame as p
from item import Item

class Block(Item):

  def __init__(self, pos=(0,0), moving=[0,0,0,0,0,0]):
    super().__init__(pos=pos, img = p.image.load('Images\\block.png'))
    self.moving = moving
    self.followers = None
    
  def update(self):
    #for moving
    moved_y = False
    if self.moving[0] > 0:
      if self.rect.x < self.moving[1]:
        if not self.followers == None:
            self.rect.x += 2
            self.rect.y -= 2
            test = p.sprite.spritecollide(self, self.followers, False) # IF COLLISION, test > 
            self.rect.x -= 2
            self.rect.y += 2
            if len(test) > 0:
              for follower in test:
                follower.move_x(self.moving[0])
        self.rect.x += self.moving[0]
      else:
        self.moving = (-self.moving[0],self.moving[1],self.moving[2],self.moving[3],self.moving[4],self.moving[5])
    elif self.moving[0] < 0:
      if self.rect.x > self.moving[2]:
        if not self.followers == None:
            self.rect.x -= 2
            self.rect.y -= 2
            test = p.sprite.spritecollide(self, self.followers, False)
            self.rect.x += 2
            self.rect.y += 2
            if len(test) > 0:
              for follower in test:
                follower.move_x(self.moving[0])
        self.rect.x += self.moving[0]
      else:
        self.moving = (-self.moving[0],self.moving[1],self.moving[2],self.moving[3],self.moving[4],self.moving[5])
        
    if self.moving[3] > 0:
      if self.rect.y < self.moving[4]:
        if not self.followers == None:
          #For pull down
          self.rect.y -= 2
          test = p.sprite.spritecollide(self, self.followers, False)
          self.rect.y += 2
          if len(test) > 0:
            self.rect.y += self.moving[3]
            for follower in test:
                follower.move_y(self.moving[3])
            self.rect.y -= self.moving[3]
          #for push down
          self.rect.y += 2
          test = p.sprite.spritecollide(self, self.followers, False)
          self.rect.y -= 2
          if len(test) > 0:
            self.rect.y += self.moving[3]
            for follower in test:
                follower.move_y(self.moving[3])
            self.rect.y -= self.moving[3]
        self.rect.y += self.moving[3]
      else:
        self.moving = (self.moving[0],self.moving[1],self.moving[2],-self.moving[3],self.moving[4],self.moving[5])
    elif self.moving[3] < 0:
      if self.rect.y > self.moving[5]:
        if not self.followers == None:
          self.rect.y -= 2
          test = p.sprite.spritecollide(self, self.followers, False)
          self.rect.y += 2
          if len(test) > 0:
            for follower in test:
                follower.move_y(self.moving[3])
        self.rect.y += self.moving[3]
      else:
        self.moving = (self.moving[0],self.moving[1],self.moving[2],-self.moving[3],self.moving[4],self.moving[5])
      
    
  