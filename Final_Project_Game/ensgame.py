import pygame as p
from game import Game
from item import Item
import color

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def main():
  p.init()
  
  size = [SCREEN_WIDTH, SCREEN_HEIGHT]
  display = p.display.set_mode(size)
  
  p.display.set_caption('Evan and Seth\'s Game!')
  p.display.set_icon(p.image.load('icon.png'))
  
  done = False
  
  clock = p.time.Clock()
  
  game = Game()

  while not done:
    done = game.handle_events()
    game.logic()
    game.draw_frame(display)
    
    clock.tick(60)
    
  pygame.quit()
  
if __name__ == '__main__':
  main()