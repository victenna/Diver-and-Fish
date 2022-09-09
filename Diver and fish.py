import pygame,random,os
pygame.init()
screen = pygame.display.set_mode((1000, 600))
screen.fill('blue')
clock = pygame.time.Clock()

class Aquarium():
    def __init__(self):
        super().__init__()
        self.aquarium = []
        for i in range(20):
            image=pygame.image.load(os.path.join("Aq_images",str(i)+'.gif'))
            self.aquarium.append(pygame.transform.scale(image, (1000, 600)))
        self.image = self.aquarium[0]
        self.rect = self.image.get_rect(center=(500,300))
        self.count = 0
        self.c = 0
    def update(self):
        self.c += 1
        if self.c%20==0:
          self.c =0
        self.image = self.aquarium[self.c]
    def draw(self):
        screen.blit(self.image, self.rect)
aquarium = Aquarium()

class Man():
    def __init__(self):
        super().__init__()
        self.man= []
        for i in range(23):
            image=pygame.image.load(os.path.join("Man_images",'man'+str(i)+'.gif'))
            self.man.append(pygame.transform.scale(image, (300, 200)))
        self.image = self.man[0]
        self.x=200
        self.rect = self.image.get_rect(center=(self.x,500))
        self.count = 0
        self.c = 0
    def update(self):
        self.c += 1
        if self.c%23==0:
          self.c =0
        self.image = self.man[self.c]
        self.x=self.x+5
        if self.x>1100:
            self.x=20
        self.rect=self.image.get_rect(center=(self.x,500))
    def draw(self):
        screen.blit(self.image, self.rect)
man = Man()

class Fish(pygame.sprite.Sprite):
    def __init__(self,image,x,y,dx,dy):
        super().__init__()
        self.image=pygame.image.load(os.path.join("Fish_images",image))
        self.image=pygame.transform.scale(self.image,(65,50))
        self.x=x
        self.y=y
        self.rect=self.image.get_rect(center=(self.x,self.y))
        self.dx=dx
        self.dy=dy
    def update(self):
        self.x=self.x+self.dx
        self.y=self.y+self.dy
        if self.x>950 or self.x<50:
            self.dx=-1*self.dx
            self.image=pygame.transform.flip(self.image,True,False)
        if self.y<50 or self.y>550:
            self.dy=-1*self.dy
        self.rect=self.image.get_rect(center=(self.x,self.y))
    
    def draw(self):
        screen.blit(self.image,self.rect)
fishes=pygame.sprite.Group()

for i in range(10):
    a=random.randint(100,500)
    b=random.randint(100,500)
    if i<5:
        c=random.randint(5,15)
        d=random.randint(2,10)
    else:
        c=-random.randint(5,15)
        d=-random.randint(2,10)
    fishes.add(Fish('f'+str(i+1)+'.png',a,b,c,d))
while True:
    screen.fill('blue')
    aquarium.update()
    aquarium.draw()
    man.update()
    man.draw()
    fishes.update()
    fishes.draw(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(10)
    pygame.display.update()
