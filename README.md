README for Assignment10.1.py

Class:
My class, Soldier, represents a soldier. The soldier is equipped with a basic sword. The soldier has a private damage and a private health variable.
It allows for an attack against a target dummy, to set 

Variables:
The sword is stored in a class variable named weapon_in_hand.
Two data variables exist, self.__damage, and self.__health, which represent the damage the soldiers attacks do and the health of the soldier respectively.

Methods: (When talking about arguments, I exclude self.)
The __init__ method defines the data variables, its much too simple for 2 sentences.
The set_health method sets the health of the soldier. It does not return anything. An int value is required as an input.
The get_health method finds the value of the soldiers health. The value is then returned. No arguments are taken.
The attack method prompts the player their weapin is being readied, then attacks and returns the amount of damage dealt baesd on the self.__damage data variable. There is a 1/5 chance of the attack missing and returning 0 damage. It does not take any input.
The victory_scream method increases the damage the soldier deals by 10. It does not return anything. No arguments are taken.

Demo program:
The demo program is a RPG-type simulation of a soldier fighting a dummy. The player is expected to enter a command, viewable by typing 'help', to fight against a target dummy.
Although the dummy does not attack back, the player can use one of the given commands, 'set hp', to set their health to or below 0, killing the soldier.
Once either the soldier or dummy dies, the game ends.

To run the program, please cd to its directory and run it via python. No additional packages are required.
