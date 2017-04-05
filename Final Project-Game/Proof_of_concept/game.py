import pygame as p
import color
from item import Item

def main():
  width, height = 800, 600

  p.init()
  gDisplay = p.display.set_mode((width, height))
  p.display.set_caption('proof of concept')
  p.display.set_icon(p.image.load('ball.png'))
  clock = p.time.Clock()

  playing = True
  click = True
  i = Item(img='ball.png',pos=(800,300))

  while playing:
    for event in p.event.get():
      if event.type == p.QUIT:
        playing = False
      if event.type == p.MOUSEBUTTONDOWN:
        if i.get_rect().collidepoint(p.mouse.get_pos()):
          click = not click
      
      print(event)
      
    gDisplay.fill(color.RED)
    i.blit(gDisplay)
    if click:
      i.pushX(-1)
    else:
      i.pushX(1)
    p.display.update()
    clock.tick(60)
      
  p.quit()
  sys.exit()

if __name__ == "__main__":
  main()