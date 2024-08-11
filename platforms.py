import pygame
pygame.init()

#Variables improtantes
screenWidth, screenHeight = 800, 500
screen = pygame.display.set_mode((screenWidth,screenHeight))
clock = pygame.time.Clock()

#Clases
class platform(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, (255,0,0), (self.x, self.y, self.width, self.height), 1)

#Funciones
def redrawScreen(screen):
    screen.fill((0,0,0))
    pltf_1.draw(screen)
    pygame.display.update()

pltf_1 = platform(0,(screenHeight-100),screenWidth,100,)

run = True
while run:
    clock.tick(20)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        run = False

    redrawScreen(screen)
pygame.QUIT()