import Boss_One_Stats
import Rooms

empire_unit_stats = [

    ['95', '0', '45', '450', 'Heal', 'For Sigmar!', 'Hammer Strike'],
    ['45', '20', '10', '320', 'Fireball', 'Flamethrower', 'Flaming sword'],
    ['80', '15', '18', '250', 'Silver Bullet', 'Axe Strike', 'Bleeding Strike'],
    ['78', '0', '30', '440', 'Charge', 'Heavy Sword Swing', 'Shield']

]

#Warpriest ability stats
heal_use = 3
health_boost = 25
dmg_boost_use = 3;
dmg_boost = 10

#foot knight ability stats
shield_turn = 1;
charge = 1;

#witch hunter ability stats
silver_ammo = 4;
bleeding_turn = 3;
bleeding_dmg = 20;

#bright wizard abilitiy stats
flame_thrower_turns = 3
flame_thrower_damage = 9
flame_thrower_initial_damage = 15
fireball_dmg = 62;

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

#warband defense
warpriest_defense = int(empire_unit_stats[0][2])
brightwizard_defense = int(empire_unit_stats[1][2])
witchhunter_defense = int(empire_unit_stats[2][2])
footknight_defense = int(empire_unit_stats[3][2])

def Charge():

  Rooms.boss_turn = False;

def hammer_strike():

    hammer_dmg = warpriest_dmg
    Boss_One_Stats.Vargheist_health -= hammer_dmg;

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

def fire_ball():

    fireball = fireball_dmg;
    Boss_One_Stats.Vargheist_health -= fireball;

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


def silver_shot():

    Boss_One_Stats.Vargheist_health -= 40

def axe_strike():

    Boss_One_Stats.Vargheist_health -= witchhunter_dmg

def axe_strike():

    Boss_One_Stats.Vargheist_health -= witchhunter_dmg


woodelves_unit_stats = [

  [45, 0, 34, 290],
  [25, 0, 40, 310],
  [70, 0, 13, 192],
  [15, 38 , 4, 167],

]




