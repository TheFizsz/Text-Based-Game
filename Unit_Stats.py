import Boss_One_Stats

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


def heal_warband(mage_hp, range_hp, tank_hp, damage_dealer_hp):

  heal_boost = 25

  mage_hp += heal_boost;
  range_hp += heal_boost
  tank_hp += heal_boost
  damage_dealer_hp += heal_boost

def for_sigmar(mage_hp, range_hp, tank_hp, damage_dealer_hp):

    dmg_boost = 10

    mage_hp += dmg_boost;
    range_hp += dmg_boost;
    tank_hp += dmg_boost;
    damage_dealer_hp += dmg_boost;

def hammer_strike():

    hammer_dmg = warpriest_dmg

    Boss_One_Stats.Vargheist_health -= warpriest_dmg;




def display_warband_health():

  print('')
  print('The Warpriest has ' + str(warpriest_health) + ' hp')
  print('The Bright Wizard has ' + str(brightwizard_health) + ' hp')
  print('The Witchunter has ' + str(witchhunter_health) + ' hp')
  print('The Foot Knight has ' + str(footknight_health) + ' hp')

def display_warpriest_abilities():

    print('')
    print('These are the Warpriest abilities: ')
    print('')
    print(empire_unit_stats[0][4] + ' - Heals the entire warband with +25 health except for himself')
    print(empire_unit_stats[0][5] + ' - The Warpriest uses a chant granting extra dmg for the warband')
    print(empire_unit_stats[0][6] + ' - A normal hammer attack dealing default strike')

def display_brightwizard_abilities():

    print('')
    print('These are the Bright Wizard abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[1][4] + ' - Launches a deadly ball of fire dealing massive damage')
    print(empire_unit_stats[1][5] + ' - A lasting flame burning the enemy for 2 turns')
    print(empire_unit_stats[1][6] + ' - Strikes a flaming blade causing damage to enemy armor')


def display_footknight_abilities():

    print('')
    print('These are the Foot Knight abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[3][4] + ' - Charges the enemy and lowers their armor')
    print(empire_unit_stats[3][5] + ' - A charged sword strike')
    print(empire_unit_stats[3][6] + ' - Raises the armor of the selected unit for one turn')

def display_witchhunter_abilities():

    print('')
    print('These are the Witch Hunter abilities: ')
    print('') #Grabs abilities from empire_unit_stats
    print(empire_unit_stats[2][4] + ' - A special round that penetrates through multiple enemies')
    print(empire_unit_stats[2][5] + ' - A default strike that can ignore 10% armor')
    print(empire_unit_stats[2][6] + ' - A special strike that bleeds enemy health for two turns')

def sword_swing():

    sword_dmg = footknight_dmg
    Boss_One_Stats.Vargheist_health -= sword_dmg

woodelves_unit_stats = [

  [45, 0, 34, 290],
  [25, 0, 40, 310],
  [70, 0, 13, 192],
  [15, 38 , 4, 167],

]




