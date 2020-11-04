import pygame, sys, random, time
from pygame.locals import *

points = 0
mx = 0
my = 0

restart = False

# 적군 class
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
            
      def hit(self,missile):
            return pygame.Rect((self.x,self.y), (101, 100)).collidepoint(missile.x,missile.y)
            
      def off_screen(self):
            return self.y > 640

      def bounce(self):
            if self.x>570 or self.x<0:
                  self.dx = -(self.dx)

# 아군 class
class Forces:
      def __init__(self):
            self.x = 320
            self.y = 574

      def move(self):
            if pressed_keys[K_LEFT] and self.x>0:
                  self.x -= 3
            if pressed_keys[K_RIGHT] and self.x<540:
                  self.x += 3

      def draw(self):
            screen.blit(forces_image, (self.x, self.y))

      def fire(self):
            missiles.append(Missile(self.x+50))

      def boom(self,enermy):
            return (enermy.x+100>forces.x) and (enermy.y+100 > forces.y) and (enermy.x < forces.x+100)

# 미사일 class
class Missile:
      def __init__(self,x):
            self.x = x
            self.y = 574

      def move(self):
            self.y -= 5

      def off_screen(self):
            return self.y < -8
      
      def draw(self):
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            
            pygame.draw.line(screen, (r,g,b),(self.x, self.y), (self.x,self.y+8), 6)

class Button:
      def __init__(self):
            self.x = 250
            self.y = 510
      def click(self):
            return (self.x+150<mx) and (self.y+100 > my) and (self.x < mx+100) 
             # 300이 mx 보다 작고, 610이 my보다 크고,
             
# class 복제            
enermys = []
forces = Forces()
missiles = []
btn = Button()

# 온갖 설정

pygame.init()                    
pygame.display.set_caption("Galaga")
screen = pygame.display.set_mode((640, 650))

myfont = pygame.font.Font(None, 50)

enermy_image = pygame.image.load("enemy.png").convert()
enermy_image.set_colorkey((0,0,0))

forces_image = pygame.image.load("forces.png").convert()
forces_image.set_colorkey((0,0,0))

game_over = pygame.image.load("game-over.png").convert()
restart_btn = pygame.image.load("restart.png").convert()

last_enermy_spawn_time = 0

clock = pygame.time.Clock()

while True:
      clock.tick(60)
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  sys.exit()
            if event.type == KEYDOWN and event.key == K_SPACE:
                  forces.fire()

      pressed_keys = pygame.key.get_pressed()

      pos = pygame.mouse.get_pos()
      mx = pos[0]
      my = pos[1]
      
      if time.time() - last_enermy_spawn_time > 1:
            enermys.append(Enermy())
            last_enermy_spawn_time = time.time()
            
      screen.fill((0, 0, 0))
      forces.move()
      forces.draw()

      # 적군
      i = 0
      while i < len(enermys):   
            enermys[i].move()
            enermys[i].bounce()
            enermys[i].draw()
      
            if enermys[i].off_screen():
                  del enermys[i]
                  i-= 1
            i += 1

      # 미사일
      i = 0
      while i < len(missiles):
            missiles[i].move()
            missiles[i].draw()
            if missiles[i].off_screen():
                  del missiles[i]
                  i-= 1
            i += 1

      # 충돌시      
      i = 0
      while i < len(enermys) :     
            j = 0
            while j < len(missiles):
                  if enermys[i].hit(missiles[j]):
                        del enermys[i]
                        del missiles[j]
                        i -= 1
                        points += 1
                        break
                  j += 1
            i+= 1
      # 끝!!
      
      for enermy in enermys:
            if forces.boom(enermy):
                  print('점수는', points)
                  screen.blit(game_over, (170, 200))
                  screen.blit(restart_btn, (250, 510))
                  while 1:
                        for event in pygame.event.get():
                              if event.type == QUIT:
                                    sys.exit()
                              if event.type == pygame.MOUSEBUTTONDOWN:
                                    if btn.click():
                                          print('ggg')
                                          restart = True

                        if restart:
                              print('hhh')
                              break
                                    
                        pygame.display.update()

            
            if restart:
                  print('111')
                  break

                        
            
      if restart:
            print('222')
            restart = False
            enermys.clear()


                              
                  



     
      
                  
      
      

     

      score_img = myfont.render("Score : " + str(points), True, (255,255,255))
      screen.blit(score_img , (10, 10))
    
      pygame.display.update()
