import Unit_Stats

Vargheist_stats = [45, 0, 15, 1400]
Vargheist_abilities = ['Claw Strike', 'Sky Pound', 'Wing Wipe']

Vargheist_health = Vargheist_stats[3]
Vargheist_dmg = Vargheist_stats[0]
Vargheist_range = Vargheist_stats[1]
Vargheist_armor = Vargheist_stats[2]


def display_Boss_Stat():

   print('The Vargheist damage is at ' + str(Vargheist_dmg))
   print('The Vargheist range is at ' + str(Vargheist_range))
   print('The Vargheist armor is at ' + str(Vargheist_armor))
   print('The Vargheist health is at ' + str(Vargheist_health))

def clawStrike (claw_strike):

  print('')
  print('The Vargheist strikes a direct hit with its claw')

  Unit_Stats.warband_health[0] -= claw_strike
  Unit_Stats.warband_health[1] -= claw_strike
  Unit_Stats.warband_health[2] -= claw_strike
  Unit_Stats.warband_health[3] -= claw_strike

def wingSwipe(nearby_unit_one, nearby_unit_two):

    if(nearby_unit_one == "Warpriest"):

      Unit_Stats.warpriest_health -= 20
      print(Unit_Stats.warpriest_health)


    if(nearby_unit_two == "Foot Knight"):

      Unit_Stats.footknight_health -= 20
      print(Unit_Stats.footknight_health)
