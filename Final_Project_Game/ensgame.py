import pygame as p
from game import Game
from item import Item
import color
import constants

def main():
  p.init()
  
  size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
  display = p.display.set_mode(size)
  
  p.display.set_caption('Evan and Seth\'s Game!')
  p.display.set_icon(p.image.load('Images\\icon.png'))
  
  done = False
  
  clock = p.time.Clock()
  
  game = Game()

  while not done:
    done = game.handle_events()
    game.logic()
    game.draw_frame(display)
    
    clock.tick(60)
    
  p.quit()
  
if __name__ == '__main__':
  main()