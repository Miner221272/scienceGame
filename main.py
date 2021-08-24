import pygame
import keyboard
# The background color can be whatever you want
background_colour = (255,255,255)
(width, height) = (1200, 600)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tutorial 1')
screen.fill(background_colour)
pygame.display.flip()
running = True
# make the x position, y position, width and the height of the rectangle
x_pos = 20
y_pos = 20
width = 50
height = 50
bright_blue =(0,255,255)
# make the rectangle variable
rectangle = pygame.Rect(x_pos, y_pos, width, height)

# now add this to a surface, add a colour and the rectangle and make it a function
def make_rect():
	pygame.draw.rect(screen, (bright_blue), rectangle)

while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    if keyboard.is_pressed('w'):
        y_pos = y_pos-10
    if keyboard.is_pressed('s'):
        y_pos = y_pos+10
    if keyboard.is_pressed('a'):
        x_pos = x_pos-10
    if keyboard.is_pressed('d'):
        x_pos = x_pos+10
  make_rect()
  pygame.display.update()