
import random
AllPokemon_dict = {
    "Bulbasoar": [60, 40, 0],
    "Bellsprout": [40, 60, 1],
    "Oddish": [50, 50, 2],
    "Charmainder": [25, 70, 3],
    "Ninetails": [30, 50, 4],
    "Ponyta": [40, 60, 5],
    "Squirtle": [80, 30, 6],
    "Psyduck": [70, 40, 7],
    "Polywag": [50, 50, 8]
}
UserName = raw_input("What would you like your name to be?")
ComputerName = raw_input("What would you like your opponent name to be?")
print tuple(AllPokemon_dict.keys())
index = int(raw_input("Input a number for your pokemon:"))
UserPokemon_variable = AllPokemon_dict.keys()[index-1]
UserPokemon = []
UserPokemon.append(UserPokemon_variable)
index = int(raw_input("Input a number of your pokemon:"))
UserPokemon_variable = AllPokemon_dict.keys()[index-1]
UserPokemon.append(UserPokemon_variable)
index = int(raw_input("Input a number of your pokemon:"))
UserPokemon_variable = AllPokemon_dict.keys()[index-1]
UserPokemon.append(UserPokemon_variable)
UserPokemon_dict = {}
for key in UserPokemon:
    if key in AllPokemon_dict:
        value = AllPokemon_dict.get(key)
        UserPokemon_dict[key] = value
    else:
        print "One of your choices is not an available pokemon"
        quit()

fireattacks = {
    "Ember": [60, 100],
    "Fire Punch": [85, 80],
    "Flame Wheel": [70, 90]
}
grassattacks = {
    "Leaf Storm": [130, 90],
    "Mega Drain": [50, 100],
    "Razor Leaf": [55, 95],
}
waterattacks = {
    "Bubble": [40, 100],
    "Hydro Pump": [185, 30],
    "Surf": [70, 90]
}

class Pokemon(object):
    def __init__(self, name, HP, AP):
        self.name = name
        self.HP = HP
        self.AP = AP

    def heal(self, HP):
        self.HP += 20
    '''
    def set_type(self, name):
        if name in FirePokemon:
            self.type = "Fire"
        elif name in WaterPokemon:
            self.type = "Water"
        elif name in GrassPokemon:
            self.type = "Grass"
        else:
            return None
    '''
    def take_damage(self, damage): # damage later in the game is actually the attack function
        if self.HP == 0:
            print "Pokemon", self.name, "is dead"
            UserPokemon_dict.remove(self.name)
            UserPokemon.remove(self.name)
        else:
            self.HP -= self.get_attack_power(self, self.AP)

    def set_attacks(self):
        AttackDict = {
            "Leaf Storm": [130, 90],
            "Mega Drain": [50, 100],
            "Razor Leaf": [55, 95],
            "Ember": [60, 100],
            "Fire Punch": [85, 80],
            "Flame Wheel": [70, 90],
            "Bubble": [40, 100],
            "Hydro Pump": [185, 30],
            "Surf": [70, 90]}
        return AttackDict

    def attack(self, attack_name):
        attackvalue = Pokemon.set_attacks
        attackvalue = attackvalue.get(attack_name)
        return Pokemon.take_damage(attackvalue[0])

    def get_attack_power(self, AP):
        return random.randint(AP-20, AP)

    def get_attacks(self):  # list version of the attack keys.
        if isinstance(self, Fire):
            return fireattacks.keys()
        elif isinstance(self, Water):
            return waterattacks.keys()
        elif isinstance(self, Grass):
            return grassattacks.keys()

    def print_attacks(self):
        if isinstance(self, Fire):
            print fireattacks.keys()
        elif isinstance(self, Water):
            print waterattacks.keys()
        elif isinstance(self, Grass):
            print grassattacks.keys()

    def add_attacks(self, attack_dict):
        self.attack = attack_dict


class Fire(Pokemon):
    def __init__(self, name, HP, AP):
        self.set_type = type
        Pokemon.__init__(self, name, HP, AP)

    def __str__(self, name, HP, AP):
        FireAttributes = [name, HP, AP]
        return str(FireAttributes)

    def set_type(self, type):
        self.type = "Fire"

    def set_attacks(self):
        print fireattacks

    def get_attack_power(self, attack, AP):
        # creating a list of Hits and misses to choose random for accuracy.
        accuracy = []
        while len(accuracy) <= attack[1]:
            accuracy = accuracy.append("hit")
        while len(accuracy) <= 100:
            accuracy = accuracy.append("miss")
        #choosing random
        index = random.randint(0, 99)
        if accuracy[index] == "miss":
            return "attack failed"
        elif accuracy[index] == "hit":
            return random.randint(AP-20, AP)

class Grass(Pokemon):
    def __init__(self, name, HP, AP):
        Pokemon.__init__(self, name, HP, AP)

    def __str__(self, name, HP, AP):
        GrassAttributes = [name, HP, AP]
        return str(GrassAttributes)

    def set_type(self, type):
        self.type = "Grass"

    def set_attacks(self):
        print grassattacks
        attack = raw_input("What attack would you like?")
        attack.get(attack, "Doesn't exist")

    def get_attack_power(self, attack, AP):
        # creating a list of Hits and misses to choose random for accuracy.
        accuracy = []
        while len(accuracy) <= attack[1]:
            accuracy = accuracy.append("hit")
        while len(accuracy) <= 100:
            accuracy = accuracy.append("miss")
        #choosing random
        index = random.randint(0, 99)
        if accuracy[index] == "miss":
            return "attack failed"
        elif accuracy[index] == "hit":
            return random.randint(AP-20, AP)

class Water(Pokemon):
    def __init__(self, name, HP, AP):
        self.set_type = type
        Pokemon.__init__(self, name, HP, AP)

    def __str__(self):
        WaterAttributes = [self.name, self.HP, self.AP]
        return str(WaterAttributes)

    def set_type(self, type):
        self.type = "Water"

    def set_attacks(self):
        print waterattacks
        attack = raw_input("What attack would you like?")
        attack.get(attack, "Doesn't exist")

    def get_attack_power(self, attack, AP):
        # creating a list of Hits and misses to choose random for accuracy.
        accuracy = []
        while len(accuracy) <= attack[1]:
            accuracy = accuracy.append("hit")
        while len(accuracy) <= 100:
            accuracy = accuracy.append("miss")
        #choosing random
        index = random.randint(0, 99)
        if accuracy[index] == "miss":
            return "attack failed"
        elif accuracy[index] == "hit":
            return random.randint(AP-20, AP)

class User(object):
    def __init__(self, name):
        self.name = User
        self.currentpokemon = self.set_active_pokemon

    def switch(self, currentpokemon): # set_pokemon, replacing the current pokemon with a new pokemon of user's choice.
        User.list_pokemon()
        currentpokemon = raw_input("What pokemon would you like to switch to?")
        if currentpokemon in UserPokemon:
            self.currentpokemon = currentpokemon
        elif not(currentpokemon in UserPokemon):
            print "This is not in your chosen list"

    def list_pokemon(self):  # printing all the Still alive Pokemon
        for pokemon in UserPokemon:
            if UserPokemon_dict.get(pokemon)[1] == 0: # if HP is 0
                UserPokemon_dict.delitem(pokemon)
                UserPokemon.remove(pokemon)
        print UserPokemon

    def heal(self, currentpokemon):
        currentpokemonHP = UserPokemon_dict.get(currentpokemon)[0]
        return Pokemon.heal(currentpokemonHP)

    def is_end_game(self):  # checking if all the pokemon the user chose are dead with 0 HP
        counter = 0
        for pokemon in UserPokemon_dict:
            if UserPokemon_dict.get(pokemon)[0] == 0:
                counter += 1
        if counter == 3:
            return True
        else:
            return False

    def print_attacks(self):
        index = AllPokemon_dict.get(self.currentpokemon)[2]
        pokemon = AllPokemon[index]
        return pokemon.print_attacks()

    def attack(self, attack_name):
        print self.name, "is attacking", ComputerName
        return Pokemon.attack(attack_name)

    def set_pokemon(self):
        return UserPokemon

    def set_active_pokemon(self):
        currentPokemon = raw_input("Which Pokemon do you want to use first to attack?")
        while not(currentPokemon in UserPokemon):  # making sure the input is a valid input
            if not(currentPokemon in UserPokemon):
                print "Not one of your three chosen pokemon."
                currentpokemon = raw_input("Which Pokemon do you want to use first to attack?")
        return currentPokemon

class Computer(User):
    def __init__(self, name):
        self.name = ComputerName
        User.__init__(self, name)

    def switch(self, currentPokemon):  # switches to another random pokemon.
        currentPokemonnew = ""
        while currentPokemonnew == currentPokemon: # if same pokemon, re-choose
            currentPokemonnew = random.choice(AllPokemonReal)
        currentPokemon = currentPokemonnew
        return currentPokemon

    def attack(self):
        attack = random.choice(Pokemon.get_attacks())
        print ComputerName, "is attacking", UserName
        return Pokemon.attack(attack)

    def play_turn(self, enemy, currentPokemon): # picks a random action.
        if ComputerPokemon_dict(currentPokemon)[0] == 0:
            Pokemon.switch(currentPokemon)
        else:
            randomaction_list = ["switch", "heal", "attack", "attack", "attack", "attack"]
            action = random.choice(randomaction_list)
            if action == "attack":
                Computer.attack()
            elif action == "heal":
                Pokemon.heal(ComputerPokemon_dict.get(currentPokemon)[0]) # putting the HP parameter from the master list.
            elif action == "switch":
                Computer.switch(currentPokemon)

    def set_pokemon(self):
        counter = 0
        ComputerPokemon_list = []
        while counter <= 2:
            key = random.choice(AllPokemonReal)
            ComputerPokemon_list.append(key)
            counter += 1
        return ComputerPokemon_list

AllPokemon = [Grass("Bulbasoar", 60, 40), Grass("Bellsprout", 40, 60), Grass("Oddish", 50, 50), Fire("Charmainder", 25, 70), Fire("Ninetails", 30, 50), Fire("Ponyta", 40, 60), Water("Squirtle", 80, 30), Water("Psyduck", 70, 40), Water("Polywag", 50, 50)]

ComputerPokemon_dict = {
    "Bulbasoar": [60, 40],
    "Bellsprout": [40, 60],
    "Oddish": [50, 50],
    "Charmainder": [25, 70],
    "Ninetails": [30, 50],
    "Ponyta": [40, 60],
    "Squirtle": [80, 30],
    "Psyduck": [70, 40],
    "Polywag": [50, 50]
}
AllPokemonReal = [["Bulbasoar", 60, 40], ["Bellsprout", 40, 60], ["Oddish", 50, 50], ["Charmainder", 25, 70], ["Ninetails", 30, 50], ["Ponyta", 40, 60], ["Squirtle", 80, 30], ["Psyduck", 70, 40], ["Polywag", 50, 50]]
FirePokemon = [Fire("Charmainder", 25, 70), Fire("Ninetails", 30, 50), Fire("Ponyta", 40, 60)]
GrassPokemon = [Grass("Bulbasoar", 60, 40), Grass("Bellsprout", 40, 60), Grass("Oddish", 50, 50)]
WaterPokemon = [Water("Squirtle", 80, 30), Water("Psyduck", 70, 40), Water("Polywag", 50, 50)]
currentPokemon = User(UserName)# setting the attacking pokemon
currentPokemon = currentPokemon.set_active_pokemon()
is_end_game = User(UserName)
while not(is_end_game.is_end_game()):  # game loop
    pokemon = User(UserName)  # printing the available attacks for
    pokemon.print_attacks()
    currentattack = raw_input("Which attack would you like to use?")
    while not(currentattack in Pokemon.get_attacks()):  # making sure valid input
        if not(currentattack in UserPokemon):
            print "Not one of your three chosen pokemon."
        currentattack = raw_input("Which attack would you like to use?")
    User.attack(currentattack)
    computerattack_name = Computer(ComputerName)