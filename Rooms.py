import Unit_Stats   #Import player abilities and Unit Statistics
import Player
import Boss_One_Stats
import random
loop_room = True;
loop_turns = False;

warband_turn = True;

warband_turn = False;
boss_turn = False;

#faction units
empire_units = [ 'Warpriest', 'Bright Wizard', 'Witch Hunter', 'Foot Knight']
woodelves_units = ['Dryad', 'Eternal Guard', 'Wildwood Ranger', 'Waystalker']

#Roome one
def RoomOne(tank, range, mage, damager_dealer):

  while loop_room:

      #Display scenario
      print('')
      print(' Your warband has entered Mordheim: The City of The Damned. An Ostermarkian Town befelled by a Warpstone comet. The once prosperous city' )
      print(' is now tainted with the horrors of the Vampire Counts. Crypt horrors, Terrorghast, and other unnamed horrors now wander the abandoned streets.')
      print(' As your warband enters the city, they can hear a rumbling nearby down an alley. It is a Vargheist, a giant bat like creature of pale skin and of crimson hair.')
      print(' This specific vargheist has ravaged the area ripping through any warband it encounters. Its been damaged but is in a blood thirsty rage.')
      print('')
      print(' Near you is a house with a balcony and the alley containing cover.')
      print('')
      print(' Your Warband has entered the house. Each one of them quickly gets into position to strike the foul beast. The ' + tank + ' and ' + ' the ' + damager_dealer)
      print(' jump off the balcony dealing extra damage and stunning the foe. The ' + range + ' and ' + mage + ' begin to fire. But now the enemy has become berzerk')
      print(' increasing damage.')
      print('')

      loop_turns = True;

      #ambush dmg boost
      Boss_One_Stats.Vargheist_health -= ((Unit_Stats.footknight_dmg + 10) + (Unit_Stats.warpriest_dmg + 10))
      Boss_One_Stats.Vargheist_dmg *= 2

      boss_turn = True;

      #After turn, begin turn system
      while loop_turns:

         #If it is the bosses turn
         if(boss_turn == True):

           boss_turn = False;
           warband_turn = True;

           print('')
           print('It is the bosses turn')

           Boss_One_Stats.display_Boss_Stat()

           random_ability = random.randint(0, 3)

           #determine the boss ability randomly
           if(random_ability == 0):

               print('')
               print('The Vargheist uses Claw Strike')

               Boss_One_Stats.clawStrike(Boss_One_Stats.Vargheist_dmg)
               Boss_One_Stats.Vargheist_dmg = 45

           elif (random_ability == 1):
               print('')

               print('The Vargheist flaps its wings and slams to the ground stunning nearby units for one turn')
               Boss_One_Stats.ground_stun(empire_units[0], empire_units[3])

           elif (random_ability == 2):

               print('')
               print('The Vargheist sweeps the nearby area causing penetrated damage to nearby units')

               Boss_One_Stats.wingSwipe(empire_units[0], empire_units[3]);

           #If boss dies exist game
           if(Boss_One_Stats.Vargheist_health == 0):

               print('')
               print('Through persistence and with the blessing of Sigmar, the warband destroys ths taint; beridding Mordheim of another horror. But the battle is not yet won,')
               print('A warp asteroid storm befalls upon the outskirts of the city and with it, hordes of Skaven have arrived alongside with Middenland forces to claim the power.')
               print('This battle is not yet to be won. Sigmar save us all...')

         #If it is the warband turn, choose what to do with units
         elif(warband_turn == True):

             Unit_Stats.display_warband_health()

             #Call unit ability selection method
             Player.selectedUnit(tank, mage, range, damager_dealer);
             warband_turn = False;
             boss_turn = True;
             print('It works')

         else:

             print('No one gets a turn')