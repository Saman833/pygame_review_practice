# task 1: create a new directory named "my_project"
import pygame 
pygame.init()
width_ba=1000
hight_ba=600
gameScreen=pygame.display.set_mode((width_ba,hight_ba))
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(60)
    
