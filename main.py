import pygame
import sys
import random
import time

class Surf:

    

    def __init__(self, x, y, id):

        self.x = x
        self.y = y
        self.id = id
        self.drawn = False
        self.yes = False
    

        self.surf = pygame.Surface((70, 70))
        pygame.draw.rect(self.surf, WHITE, (0, 0, 65, 65), 8)
        self.rect = self.surf.get_rect(x = self.x, y =self. y)
        



    def draw(self, sc):
        sc.blit(self.surf, self.rect)


    def get(self):
        return self.x, self.y

    def check(self):
        mouse = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()
        
        
        if self.x < mouse[0] < (self.x + 10) + 40:
            if self.y < mouse[1] < (self.y + 10) + 40:
                if pressed[0]:
                    pygame.draw.line(self.surf, WHITE, [15, 15], [45, 45], 4)
                    pygame.draw.line(self.surf, WHITE, [45, 15], [15, 45], 4)
                    self.drawn = True
                    #pygame.draw.circle(self.surf, WHITE, (33, 33), 20, 4)


    def auto(self):
        pygame.draw.circle(self.surf, WHITE, (33, 33), 20, 4)
        self.drawn = True
        self.yes = True


    def ex(self):
        pygame.draw.line(self.surf, WHITE, [15, 15], [45, 45], 4)
        pygame.draw.line(self.surf, WHITE, [45, 15], [15, 45], 4)
        drawn = True
        print("Ok2")


# Colors
YELLOW = (238, 217, 176)
RED = (240, 0, 0)
BLUE = (0, 0, 240)
GREEN = (0, 240, 0)
WHITE = (255, 255, 255)

# Size

WIDTH = 600
HEIGHT = 400


#FPS

FPS = 60




clock = pygame.time.Clock()

# Create Window

sc = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Крестики-Нолики')


s = Surf(200, 100, 1)
s2 = Surf(260, 100, 2)
s3 = Surf(260+60, 100, 3)

s4 = Surf(200, 160, 4)
s5 = Surf(260, 160, 5)
s6 = Surf(260+60, 160, 6)

s7 = Surf(200, 220, 7)
s8 = Surf(260, 220, 8)
s9 = Surf(260+60, 220, 9)

lst = [s, s2, s3, s4, s5, s6, s7, s8, s9]

nums  = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# main cycle
while True:

    for i in pygame.event.get():

        if i.type == pygame.QUIT:
            sys.exit()

        if i.type == pygame.MOUSEBUTTONDOWN:
            if nums:
                if i.button == 1:
                    x, y = i.pos
                    print(x, y)
                    for index, b in enumerate(lst):
                        if lst[0].yes and lst[1].yes and lst[2].yes:
                            print("Work!")
                            pygame.draw.line(sc, WHITE, [20, 100], [320, 10660], 4)
                        x1, y1 = b.get()
                        if x1 < x < x1 + 60:
                            if y1 < y < y1 + 60:
                                b.auto()
                                nums.remove(index)

        if i.type == pygame.MOUSEBUTTONUP:
            if nums:

                time.sleep(1)
                if i.button == 1:
                    for n in range(1, 100):
                        r = random.choice(nums)
                        nums.remove(r)
                        if not lst[r].drawn:
                            lst[r].ex()
                            print(f"n = {n}, r = {r}")
                            break
                        elif lst[r].drawn:
                            continue

    
    

    sc.fill((10, 10, 10))
    
    s.draw(sc)
    s2.draw(sc)
    s3.draw(sc)
    s4.draw(sc)
    s5.draw(sc)
    s6.draw(sc)
    s7.draw(sc)
    s8.draw(sc)
    s9.draw(sc)
    clock.tick(60)
    pygame.display.update()