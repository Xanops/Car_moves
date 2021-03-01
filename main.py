import pygame

pygame.init()
screen = pygame.display.set_mode((600, 95))
screen.fill('white')


class Car(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('data/car2.png')
        self.img_left = pygame.transform.flip(self.img, True, False)

    def right(self):
        return self.img

    def left(self):
        return self.img_left


x, y = 0, 0
clock = pygame.time.Clock()
direction = 'right'

running = True
while running:
    time_delta = clock.tick(60) / 20
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill('white')
    if direction == 'right' and x + time_delta + 150 <= 600:
        x += time_delta
        screen.blit(Car().right(), (x, y))
    elif direction == 'right':
        direction = 'left'

    if direction == 'left' and x - time_delta >= 0:
        x -= time_delta
        screen.blit(Car().left(), (x, y))
    elif direction == 'left':
        direction = 'right'

    pygame.display.update()

pygame.quit()
