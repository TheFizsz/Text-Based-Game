import Rooms #Import rooms


#faction options
warhammer_factions = ['The Empire']

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

            print('')
            print('You will play as ' + warhammer_factions[0])
            print('')
            print_warband(empire_units)
            Rooms.RoomOne(empire_units[3], empire_units[2],empire_units[1], empire_units[0])



  elif(ask_user_start == 'N'):

    print('')
    print('Au Revoir!')


  else:

    print('')
    print('Response was invalid. Please try again')