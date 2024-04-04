#insert coins by pressing spacebar or clicking the coin slot
#start the round by pressing enter or clicking the red handle
#reset game by pressing r

#author: Tiina Mannelin

import pygame
import random
import math

class Slot:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Slots")
        self.money = 20
        self.bet = 0
        self.housewin = 0
        self.row = [0,1,2]
        self.handle = False
        self.roll = False
        self.display = pygame.display.set_mode((700, 700))
        self.gameover = False

        self.loadImages()
        self.loop()
    
    def updateView(self):
        self.display.fill((0,0,0))
        #draw slot machine
        pygame.draw.rect(self.display, (255, 0, 0), (55, 225, 50, 60))
        pygame.draw.rect(self.display, (250, 200, 0), (100, 100, 490, 270))
        pygame.draw.rect(self.display, (250, 200, 0), (70, 370, 550, 300))
        pygame.draw.rect(self.display, (255, 255, 255), (110, 400, 470, 230))
        pygame.draw.rect(self.display, (250, 200, 0), (60, 230, 40, 50))
        pygame.draw.rect(self.display, (0, 0, 0), (75, 240, 5, 25))
        pygame.draw.rect(self.display, (250, 200, 0), (590, 250, 40, 30))
        pygame.draw.rect(self.display, (255, 255, 255), (140, 140, 100, 100))
        pygame.draw.rect(self.display, (255, 255, 255), (290, 140, 100, 100))
        pygame.draw.rect(self.display, (255, 255, 255), (440, 140, 100, 100))
        pygame.draw.rect(self.display, (255, 255, 255), (265, 300, 150, 40))
        #slot machine handle graphic
        if self.handle:
            pygame.draw.rect(self.display, (250, 200, 0), (630, 250, 30, 200))
            pygame.draw.circle(self.display, (255, 0, 0), (645, 450), 25)
        else:
            pygame.draw.rect(self.display, (250, 200, 0), (630, 80, 30, 200))
            pygame.draw.circle(self.display, (255, 0, 0), (645, 80), 25)
        #fruits to slots
        if not self.roll:
            self.display.blit(self.images[self.row[0]], (145, 150))
            self.display.blit(self.images[self.row[1]], (295, 150))
            self.display.blit(self.images[self.row[2]], (445, 150))
        else:
            #roll effect
            pygame.draw.line(self.display, (0, 0, 0), (170, 170), (170, 220), 2)
            pygame.draw.line(self.display, (0, 0, 0), (190, 165), (190, 225), 2)
            pygame.draw.line(self.display, (0, 0, 0), (210, 170), (210, 220), 2)

            pygame.draw.line(self.display, (0, 0, 0), (320, 170), (320, 220), 2)
            pygame.draw.line(self.display, (0, 0, 0), (340, 165), (340, 225), 2)
            pygame.draw.line(self.display, (0, 0, 0), (360, 170), (360, 220), 2)

            pygame.draw.line(self.display, (0, 0, 0), (470, 170), (470, 220), 2)
            pygame.draw.line(self.display, (0, 0, 0), (490, 165), (490, 225), 2)
            pygame.draw.line(self.display, (0, 0, 0), (510, 170), (510, 220), 2)
        #money texts
        myfont = pygame.font.SysFont("Arial", 30)
        mytext = myfont.render(f"wallet: {self.money}€", True, (10, 250, 50))
        self.display.blit(mytext, (100, 50))
        myfont = pygame.font.SysFont("Arial", 30)
        mytext = myfont.render(f"bet: {self.bet}€", True, (0,0,0))
        self.display.blit(mytext, (280, 300))
        
        if self.gameover:
            #game over message when user has run out of money
            myfont = pygame.font.SysFont("Arial", 50)
            mytext = myfont.render(f"Game Over", True, (250, 0, 0))
            self.display.blit(mytext, (220, 450))
            myfont = pygame.font.SysFont("Arial", 35)
            mytext = myfont.render(f"You splurged {self.housewin}€", True, (250, 0, 0))
            self.display.blit(mytext, (215, 510))
        elif self.money > 200:
            #congratulatory message when user has won a lot of money
            myfont = pygame.font.SysFont("Arial", 50)
            mytext = myfont.render(f"Yay you're rich!", True, (0, 250, 0))
            self.display.blit(mytext, (180, 450))
            myfont = pygame.font.SysFont("Arial", 35)
            mytext = myfont.render(f"You invested {self.housewin}€", True, (0, 250, 0))
            self.display.blit(mytext, (215, 510))
        else:
            #winlist
            myfont = pygame.font.SysFont("Arial", 30)
            #x3
            mytext = myfont.render(f"{self.bet * 7}€", True, (0,0,0))
            self.display.blit(mytext, (290, 430))
            mytext = myfont.render(f"{self.bet * 5}€", True, (0,0,0))
            self.display.blit(mytext, (290, 470))
            mytext = myfont.render(f"{self.bet * 3}€", True, (0,0,0))
            self.display.blit(mytext, (290, 510))
            mytext = myfont.render(f"{self.bet * 2}€", True, (0,0,0))
            self.display.blit(mytext, (290, 550))
            #x2
            mytext = myfont.render(f"{math.floor(self.bet * 2.5)}€", True, (0,0,0))
            self.display.blit(mytext, (490, 430))
            mytext = myfont.render(f"{self.bet}€", True, (0,0,0))
            self.display.blit(mytext, (490, 470))
            mytext = myfont.render(f"{math.floor(self.bet/2)}€", True, (0,0,0))
            self.display.blit(mytext, (490, 510))
            mytext = myfont.render(f"{math.floor(self.bet/3)}€", True, (0,0,0))
            self.display.blit(mytext, (490, 550))
            #image thumbnails
            xs = [160,200,240,400,440]
            ys = [430,470,513,550]
            for y in range(len(self.thumbnails)):
                for x in xs:
                    self.display.blit(self.thumbnails[y], (x, ys[y]))

        pygame.display.flip()

    def loadImages(self):
        self.images = []
        self.thumbnails = []
        for nimi in ["cherry","orange","watermelon","lemon"]:
            self.images.append(pygame.image.load(nimi + ".png"))
            self.thumbnails.append(pygame.image.load(nimi + ".png"))
            self.thumbnails[-1] = pygame.transform.scale(self.thumbnails[-1], (0.4*self.thumbnails[-1].get_width(), 0.4*self.thumbnails[-1].get_height()))

    def round(self):
        if self.bet <1:
            #no bet placed
            return
        self.housewin += self.bet
        nextrow = []
        for i in range(0,3):
            nextrow.append(random.randint(0,len(self.images)-1))
        self.row = nextrow
        if len(set(nextrow)) ==1:
            #x3
            match nextrow[0]:
                case 0:
                    self.money += self.bet * 7
                case 1:
                    self.money += self.bet * 5
                case 2:
                    self.money += self.bet * 3
                case 3:
                    self.money += self.bet * 2
        elif len(set(nextrow)) ==2:
            #x2
            if nextrow.count(nextrow[0]) == 2:
                m = nextrow[0]
            else:
                m = nextrow[1]
            match m:
                case 0:
                    self.money += math.floor(self.bet * 2.5)
                case 1:
                    self.money += self.bet
                case 2:
                    self.money += math.floor(self.bet/2)
                case 3:
                    self.money += math.floor(self.bet/3)
        self.bet = 0
        if self.money == 0:
            self.gameover = True
    
    def pull(self):
        self.handle = True
        if self.bet > 0:
            self.roll = True
            pygame.time.set_timer(pygame.USEREVENT, 3000, True)
        else:
            pygame.time.set_timer(pygame.USEREVENT, 120, True)
    
    def insert(self):
        if self.money > 0 and not self.handle:
            self.money -= 1
            self.bet += 1

    def loop(self):
        myclock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT:
                    self.handle = False
                    self.roll = False
                    self.round()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 610 < event.pos[0] < 670 and 50 < event.pos[1] < 110:
                        self.pull()
                    if 55 < event.pos[0] < 100 and 225 < event.pos[1] < 285:
                        self.insert()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    if event.key == pygame.K_RETURN:
                        self.pull()
                    if event.key == pygame.K_SPACE:
                        self.insert()
                    if event.key == pygame.K_r:
                        self.__init__()
                if event.type == pygame.QUIT:
                    exit()
            self.updateView()
            myclock.tick(60)

if __name__ == "__main__":
    Slot()
