import Unit_Stats
import Rooms
import sys

def selectedUnit(tank, mage, damage_dealer, range):

   damage_dealer_use = True;
   tank_use = True;
   mage_use = True;
   range_use = True;
   loop_unit_selection = True;

   while loop_unit_selection:

     print('')
     selectedUnit = raw_input('It is now your turn. What unit would you like to use? : ' + tank + ', ' + mage + ', ' + damage_dealer + ', ' + range)

     #If player selects warpriest

     if(selectedUnit == 'Warpriest' and damage_dealer_use == True):

        damage_dealer_use = False;

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_warpriest_abilities()

        #check what abilities is selected
        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        #Perform appropriate method to selected ability
        if(selected_ability == 'Heal'):

          heal_use = 3

          if(heal_use > 0):

              heal_use -= 1;
              print('')
              print('The Warpriest heals the entire warband with a 25 hp bonus')
              print('')
              print('You now have ' + str(heal_use) + ' uses left')
              Unit_Stats.heal_warband(Unit_Stats.brightwizard_health, Unit_Stats.footknight_health,
                                      Unit_Stats.witchhunter_health, Unit_Stats.warpriest_health)

          elif( heal_use == 0):

              heal_use = 0;


        elif (selected_ability == 'For Sigmar!'):

          print('')
          print('The Warpriest uses For Sigmar! giving all units in Melee a 10 dmg boost')
          Unit_Stats.for_sigmar(Unit_Stats.brightwizard_health, Unit_Stats.footknight_health,
                                  Unit_Stats.witchhunter_health, Unit_Stats.warpriest_health)


        elif (selected_ability == 'Hammer Strike'):
            print('')
            print('The Warpriest uses Hammer Strike dealing 95 dmg')
            Unit_Stats.hammer_strike()

     #Disable selection for unit once selected again in the same turn
     if(selectedUnit == 'Warpriest' and damage_dealer_use == False):

        print('')
        print('You must wait for the next turn to use this unit')


    #If player selects foot knight
     if (selectedUnit == 'Foot Knight' and tank_use):

        tank_use = False;

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_footknight_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Charge'):

            print('')
            print('The Foot Knight charges the Vargheist lowering its defense for one turn')


        elif (selected_ability == 'Heavy Sword Swing'):

            print('')
            print('The Foot Knight strikes the beast with his blade dealing 78 dmg')
            Unit_Stats.sword_swing()

        elif (selected_ability == 'Shield'):

            shield_turn = 1;
            print('')
            print('The Foot Knight raises his shield giving a 12 armor boost for one turn')

            #use up shield turn
            if(shield_turn == 1):

                shield_turn -= 1;
                print('')
                print('You can no longer use this ability until the next game')

            elif (shield_turn < 1):

                shield_turn = 0;


     elif (selectedUnit == 'Foot Knight' and tank_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

     if (selectedUnit == 'Bright Wizard' and mage_use == True):

        mage_use = False;

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_brightwizard_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Fireball'):

            print('')
            print('The Bright Wizard uses Fireball')

        elif (selected_ability == 'Flamethrower'):

            print('')
            print('The Bright Wizard uses Flamethrower')

        elif (selected_ability == 'Flaming Sword'):
            print('')
            print('The Bright Wizard uses Flaming Sword')

     elif (selectedUnit == 'Bright Wizard' and mage_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

     if (selectedUnit == 'Witch Hunter' and range_use):

        range_use = False;

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_witchhunter_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Silver Bullet'):

            print('')
            print('The Witch Hunter uses Silver Bullet')

        elif (selected_ability == 'Axe Strike'):
            print('')
            print('The Witch Hunter uses Axe Strike')

        elif (selected_ability == 'Hammer Strike'):
            print('')
            print('The Witch Hunter uses Bleeding Strike')

     elif (selectedUnit == 'Witch Hunter' and range_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

     print('')
     print('Witch Hunter: ' + str(range_use))
     print('Foot Knight: ' + str(tank_use))
     print('Bright Wizard: ' + str(mage_use))
     print('War Priest: ' + str(damage_dealer_use))

     #if all units have been used, end the turn
     if(range_use == False and tank_use == False and mage_use == False and damage_dealer_use == False):

        raw_input('This is working')
        break
        print( 'Witch Hunter: ' + str(range_use))
        print( 'War Priest: ' + str(tank_use))
        print( 'Bright Wizard: ' + str(mage_use))
        print( 'Foot Knight: ' + str(damage_dealer_use))
        Rooms.boss_turn = True;
        Rooms.warband_turn = False;
        loop_unit_selection = False;

     else:

        print('This is not working')
    





