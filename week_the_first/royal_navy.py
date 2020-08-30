import pygame, sys


pygame.init()

#set the screen size 
size = width, height = 800, 800
                     #Left, Top      ,Width, Height
sea_rect = pygame.Rect(0, int(height / 2), width, int(height / 2)  )
screen = pygame.display.set_mode(size)

########### R    G    B
sky_color = 135, 206, 235
sea_color = 35, 142, 104
# 
# troubled_sky_color = RED, GREEN, BLUE
# troubled_sea_color = RED, GREEN, BLUE

#load up the british flag
british_sailing_flag = pygame.image.load('british_sailing_flag.png')
#jolly_roger = pygame.image.load('FILENAME_GOES_HERE.png')
#load the ship
ship = pygame.image.load('ship.png')

#get the size of the flag
flag_rect = british_sailing_flag.get_rect()
ship_rect = ship.get_rect() #yarr she be ship rect, matey
flag_pos = 550, 150

pygame.font.init()  
# REMOVE THIS HERE FUNNY FONT, this is serious biznis
funny_font = pygame.font.SysFont('Comic Sans MS', 12)

clicked = False

while 1:
  for event in pygame.event.get():
    if event.type ==  pygame.MOUSEBUTTONUP:
      clicked = True
    if event.type == pygame.QUIT: 
      sys.exit()

  screen.fill(sky_color)
  
  pygame.draw.rect(screen, sea_color, sea_rect)
  screen.blit(ship,  screen.get_rect() )
  screen.blit(british_sailing_flag, flag_pos)
  #if ye be wanting to do something when the winder is clicked, do it here
  if clicked:
    #don't render this funny font if ye be serious about pirating, matey
    text_surface = funny_font.render("""The sun never sets on Her Majesty's Navy""", False, (0, 0, 0))
    screen.blit(text_surface,(0,0))
    #here's where we hoist the jolly roger and rid us of her majesty's towelette 
    

  pygame.display.flip()


