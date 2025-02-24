# task 1: create a new directory named "my_project"
import pygame
import random
width_ba=1000
height_ba=600
class Shape: 
    def __init__(self):
        self.width = width_ba
        self.height = height_ba
        self.speed = 5
        self.direction = None
        self.x:int = None 
        self.y:int = None
        self.color=None
        self.size=None
    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    def random_size(self):
        return random.randint(20, 50)
    def random_x_position(self):
        return random.randint(20, self.width-40)
    def random_y_position(self):
        return random.randint(20, self.height-40)
    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]
        if self.x < 20 or self.x > width_ba - 2 * self.size-20:
            self.direction[0] *= -1
        if self.y < 20 or self.y > height_ba - 2 * self.size-20:
            self.direction[1] *= -1 
    def change_direction(self, direction):
        self.direction = direction
    def random_direction(self):
        self.direction = [random.choice([-1, 1]), random.choice([-1, 1])]
        return self.direction
class Rectangle(Shape):
    def __init__(self,shape, x, y, size, color,direction):
        super().__init__()
        self.shape = shape
        self.x = x
        self.y = y
        self.size =  size
        self.color = color
        self.speed = 5
        self.direction = direction
    def draw(self, screen):
        self.shape(screen, self.color, (self.x, self.y, self.size, self.size))
        pygame.draw.rect
class RandomShapeFactory:
    def __init__(self):
        self.shape = Shape()
    def create_rectangle(self,shape_type):
        if shape_type == "rectangle":
            return Rectangle(pygame.draw.rect,self.shape.random_x_position(),self.shape.random_y_position(), self.shape.random_size(), self.shape.random_color(), self.shape.random_direction()  )
        elif shape_type == "circle":
            return Circle(pygame.draw.circle,self.shape.random_x_position(),self.shape.random_y_position(),self.shape.random_size(),self.shape.random_color(), self.shape.random_direction() )
class Circle(Shape):
    def __init__(self,shape, x=None, y=None, size=None, color=None, direction=None):
        super().__init__()
        self.shape = shape
        self.x = x
        self.y = y
        self.size = size
        self.color =  color
        self.speed = 5
        self.direction = direction
    def draw(self, screen):
        self.shape(screen, self.color, (self.x, self.y), self.size)
def main(): 
    pygame.init()
    rs=RandomShapeFactory()
    shape_types=["rectangle", "circle"]
    shapes=[rs.create_rectangle(random.choice(shape_types)) for _ in range(10)]
    gameScreen=pygame.display.set_mode((width_ba,height_ba))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        gameScreen.fill((255, 255, 255))
        for shape in shapes:
            shape.move()
            shape.draw(gameScreen)
        pygame.display.update()
        clock.tick(60)
        pygame.display.flip()
if __name__ == "__main__":
    main()




