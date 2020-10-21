import pygame, sys, random, time
from pygame.locals import *



class Enermy:
      def __init__(self):
            self.x = random.randint(0, 570)
            self.y = -100
            self.dy = 0
            self.dy = random.randint(2, 6)
            self.dx = random.choice((-(self.dy), (self.dy)))

      def move(self):
            self.dy += 0.1
            self.y += self.dy
            self.x += self.dx
      def draw(self):
            screen.blit(enermy_image, (self.x, self.y))
      def off_screen(self):
            return self.y > 640

      def bounce(self):
            if self.x>570 or self.x<0:
                  self.dx = -(self.dx)


class Forces:
      def __init__(self):
            self.x = 320

      def move(self):
            if pressed_keys[K_LEFT] and self.x>0:
                  self.x -= 3
            if pressed_keys[K_RIGHT] and self.x<540:
                  self.x += 3

      def draw(self):
            screen.blit(forces_image, (self.x, 574))


class Missile:
      def __init__(self,x):
            self.x = x
            self.y = 574

      def move(self):
            self.x += 5

      def off_screen(self):
            return self.y < -8
      def draw(self):
            pygame.draw.line(screen, (255,0,0),(self.x, self.y), (self.x,self.y+8),1)
enermys = []
forces = Forces()
missiles = []

pygame.init()
pygame.display.set_caption("Galaga")
screen = pygame.display.set_mode((640, 650))

enermy_image = pygame.image.load("enemy.png").convert()
enermy_image.set_colorkey((0,0,0))

forces_image = pygame.image.load("forces.png").convert()
forces_image.set_colorkey((0,0,0))

last_enermy_spawn_time = 0

clock = pygame.time.Clock()

while 1:
      clock.tick(60)
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  sys.exit()

      pressed_keys = pygame.key.get_pressed()
                  
      if time.time() - last_enermy_spawn_time > 1:
            enermys.append(Enermy())
            last_enermy_spawn_time = time.time()
            
      screen.fill((0, 0, 0))
      forces.move()
      forces.draw()
      
      i = 0
      while i < len(enermys):
            enermys[i].move()
            enermys[i].bounce()
            enermys[i].draw()
      
            if enermys[i].off_screen():
                  del enermys[i]
                  i-= 1
            i += 1
            

      pygame.display.update()

