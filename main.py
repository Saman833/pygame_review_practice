# task 1: create a new directory named "my_project"
import pygame
import random
width_ba=1000
hight_ba=600
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = (0, 0, 255)
        self.speed = 5
        self.direction = [1, 1]
    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        if self.x < 20 or self.x > width_ba - 2 * self.radius-20:
            self.direction[0] *= -1
        if self.y < 20 or self.y > hight_ba - 2 * self.radius-20:
            self.direction[1] *= -1 
    def change_direction(self, direction):
        self.direction = direction
    def change_direction_randomly(self):
        self.direction = (random.randint(-1, 1), random.randint(-1, 1))
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
def main(): 
    pygame.init()
    circle1 = Circle(50, 40, 40)
    gameScreen=pygame.display.set_mode((width_ba,hight_ba))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        gameScreen.fill((255, 255, 255))
        circle1.move()
        circle1.draw(gameScreen)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()
if __name__ == "__main__":
    main()




