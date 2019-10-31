"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Character:
    def __init__(self, health, power, name):
        self.health = health
        self.power = power
        self.name = name
        

    def alive(self):
        if self.health > 0:
            return True

    def attack(self, enemy):
        enemy.health -= self.power
        print("%s does %d damage to the %s." % (self.name, self.power, enemy.name))
        if enemy.alive() != True:
            print("The %s is dead." %(enemy.name))
    
    def print_status(self):
        print("%s has %d health and %d power." % (self.name, self.health, self.power))

class Hero(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("You do %d damage to the goblin." % self.power)
    #     if enemy.health <= 0:
    #         print("The goblin is dead.")

    # def alive(self):
    #     if self.health > 0:
    #         return True

    # def print_status(self):
    #     print("You have %d health and %d power." % (hero.health, hero.power))

class Goblin(Character):
    def __init__(self, health, power, name):
       super().__init__(health, power, name)

    # def attack(self, enemy):
    #     enemy.health -= self.power
    #     print("The goblin does %d damage to you." % self.power)

    # def alive(self):
    #     if self.health > 0:
    #         return True

    # def print_status(self):
    #     print("The goblin has %d health and %d power." % (goblin.health, goblin.power))

class Zombie(Character):
    def __init__(self, health, power, name):
        super().__init__(health, power, name)
        self.health = 999

    def alive(self):
        return True

hero = Hero(10, 5, 'hero')
enemy = Zombie(6, 2, 'zombie')


def main():
#     hero.health = 10
#     hero.power = 5
#     goblin.health = 6
#     goblin.power = 2

    while enemy.alive() and hero.alive():
        hero.print_status()
        enemy.print_status()
        print()
        print("What do you want to do?")
        print("1. fight enemy")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
            hero.attack(enemy)
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if enemy.health > 0:
            # Goblin attacks hero
            enemy.attack(hero)
            # if hero.health <= 0:
            #     print("You are dead.")

main()
