empire_unit_stats = [

    ['95', '0', '45', '450', 'Heal', 'For Sigmar!', 'Hammer Strike'],
    ['45', '20', '10', '320', 'Fireball', 'Flamethrower', 'Flaming sword'],
    ['80', '15', '18', '250', 'Silver Bullet', 'Axe Strike', 'Bleeding Strike'],
    ['78', '0', '30', '440', 'Charge', 'Heavy Sword Swing', 'Shield']

]

#warband health
warpriest_health = int(empire_unit_stats[0][3])
brightwizard_health = int(empire_unit_stats[1][3])
witchhunter_health = int(empire_unit_stats[2][3])
footknight_health = int(empire_unit_stats[3][3])

warband_health = [warpriest_health, brightwizard_health, witchhunter_health, footknight_health]

#warband damage
warpriest_dmg = int(empire_unit_stats[0][0])
brightwizard_dmg = int(empire_unit_stats[1][0])
witchhunter_dmg = int(empire_unit_stats[2][0])
footknight_dmg = int(empire_unit_stats[3][0])


def heal_warband():

  print(warpriest_health)
  print(brightwizard_health)
  print(witchhunter_health)
  print(footknight_health)

def display_warband_health():


  print('The Warpriest has ' + str(warband_health[0]) + ' hp')
  print('The Bright Wizard has ' + str(warband_health[1]) + ' hp')
  print('The Witchunter has ' + str(warband_health[2]) + ' hp')
  print('The Foot Knight has ' + str(warband_health[3]) + ' hp')

def display_warpriest_abilities():

    print('')
    print('These are the Warpriest abilities: ')
    print('')
    print(empire_unit_stats[0][4] + ' - Heals the entire warband with +40 health')
    print(empire_unit_stats[0][5] + ' - The Warpriest hammer generates holy light dealing double damage')
    print(empire_unit_stats[0][6] + ' - A normal hammer attack dealing default strike')

def display_footknight_abilities():

    print('')
    print('These are the Foot Knight abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[3][4] + ' - Launches a deadly ball of fire dealing massive damage')
    print(empire_unit_stats[3][5] + ' - A lasting flame burning the enemy for 2 turns')
    print(empire_unit_stats[3][6] + ' - Strikes a flaming blade causing damage to enemy armor')

def display_brightwizard_abilities():

    print('')
    print('These are the Bright Wizard abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[1][4] + ' - Charges the enemy and lowers their armor')
    print(empire_unit_stats[1][5] + ' - A charged sword strike')
    print(empire_unit_stats[1][6] + ' - Raises the armor of the selected unit for one turn')

def display_witchhunter_abilities():

    print('')
    print('These are the Witch Hunter abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[2][4] + ' - A special round that penetrates through multiple enemies')
    print(empire_unit_stats[2][5] + ' - A default strike that can ignore 10% armor')
    print(empire_unit_stats[2][6] + ' - A special strike that bleeds enemy health for two turns')

woodelves_unit_stats = [

  [45, 0, 34, 290],
  [25, 0, 40, 310],
  [70, 0, 13, 192],
  [15, 38 , 4, 167],

]




