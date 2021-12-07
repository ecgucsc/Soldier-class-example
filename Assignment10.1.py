# Edward Gentry // Assignment 10.1: Your Own Class
# An RPG-like simlation class demonstration


import random
import time

# THIS CLASS CREATES A DUMMY AND IS ONLY USED SO THE OTHER CLASS MAKES SENSE, PLEASE DO NOT GRADE THIS CLASS.
class Dummy():
    # Define the type of enemy
    enemy_type = "Dummy"
    def __init__(self):
        # Define the stats of the enemy
        self.__health = 100

    # Takes health away from the character
    def take_damage(self, amount):
        self.__health -= amount
        print(f"{self.enemy_type} took {amount} damage!")

    def get_health(self):
        return self.__health



# A class for a soldier (The actual class for the assignment)
class Soldier():
    # Define the type of weapon the soldier has (Class variable)
    weapon_in_hand = "Sword"
    # Class methods
    def __init__(self):
        # Define the stats of the soldier
        self.__damage = 30
        self.__health = 100


                        ## SET / GET METHODS ##
    # sets the health
    def set_health(self, amount):
        self.__health = amount
        print(f"Your health has been set to {amount}!")

    # Get the health
    def get_health(self):
        return self.__health
    

                        ## 2 OTHER METHODS
    # Ready and perform an attack
    def attack(self):
        # Alert the user
        print(f"You ready your {self.weapon_in_hand}...")
        time.sleep(1)
        # Determins weather or not the attack will hit determined by accuracy; 0 accuracy always misses 
        __hit = random.randint(1,5) != 1

        if __hit:
            # Hits and returns the damage
            print(f"Your {self.weapon_in_hand} hit, dealing {self.__damage} damage!")
            return self.__damage
        else:
            # Misses and returns 0 damage
            print(f"But your {self.weapon_in_hand} missed...")
            return 0

    # Scream for victory, increasing the soldier's damage by 10
    def victory_scream(self):
        self.__damage += 10
        print(f"You begin screaming for victory!")
        print(f"ATK increased by 10!")

    
# Main function
def main():
    # Create classes
    player = Soldier()
    dummy = Dummy()

    # Welcome
    print("Welcome to Assignment 10.1 RPG!")

    # Prompt loop
    while True:
        if dummy.get_health() > 0 and player.get_health() > 0:
            # If the dummy isnt dead ask them for a command
            action = input("What action would you like to perform? Type 'help' for actions! ").lower()

            # Commands
            if action == "help":    # list all commands
                print("""'help', Brings up this text.
'attack' Attacks the target dummy.
'view hp' Views your current hp.
'set hp' Promps you to set your current health.
'victory scream' Scream for victory, increasing your attack forever.""")
            elif action == "attack":    # Attacks the dummy.
                # Performs an attack then deals the damage to the dummy
                damage_dealt = player.attack()
                dummy.take_damage(damage_dealt)
            elif action == "view hp":   # views the players own HP
                print(f"You have {player.get_health()} health!")
            elif action == "set hp":    # sets the players own HP
                hp_to_set = None
                try:
                    hp_to_set = int(input("What hp would you like to set your character to?"))
                except:
                    print("Please enter a valid int.")
                    return
                player.set_health(hp_to_set)
            elif action == "victory scream":    # Increases the players attack
                player.victory_scream()
            else:   # Incorrect command
                print("Unknown action, try again.")
        else:
            # Game over, the dummys hp was less than or equal to 0
            print("Game over!")
            break





if __name__ == "__main__":
    main()