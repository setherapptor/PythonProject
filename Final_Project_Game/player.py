import pygame as p
from item import Item
import constants

class Player(Item):
  #TODO: Make it that if inside a block before moving, move up until okay, may make stairs or slants possible



  def __init__(self, pos=(0,0)):
    self.images = [p.image.load("Images\\stand.png"),p.image.load("Images\\walk.png"),p.image.load("Images\\jump.png"),p.image.load("Images\\fall.png"),p.image.load("Images\\hurt.png"),p.image.load("Images\\dead.png")]#Load all images here
    super().__init__(pos=pos,img=p.image.load("Images\\stand.png"))
    #action decay
    self.fallen = 0
    self.jump = 0
    self.shot = 0
    self.dead = 0
    self.hurt = 0

    #for movement
    self.xvel = 0
    self.yvel = 0

    #for some sprite calculations
    self.clock = 120

    #for collision testing
    self.blocks = None

    #for walking
    self.right = False
    self.left = False

  def update(self):

    #Internal Clock Tick
    self.clock -= 1
    if self.clock <= 0:
      self.clock = 120

    #Falling check
    if not self.grounded() and self.jump == 0:#IF not grounded and not mid jump
      if(self.clock % 3 == 0 or self.yvel == 0):#Calculate gravity
        #self.move_y(dist=min(constants.TERMINAL_VELOCITY, self.yvel + 1))
        self.yvel = min(constants.TERMINAL_VELOCITY, self.yvel + 1)
    else:
      self.yvel = min(0, self.yvel)#If falling, stop. Else: keep going(up)
      if self.jump > 0:
        self.yvel = -constants.JUMP_SPEED
        if self.jump == 1:
          self.yvel = - (2 * constants.JUMP_SPEED) // 3

    #Walking
    if self.left and self.right:
      self.xvel = self.xvel - self.sign(self.xvel)
    elif self.right:
      self.xvel = min(self.xvel + constants.WALK_ACCELERATION, constants.TOP_SPEED)
    elif self.left:
      self.xvel = max(self.xvel - constants.WALK_ACCELERATION, -constants.TOP_SPEED)
    elif self.grounded():
      self.xvel = self.xvel - self.sign(self.xvel)


    #Move and Collision
    collided_y = self.move_y(self.yvel)
    if collided_y:
      #If collided on y, either
      self.jump = 0 # if on top
      self.yvel = 0 #either collision on top or bottom

    collided_x = self.move_x(self.xvel)
    if collided_x:
      #If collided on x, either
      self.xvel = 0

    #Sprite Calculations and Decay(If multiple frames for a sprite, use % on the decay factor or on clock)
    if self.dead > 0:
      self.image = self.images[5]
      self.dead -= 1
    elif self.yvel < 0 or self.jump > 0:
      self.image = self.images[2]
      self.jump = max(self.jump - 1, 0)
    elif self.yvel > 0:
      self.image = self.images[3]
    elif not self.xvel == 0 and self.grounded():
      self.image = self.images[1]
    else:
      self.image = self.images[0]


  def move_x(self, dist=1):
    #return True on collsion, False otherwise
    if not dist == 0:
      tick = self.sign(dist)
      for i in range(abs(dist)):
        self.rect.x += tick
        collide_blocks = p.sprite.spritecollide(self, self.blocks, False)
        if len(collide_blocks) > 0:
          self.rect.x -= tick
          return True
      return False

  def move_y(self, dist=1):
    #return True on collsion, False otherwise
    if not dist == 0:
      tick = self.sign(dist)
      for i in range(abs(dist)):
        self.rect.y += tick
        collide_blocks = p.sprite.spritecollide(self, self.blocks, False)
        if len(collide_blocks) > 0:
          self.rect.y -= tick
          return True
      return False

  def jump_start(self):
    if self.grounded():
      self.jump = constants.JUMP_TIME

  def jump_stop(self):
    self.jump = min(self.jump, 1)

  def grounded(self):
    if not self.blocks == None:
      self.rect.y += 1
      grounded_plats = p.sprite.spritecollide(self, self.blocks, False)
      self.rect.y -= 1
      if len(grounded_plats) > 0:
        return True
      else:
        return False
    else:
      return False


  def sign(self, num):# For Various math
    if num == 0 or num == None:
      return 0
    return num//abs(num)
