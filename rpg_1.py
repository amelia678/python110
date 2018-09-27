class Character:
   
    
    def attack(self, enemy):
        # Goblin attacks hero
        enemy.health -= self.power
        print("The goblin does %d damage to you." % self.power)
        if enemy. health <= 0:
            print("You are dead.")
        
    
    def alive(self):
        if self.health > 0 :
            return True
        else:
            return False
    
    

class Hero(Character):
    def __init__(self, hero_health, hero_power):
        self.health = hero_health
        self.power = hero_power
    
    def print_status(self):
        print("You have %d health and %d power." % (self.health, self.power))
    
        
    
    
            
    
    
    
class Goblin(Character): 
    def __init__(self, goblin_health, goblin_power):
        self.health = goblin_health
        self.power = goblin_power
    
    
    def print_status(self):
        print("The goblin has %d health and %d power." % (self.health, self.power))
    
    
    
        






# ""
# In this simple RPG game, the hero fights the goblin. He has the options to:

# 1. fight goblin
# 2. do nothing - in which case the goblin will attack him anyway
# 3. flee

# """

def main():
    hero = Hero(10, 5)
    goblin = Goblin(6, 2)
 

    while goblin.alive() and hero.alive():
        hero.print_status()
        goblin.print_status()
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
           hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.alive():
            # Goblin attacks hero
            goblin.attack(hero)
main()
