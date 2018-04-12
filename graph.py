import pygame
import math

pygame.init()
screen = pygame.display.set_mode((1600, 850))
pygame.display.set_caption('STEM Quickie')
done = False
is_blue = True
side = 1600
top = 850
s = 0
s1 = 0
x = 1570
y = 770
r = 1
dead = True
dead1 = True
x1 = 30
y1 = 30
r1 = 0
p = []
f = True
f1 = True
p1 = []
ftrue = 0

clock = pygame.time.Clock()

while not done:
    if not dead or not dead1:
        if dead:
            s += 1
            ftrue = 50
        if dead1:
            s1 += 1
            ftrue = -50
        x = 1570
        y = 770
        r = 1
        dead = True
        dead1 = True
        x1 = 30
        y1 = 30
        r1 = 0
        p = []
        p1 = []
        f = True
        f1 = True
    if x<0:
        x += side
    elif x>side:
        x-= side
    if y<0:
        y += top
    elif y>top:
        y -=top
    if x1<0:
        x1 += side
    elif x1>side:
        x1-= side
    if y1<0:
        y1 += top
    elif y1>top:
        y1 -=top
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    done = True

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP] and ftrue == 0:
        y += int(round(2.5*math.sin(r*math.pi)))
        x += int(round(2.5*math.cos(r*math.pi)))
    if pressed[pygame.K_DOWN] and ftrue == 0:
        y -= int(round(2.5*math.sin(r*math.pi)))
        x -= int(round(2.5*math.cos(r*math.pi)))
    if pressed[pygame.K_RIGHT] and ftrue == 0: r += .01
    if pressed[pygame.K_LEFT] and ftrue == 0: r -= .01
    if pressed[pygame.K_RSHIFT] and ftrue == 0:
        if len(p) < 3 and f:
            p.append([x+int(round(30*math.cos(r*math.pi))), y+int(round(30*math.sin(r*math.pi))), r, 60])
            f = False
    else: f = True

    if pressed[pygame.K_w] and ftrue == 0:
        y1 += int(round(2.5*math.sin(r1*math.pi)))
        x1 += int(round(2.5*math.cos(r1*math.pi)))
    if pressed[pygame.K_s] and ftrue == 0:
        y1 -= int(round(2.5*math.sin(r1*math.pi)))
        x1 -= int(round(2.5*math.cos(r1*math.pi)))
    if pressed[pygame.K_d] and ftrue == 0: r1 += .01
    if pressed[pygame.K_a] and ftrue == 0: r1 -= .01
    if pressed[pygame.K_q] and ftrue == 0:
        if len(p1) < 3 and f1:
            p1.append([x1+int(round(30*math.cos(r1*math.pi))), y1+int(round(30*math.sin(r1*math.pi))), r1, 60])
            f1 = False
    else: f1 = True


    if ftrue == 0:
        screen.fill((125, 125, 125))
    elif ftrue>0:
        screen.fill((0, 100, 200))
        ftrue -= 1
    elif ftrue<0:
        screen.fill((200, 100, 0))
        ftrue +=1
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    label = myfont.render("one: "+str(s)+" two: "+str(s1), 1, (255, 0, 0))
    screen.blit(label, (side/2, top/2))
    if dead:
        pygame.draw.circle(screen, (0, 125, 255), (x, y), 25)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r-.125)*math.pi))), y+int(round(30*math.sin((r-.125)*math.pi)))), 5)
        pygame.draw.circle(screen, (0,0,0), (x+int(round(30*math.cos((r+.125)*math.pi))), y+int(round(30*math.sin((r+.125)*math.pi)))), 5)

    if dead1:
        pygame.draw.circle(screen, (255, 125, 0), (x1, y1), 25)
        pygame.draw.circle(screen, (0,0,0), (x1+int(round(30*math.cos((r1-.125)*math.pi))), y1+int(round(30*math.sin((r1-.125)*math.pi)))), 5)
        pygame.draw.circle(screen, (0,0,0), (x1+int(round(30*math.cos((r1+.125)*math.pi))), y1+int(round(30*math.sin((r1+.125)*math.pi)))), 5)



    for i in p:
        if i[0]<0:
            i[0] += side
        elif i[0]>side:
            i[0] -= side
        elif i[1]<0:
            i[1] += top
        elif i[1]>top:
            i[1] -= top
        if i[3] > 0:
            i[1] += int(round(10*math.sin(i[2]*math.pi)))
            i[0] += int(round(10*math.cos(i[2]*math.pi)))
            i[3] -= 1
        pygame.draw.circle(screen, (0, 100, 200), (i[0], i[1]), 5)
        pygame.draw.circle(screen, (0, 0, 0), (i[0], i[1]), 6, 2)
        if 30 > math.sqrt((abs(i[0]-x)**2)+(abs(i[1]-y)**2)):
            #dead = False
            p.remove(i)
        if 30 > math.sqrt((abs(i[0]-x1)**2)+(abs(i[1]-y1)**2)):
            dead1 = False
            p.remove(i)

    for i in p1:
        if i[0]<0:
            i[0] += side
        elif i[0]>side:
            i[0] -= side
        elif i[1]<0:
            i[1] += top
        elif i[1]>top:
            i[1] -= top
        if i[3] > 0:
            i[1] += int(round(10*math.sin(i[2]*math.pi)))
            i[0] += int(round(10*math.cos(i[2]*math.pi)))
            i[3] -= 1
        pygame.draw.circle(screen, (200, 100, 0), (i[0], i[1]), 5)
        pygame.draw.circle(screen, (0, 0, 0), (i[0], i[1]), 6, 2)
        if 30 > math.sqrt((abs(i[0]-x)**2)+(abs(i[1]-y)**2)):
            dead = False
            p1.remove(i)
        if 30 > math.sqrt((abs(i[0]-x1)**2)+(abs(i[1]-y1)**2)):
            #dead1 = False
            p1.remove(i)

    pygame.display.update()
    clock.tick(90)
