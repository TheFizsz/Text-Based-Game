import Unit_Stats
import Rooms
import Boss_One_Stats
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

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_warpriest_abilities()

        #check what abilities is selected
        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        #Perform appropriate method to selected ability
        if(selected_ability == 'Heal'):



          if(Unit_Stats.heal_use > 0):

              damage_dealer_use = False;
              Unit_Stats.heal_use -= 1;
              print('')
              print('The Warpriest heals the entire warband with a 25 hp bonus')
              print('')
              print('You now have ' + str(Unit_Stats.heal_use) + ' uses left')

              Unit_Stats.footknight_health += Unit_Stats.health_boost
              Unit_Stats.warpriest_health += Unit_Stats.health_boost
              Unit_Stats.witchhunter_health += Unit_Stats.health_boost
              Unit_Stats.brightwizard_health += Unit_Stats.health_boost

          elif( Unit_Stats.heal_use < 0):

              Unit_Stats.heal_use = 0;
              print('You are out of heal boosts')

        elif (selected_ability == 'For Sigmar!'):

          Unit_Stats.dmg_boost_use

          if (Unit_Stats.dmg_boost_use > 0):

             Unit_Stats.damage_dealer_use = False;
             Unit_Stats.dmg_boost_use -= 1
             print('')
             print('The Warpriest uses For Sigmar! giving all units in Melee a 10 dmg boost')
             print('')
             print('You now have ' + str(Unit_Stats.dmg_boost_use) + ' uses left')

             Unit_Stats.witchhunter_dmg += Unit_Stats.dmg_boost
             Unit_Stats.footknight_dmg  += Unit_Stats.dmg_boost
             Unit_Stats.warpriest_dmg  += Unit_Stats.dmg_boost
             Unit_Stats.brightwizard_dmg += Unit_Stats.dmg_boost

          elif(dmg_boost_use < 0):

              damage_dealer_use = True;
              print('')
              print('You are out of damagee boosts')

        elif(selected_ability == 'Hammer Strike'):

            damage_dealer_use = False;
            print('')
            print('The Warpriest uses Hammer Strike dealing 95 dmg')
            Unit_Stats.hammer_strike()

     #Disable selection for unit once selected again in the same turn
     if(selectedUnit == 'Warpriest' and damage_dealer_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

    #If player selects foot knight
     if (selectedUnit == 'Foot Knight' and tank_use):

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_footknight_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Charge'):

            if(Unit_Stats.charge > 0):

              Unit_Stats.charge -= 0;
              tank_use = False;
              print('')
              print('The Foot Knight charges the Vargheist lowering its defense for one turn')
              #Create method

            elif(Unit_Stats.charge < 0):

              print('')
              print('You are out of charges')

        elif (selected_ability == 'Heavy Sword Swing'):

            tank_use = False;
            print('')
            print('The Foot Knight strikes the beast with his blade dealing 78 dmg')
            Unit_Stats.sword_swing()

        elif (selected_ability == 'Shield'):

            #use up shield turn
            if(Unit_Stats.shield_turn == 1):

                tank_use = False;
                Unit_Stats.shield_turn -= 1;
                Unit_Stats.footknight_defense += 12 #boost knight defense
                print('')
                print('The Foot Knight raises his shield giving a 12 armor boost for one turn')
                print('')
                print('You can no longer use this ability until the next game')

            if (Unit_Stats.shield_turn < 0):

                Unit_Stats.footknight_defense -= 12 #reset knight defense
                tank_use = True;
                print('')
                print('You are out of shield boosts')
                shield_turn = 0;


     elif (selectedUnit == 'Foot Knight' and tank_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

     if (selectedUnit == 'Bright Wizard' and mage_use == True):

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_brightwizard_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Fireball'):

            print('')
            print('The Bright Wizard uses Fireball')

            #Call fireball dmg method
            Unit_Stats.fire_ball()

            mage_use = False;

        elif (selected_ability == 'Flamethrower'):

            if(Unit_Stats.flame_thrower_turns > 0):

                Unit_Stats.flame_thrower_turns -= 1;
                print('')
                print('The Bright Wizard uses Flamethrower dealing 9 damage for 3 turns')
                mage_use = False;

                Boss_One_Stats.Vargheist_health -= Unit_Stats.flame_thrower_damage;

            elif(Unit_Stats.flame_thrower_turns < 0):

                Unit_Stats.flame_thrower_turns = 0;
                print('')
                print('You can no longer use this abiltiy until the next turn')

        elif (selected_ability == 'Flaming Sword'):
            print('')
            print('The Bright Wizard uses Flaming Sword lowering the armor of the beast')

     elif (selectedUnit == 'Bright Wizard' and mage_use == False):

        print('')
        print('You must wait for the next turn to use this unit')

     if (selectedUnit == 'Witch Hunter' and range_use):

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_witchhunter_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if (selected_ability == 'Silver Bullet'):

            if(Unit_Stats.silver_ammo > 0):

                Unit_Stats.silver_ammo -= 1;

                print('')
                print('The Witch Hunter uses Silver Bullet dealing 40 dmg to health ignoring armor')
                print('')
                print('You now have ' + str(Unit_Stats.silver_ammo) + ' bullets left')

                range_use = False;

            elif(Unit_Stats.silver_ammo < 0):

                range_use = True;
                Unit_Stats.silver_ammo = 0;

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
    





