# This is a sample Python script.
import random
import pygame

pygame.init()
screen = pygame.display.set_mode([800, 600])

keep_going = True
GREEN = (0, 255, 0)

radius = 50

colors = [0]*100
locations = [0]*100
sizes = [0]*100
while keep_going:
    for n in range(100):
        colors[n] = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        sizes[n] = (random.randint(10,100))
        new_x = locations[n][0] + 1
        new_y = locations[n][1] + 1
        locations[n] = (new_x, new_y)
        for n in range(100):
            pygame.draw.circle(screen, colors[n], locations[n], sizes[n])
            if new_x > 800:
                new_x -= 800
            if new_y > 600:
                new_y -= 600



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keep_going= False
            pygame.display.update()



pygame.quit()
