# POKEMON ATTACK EFFICACY CALCULATOR
# Richard Williams 2016
# Currently outputs type advantages for pokemon go.

import csv
import numpy as np

# Open CSV attack strength chart and create type and comparison arrays
with open('attackchart.csv') as csvfile:
    read_csv = csv.reader(csvfile,delimiter=',')
    master_chart = []

    for row in read_csv:
        master_chart.append(row)

#convert to numpy charts and extract information

master_chart = np.array(master_chart)
attack_type = master_chart[0,1:]
attack_chart = master_chart[1:,1:]

def get_indices(attacker, defender):
    """gets the index for attacker and defender. accepts pokemon types as upper
    case strings and returns as the index number for the attack_chart"""
    for i in range(0,len(attack_type)-1):
        if attacker == attack_type[i]:
            attacker_index = i

        if defender == attack_type[i]:
            defender_index = i

    return attacker_index, defender_index

def get_attack_advantage(attacker_index, defender_index):
    """accepts the index numbers corressponding to the pokemon chart, and returns
    the advantage to the attacker as a fraction"""

    return attack_chart[attacker_index,defender_index]

def get_types():
    """prompt the user to enter the types"""
    
    attacker = input('Attacker: ')
    defender = input('Defender: ')
    return attacker.upper(), defender.upper()

#need to write something to make sure attack type is valid

def print_effectiveness(attack_advantage):
    """Print the Effectiveness of the attac"""
    
    attack_advantage = float(attack_advantage)
    if attack_advantage == 0:
        print('It had no effect')
    elif attack_advantage < 1:
        print('It\'s not very effective')
    elif attack_advantage == 1:
        print('')
    elif attack_advantage > 1:
        print('It\'s super effective!')

#Run Program
print('Pokemon Go Attack Calculator')
print('(c) Richard Williams 2016')
print('')
attacker, defender = get_types()
attacker_index, defender_index = get_indices(attacker,defender)
attack_advantage = get_attack_advantage(attacker_index,defender_index)
print('')
print('Attack Effectiveness: '+str(attack_advantage))
print_effectiveness(attack_advantage)
