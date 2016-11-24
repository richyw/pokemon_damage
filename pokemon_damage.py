import csv
import numpy as np

# Open CSV attack strength chart and create type and comparison arrays
with open('attackchart.csv') as csvfile:
    readCSV = csv.reader(csvfile,delimiter=',')
    master_chart = []

    for row in readCSV:
        master_chart.append(row)

#convert to numpy charts and extract information
master_chart = np.array(master_chart)
attack_type = master_chart[0,1:]
attack_chart = master_chart[1:,1:]

def getIndices(attacker,defender):

    #get index for attacker and defender
    for i in range(0,len(attack_type)-1):
        if attacker == attack_type[i]:
            attacker_index = i
            pass
        else:
            print('Attacker Type Not Found')

        if defender == attack_type[i]:
            defender_index = i
            pass
        else:
            print('Defender Type Not Found')

        return attacker_index, defender_index

def getAttackAdvantage(attacker_index,defender_index):
    return attack_chart[attacker_index,defender_index]

def getTypes():
    attacker = input('Attacker: ')
    defender = input('Defender: ')
    return attacker.upper(), defender.upper()

#Run Program

attacker, defender = getTypes()
attacker_index, defender_index = getIndices(attacker,defender)
attack_advantage = getAttackAdvantage(attacker_index,defender_index)
print(attack_advantage)
