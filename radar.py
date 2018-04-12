import pygame
import math
import serial
import numpy as np
ser = serial.Serial('/dev/ttyUSB1', 9600)
pygame.init()
screen = pygame.display.set_mode((720, 480))
pygame.display.set_caption('Radar')
done = False
arduino = ''
dist = ''
pos = ''

clock = pygame.time.Clock()

while not done:
    screen.fill((100, 100, 200))
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()

    arduino = ser.readline()
    dist = arduino[:arduino.find('p')]
    pos = arduino[arduino.find('p')+1:]

    print dist
    print pos

    x = (int(dist)/2 * np.cos((1+(float(pos)/180))*np.pi))+360
    y = (int(dist)/2 * np.sin((1+(float(pos)/180))*np.pi))

    print x -360
    print y

    pygame.draw.circle(screen, (100,0,0), (int(x), -1*int(y)), 5)



    pygame.display.update()
    clock.tick(90)
