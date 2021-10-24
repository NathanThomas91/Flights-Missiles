import pygame
import random
pygame.init()
screen = pygame.display.set_mode([900, 600])

sound1 = pygame.mixer.Sound('Laser-Gun.wav')
sound1.set_volume(0.2)

cloud1 = pygame.image.load('cloud_1.png')
cloud2 = pygame.image.load('cloud_2.png')
cloud3 = pygame.image.load('cloud_3.png')
game_over = pygame.image.load('1.png')
game_won = pygame.image.load('win_screen.png')

clock = pygame.time.Clock()

global Flag 
Flag = False

class player(pygame.sprite.Sprite):
    def __init__(self):
        super(player, self).__init__()
        self.img = pygame.image.load('jet_1.png')
        self.rect = self.img.get_rect()
    def update(self, x):
        global rectangle, rectangley
        rectangle = self.rect.centerx
        rectangley = self.rect.centery
        if x[pygame.K_UP]:
            self.rect.move_ip(0, -5)
        elif x[pygame.K_DOWN]:
            self.rect.move_ip(0, 5)
        elif x[pygame.K_RIGHT]:
            self.rect.move_ip(5, 0)
        elif x[pygame.K_LEFT]:
            self.rect.move_ip(-5, 0)
class animaen(pygame.sprite.Sprite):
    def __init__(self):
        super(animaen, self).__init__()
        self.img = pygame.image.load('missile.png')
        self.rect = self.img.get_rect(center = (random.randint(
            600 + 20, 600 + 100 ), random.randint(0 , 600)))
        self.speed = random.randint(1, 20)
    def update(self):
        self.rect.move_ip(-self.speed,0)
        if self.rect.right < 0:
            self.kill()
            
def game_end():
    global Flag
    sound1.stop()
    screen.blit(game_over,(100, 0))
    Flag = True
def check_win():
    if rectangle >= 845:
        screen.blit(game_won,(150, 50))
        global Flag
        Flag = True
def borders():
    global Flag
    if rectangle <= 40:
        game_end()
    if rectangley <= 9:
        game_end()
    if rectangley >= 589:
        game_end()
        
obj = player()
add_animaen = pygame.USEREVENT
pygame.time.set_timer(add_animaen, 1000)
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(obj)

running = True
while running:
    sound1.play()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_end()
                running = False
        if event.type == add_animaen:
            obj1 = animaen()
            obj2 = animaen()
            enemies.add(obj2)
            all_sprites.add(obj2)
            enemies.add(obj1)
            all_sprites.add(obj1)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    abc = pygame.key.get_pressed()
    obj.update(abc)
    enemies.update()
    screen.fill((135,206,235))
    screen.blit(cloud2,(400, 30))
    screen.blit(cloud3,(30, -60))
    screen.blit(cloud1,(600, -30))
    screen.blit(cloud3,(790, -80))
    for x2 in all_sprites:
        screen.blit(x2.img,x2.rect)
    if pygame.sprite.spritecollideany(obj, enemies):
        obj.kill()
        game_end()
        running = False
    if Flag == True:
        running = False
    check_win()
    borders()
    pygame.display.flip()
    clock.tick(30)      
