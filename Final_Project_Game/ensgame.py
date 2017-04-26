#ensgame.py
#Contains the main and initializes both the Game and Pygame
#ensgame stands for Evan and Seth's game

import pygame as p
from game import Game
import constants

def main():
  #Initializes pygame
  p.init()
  
  #Creates a display that the game prints objects to
  size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
  display = p.display.set_mode(size)
  
  #Sets window's name and icon
  p.display.set_caption('Evan and Seth\'s Game!')
  p.display.set_icon(p.image.load('Images\\icon.png'))
  
  #If True, the game closes and ends
  done = False
  
  #Clock lets the game pause for a tiny bit so that the target framerate is not exceeded
  clock = p.time.Clock()
  
  #initializes Game from game.py
  game = Game()

  while not done:
    done = game.handle_events()
    game.logic()
    game.draw_frame(display)
    
    clock.tick(60)#Target framerate is 60 frames per second
    
  p.quit()
  
if __name__ == '__main__':
  main()