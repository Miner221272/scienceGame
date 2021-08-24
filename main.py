import pygame.display
import pyautogui

def res(resX, resY):
    pygame.display.set_mode((resX, resY))
    pygame.display.set_mode(modes[0], FULLSCREEN, 16)
    pygame.display.init()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    width, height= pyautogui.size()
    res(width,height)

# See PyCharm help at https://www.jetbrains.com/help/pych