import Unit_Stats
import Rooms



def selectedUnit(tank, mage, damage_dealer, range):

   loop_unit_selection = True;
   damage_dealer_use = True;
   tank_use = True;
   mage_use = True;
   range_use = True;

   while True:

    print('')
    selectedUnit = raw_input(
           'It is now your turn. What unit would you like to use? : ' + tank + ', ' + mage + ', ' + damage_dealer + ', ' + range)

    #If player selects warpriest

    if (selectedUnit == 'Warpriest' and damage_dealer_use == False):
        print('')
        print('You must wait for the next turn to use this unit')

    if(selectedUnit == 'Warpriest' and damage_dealer_use == True):

        damage_dealer_use = False;

        print('')
        print('You have selected the ' + selectedUnit)

        Unit_Stats.display_warpriest_abilities()

        print('')
        selected_ability = raw_input('Which ability would you like to use? : ')

        if(selected_ability == 'Heal'):

          print('')
          print('The Warpriest uses Heal')

        elif (selected_ability == 'For Sigmar!'):
            print('')
            print('The Warpriest uses For Sigmar!')

        elif (selected_ability == 'Hammer Strike'):
            print('')
            print('The Warpriest uses Hammer Strike')

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

        if (selected_ability == 'Cnarge'):

            print('')
            print('The Foot Knight uses Charge')

        elif (selected_ability == 'Heavy Sword Swing'):
            print('')
            print('The Foot Knight uses For Sigmar!')

        elif (selected_ability == 'Shield'):
            print('')
            print('The Foot Knight uses Shield')
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

    print(range_use)
    print(tank_use)
    print(mage_use)
    print(damage_dealer_use)

    #if all units have been used, end the turn
    if(range_use == False and tank_use == False and mage_use == False and damage_dealer_use == False):

        break
        print(range_use)
        print(tank_use)
        print(mage_use)
        print(damage_dealer_use)
        Rooms.warband_turn = False;
        loop_unit_selection = False;
