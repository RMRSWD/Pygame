import pygame
import random 
from pygame import mixer 
class Bird:
    def __int__(self):
        pygame.int() #Init pygame 
        self.xScreen, self.yScreen = 500, 600 #Screen create 
        linkBackGroud = './Data/background.png' 
        self.linkImgBird = "./Data/bird.png"
        self.screen = pygame.display.set_mode(
            (self.xScreen, self.yScreen)) #Initiliser la taille d'écran
        pygame.display.set_caption("Code Learn - Flappybird -DV")
        self.background = pygame.image.load(linkBackGroud)
        self.gamerunning = True 
        icon = pygame.image.load(self.linkImgBird)
        pygame.display.set_icon(icon)
        #----------------------------------------------------------
        #étabir la configuration de bird
        self.xSizeBird = 80 #hauteur bird
        self.ySizeBird = 60 #largeur bird 
        self.xBird = self.xScreen/3 #position par défaut de bird
        self.yBird = self.yScreen/2
        self.VBirdUp = 70 # vitess sauté de bird
        self.VBirdDown = 7 # vitess tombé de bird 
        #----------------------------------------------------------
        #établir la configuration de la colonne
        self.xColunm = self.yScreen + 250 # Initialiser le premier colonne 
        self.yColunm = 0
        self.xSizeColunm = 100 # large de la colonne
        self.ySizeColunm = self.yScreen 
        self.Vcolunm = 6 # vitess marché de la colonne 
        self.colunmChange = 0 

        self.score = 0
        self.checkLost = False 
        #----------------------------------------------------------------
    def music(self,url): #activer le son
        bulletSound = mixer.Sound(url)
        bulletSound.play()
        #----------------------------------------------------------------
    def image_draw(self,url, xLocal, yLocal, xImg, yImg): # Imprimer l'image
        PlanesImg = pygame.image.load(url)
        PlanesImg = pygame.transform.scale(
            PlanesImg, (xImg,yImg)) # changer la taille d'image 
        self.screen.blit(PlanesImg, (xLocal, yLocal))
        #----------------------------------------------------------------
    def show_score(self, x, y, scores, size): # Afficher la note
        font = pygame.font.SysFont('comicsansms', size)
        score = font.render(str(scores), True, (255, 255, 255))
        self.screen.blit(score,(x, y))
        #----------------------------------------------------------------
    def colunm(self):
        maginColunm = 80 
        yColunmChangeTop = -self.ySizeColunm/2 - maginColunm + \
            self.colunmChange # la distance de colonne en haut et colonne en bas est 80*2
        yColunmChangeBotton = self.ySizeColunm/2 + maginColunm + self.colunmChange
        self.image_draw('.Data/colunm.png', self.xColunm,yColunmChangeTop, self.xSizeColunm, self.ySizeColunm)
        self.image_draw('./Data/colunm.png', self.xColunm, yColunmChangeBotton, self.xSizeColunm, self.ySizeColunm)
        self.xColunm = self.xColunm - self.Vcolunm
        if self.xColunm < -100: # si la colonne passe l'écran
            self.xColunm = self.xScreen # créer une nouvelle colonne 
            # random la distance entre les colonnes
            self.colunmChange = random.randint(-150, 150)
            self.score += 1
        return yColunmChangeTop + self.ySizeColunm, yColunmChangeBotton #retourner la position de deux colonnes 

    def run(self):
        while self.gamerunning:
            self.screen.blit(self.background, (0,0)) 
            for event in pygame.event.get(): #prendre des événements 
                #print(event)
                if event.type == pygame.QUIT: #appuyer la quittée
                    self.gamerunning = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.yBird -= self.VBirdUp # bird atterir
                    self.music('.Data/swoosh.wav')
                if event.type == pygame.KEYDOWN: # les événement ont des appuyées bas 
                    if event.key == pygame.K_SPACE:
                        self.yBird -= self.VBirdUp # bird atterir
                        self.music('.Data/swoosh.wav')
            self.yBird += self.VBirdDown # bird décoller/tomber
            ycolunmChangeTop, yColunmChangeBotton = self.colunm()
            #print(self.yBird, yColunmChangeTop, self.yBird + self.ySizeBird, yColunmChangeBotton)
            #------------Vérifier bird touche à la colonne?---------------
            if self.yBird < ycolunmChangeTop and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True 
            if self.yBird+self.ySizeBird > yColunmChangeBotton and (self.xColunm+self.xSizeColunm - 5 > self.xBird+self.xSizeBird > self.xColunm + 5 or self.xColunm+self.xSizeColunm > self.xBird > self.xColunm):
                self.checkLost = True
            # vérifier bird a touché le tuyeau
            if (self.yBird + self.ySizeBird > self.yScreen) or self.yBird < 0:
                self.yBird = self.yScreen/2
                self.checkLost = True 
            self.Vcolunm = 6 if self.scores < 1 else 6 + self.scores/5 # la vitess progesse 
            self.VBirdDown = 7 if self.scores < 1 else 7 + self.scores/10  # bird tombe plus vite selon le temps
            print(self.Vcolunm)
            while (self.checkLost): # si bird touche un objet 
                self.xColunm = self.xScreeen + 100
                for event in pygame.event.get(): # si appuyer
                    if event.type == pygame.Quit: # quitter
                        self.gamerunning = False 
                        self.checkLost = False
                        break 
                    if event.type == pygame.KEYDOWN: # quitter
                        self.checkLost = False
                        self.scores = 0
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.checkLost == False 
                        self.score = 0
                self.show_score(100, 100, "Scores:{}".format(self.scores), 40) #imprimer la note
                self.show_score(self.xScreen/2-100, self.yScreen/2-100,"Game Over", 50) # imprimer Loss
                self.Vcolunm = 6
                self.VBirdDown = 7
                pygame.display.update()
            self.image_draw(self.linkImgBird, self.xBird, self.yBird, self.xSizeBird, self.ySizeBird)
            self.show_score(self.xScreen-200, 20, "DucVu ^_^!!", 15)
            self.show_score(10, 10, "Score:{}".format(self.scores), 35)
            pygame.display.update() #Update 
            clock = pygame.time.Clock()
            clock.tick(80)
def main(): 
    bird = Bird()
    bird.run()





    






