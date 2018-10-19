import Rooms #Import rooms


#faction options
warhammer_factions = ['The Empire','Wood Elves']

#faction units
empire_units = [ 'Warpriest', 'Bright Wizard', 'Witch Hunter', 'Foot Knight']
woodelves_units = ['Dryad', 'Eternal Guard', 'Wildwood Ranger', 'Waystalker']

#display warband
def print_warband(warband):

    print(str(warband))

loop_game = True;

#Start game
while loop_game:

  #ask the user if they want to play
  ask_user_start = raw_input('Welcome to Warhammer Roleplay. Would you like to play? Y/N: ')

  #iF yes
  if(ask_user_start == 'Y'):


    #Ask what faction to play
    print(warhammer_factions)
    selected_faction = raw_input('Parfait! What faction would you like to play?')


    for faction in warhammer_factions:

        #Check selected faction
        if(selected_faction == faction):

            print('You have selected ' + faction)

            #If the empire, start assigned room
            if(faction == 'The Empire'):

                print('')
                print_warband(empire_units)
                Rooms.RoomOne(empire_units[3], empire_units[2],empire_units[1], empire_units[0])

            #If elves start assigned room
            elif(faction == 'Wood Elves'):

                print_warband(woodelves_units)
                print('Here is your warband: ' + str(woodelves_units))


  elif(ask_user_start == 'N'):

    print('')
    print('Au Revoir!')

  else:

    print('')
    print('Response was invalid. Please try again')