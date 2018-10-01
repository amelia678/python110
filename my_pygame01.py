import pygame
import time 
from random import randint

class Monster:
    def __init__(self, monster_x, monster_y):
        self.monster_x = monster_x
        self.monster_y = monster_y
        self.speed_x = 5
        self.speed_y = 5
    
class Hero:
    def __init__(self, hero_x, hero_y):
        self.hero_x = hero_x
        self.hero_y = hero_y
        self.speed_x = 3
        self.speed_y = 3
    
   
  

def main():
    width = 510
    height = 475
    # blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()
    monster_x = 100
    monster_y = 100
    hero_x = 225
    hero_y = 225
    # change_dir_countdown = 120
   
    

    # Game initialization
    # monster = Monster(100,100)
    
  
 
    
    
    stop_game = False
    while not stop_game:
        for event in pygame.event.get():
            

            # # Event handlings
            if event.type == pygame.KEYDOWN:
                if event.key == KEY_DOWN:
                    hero.y += 3
                elif event.key == KEY_UP:
                    hero.y -= 3
                elif event.key == KEY_LEFT:
                    hero.x -= 3
                elif event.key == KEY_RIGHT:
                    hero.x += 3
            

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        monster_y = monster_y - 5 
        if monster_y < 0:
            monster_y = 475
        if monster_x > 510:
            monster_x = 0 
        
        # change_dir_countdown = change_dir_countdown - 1
        # if change_dir_countdown == 0:
        #     change_dir_countdown = 120
        #     direction_change = randint(0,3)
        #     if direction_change == 0:
        #         monster.speed_y -= 5
        #     elif direction_change == 1:
        #         monster.speed_x += 5
        #     elif direction_change == 2:
        #         monster.speed_y += 5
        #     elif direction_change == 3:
        #         monster.speed_x -= 5



        # Draw background
        
        background_image = pygame.image.load('background.png').convert_alpha()
        hero_1 = pygame.image.load('hero.png').convert_alpha()
        monster = pygame.image.load('monster.png').convert_alpha()
        
        
        



        # Game display

        pygame.display.update()
        clock.tick(60)
        screen.blit(background_image, (0,0))
        screen.blit(hero_1, (hero_x, hero_y))
        screen.blit(monster, (monster_x, monster_y))
        

        
        

    pygame.quit()

if __name__ == '__main__':
    main()
