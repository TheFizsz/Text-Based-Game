import Unit_Stats   #Import player abilities and Unit Statistics
import Player

loop_room = True;
loop_turns = False;

warband_turn = True;

warband_turn = False;
boss_turn = False;

initial_moves = ['a: Move into the house and take position for an ambush', 'b: Wait in the alley and take on the beast']

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

      #Ask user what first move to make
      initial_move_one = raw_input('What would you like to do: ' + str(initial_moves))

      loop_turns = True;

      #If move a is selected, attack Vargheist
      if(initial_move_one == 'a'):

          Unit_Stats.Vargheist_health -= ((Unit_Stats.footknight_dmg + 10) + (Unit_Stats.warpriest_dmg + 10))
          Unit_Stats.Vargheist_dmg *= 2

          print('')
          print(' You have selected ' + initial_moves[0])
          print('')
          print(' Your Warband has entered the house. Each one of them quickly gets into position to strike the foul beast. The ' + tank + ' and ' + ' the ' + damager_dealer)
          print(' jump off the balcony dealing extra damage and stunning the foe. The ' + range + ' and ' + mage + ' begin to fire. But now the enemy has become berzerk')
          print(' increasing damage.')
          print('')
          Unit_Stats.display_Boss_Stat()
          boss_turn = True;

      #If move b is selected, then do this
      elif(initial_move_one == 'b'):

          print('')
          #Unit_Stats.heal_warband()

      #After turn, begin turn system
      while loop_turns:

         #If it is the bosses turn
         if(boss_turn == True):

           Unit_Stats.clawStrike(Unit_Stats.Vargheist_dmg)
           Unit_Stats.Vargheist_dmg = 45

           print('')
           print(Unit_Stats.display_warband_health())
           boss_turn = False;
           warband_turn = True;

         #If it is the warband turn, choose what to do with units
         elif(warband_turn == True):

             #Call unit ability selection method
             Player.selectedUnit(tank, mage, range, damager_dealer);