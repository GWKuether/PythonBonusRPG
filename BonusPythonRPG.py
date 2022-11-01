import random


Hercules = {'Name': "Hercules", 'Health': 100, 'Attack Power': 50, 'Attacks': ['Punch', 'Kick', 'Tackle', 'Trample']}

Gremlin_1 = {'Health': 20, 'Attack Power': 5, 'Attacks': ['Bite', 'Hiss', 'Scratch']}

Gremlin_2 = {'Health': 20, 'Attack Power': 5, 'Attacks': ['Bite', 'Hiss', 'Scratch']}

Dragon = {'Health': 200, 'Attack Power': 25, 'Attacks': ['Breathe Fire', 'Tail Slap' 'Slash']}


print(Hercules['Attacks'][2])

gremlin_1_attack = random.choice(Gremlin_1['Attacks'])

gremlin_2_attack = random.choice(Gremlin_1['Attacks'])

print(gremlin_1_attack)

print(gremlin_2_attack)




def choose_hercules_attack(enemy):
    attack_chosen = False
    while attack_chosen == False:
        attack_choice = input(f"Which attack should Hercules use? {Hercules['Attacks'][0]}, {Hercules['Attacks'][1]}, {Hercules['Attacks'][2]}, or {Hercules['Attacks'][3]}? ")
        if attack_choice == Hercules['Attacks'][0]:
            print(f"Hercules used his giant hand to punch the {enemy}.")
            attack_chosen = True
        elif attack_choice == Hercules['Attacks'][1]:
            print(f"Hercules wound up his leg and kicked the {enemy}.")
            attack_chosen = True
        elif attack_choice == Hercules['Attacks'][2]:
            print(f"Hercules flew into the air and tackled the {enemy}.")
            attack_chosen = True
        elif attack_choice == Hercules['Attacks'][3]:
            print(f"Hercules lifted his boots and trampled the {enemy}.")
            attack_chosen = True



choose_hercules_attack("Dragon")


def run_game():
    pass

def fight(initiator, receiver):
    pass