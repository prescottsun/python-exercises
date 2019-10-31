hotel = {
  '1': {
    '101': ['George Jefferson', 'Wheezy Jefferson'],
  },
  '2': {
    '237': ['Jack Torrance', 'Wendy Torrance'],
  },
  '3': {
    '333': ['Neo', 'Trinity', 'Morpheus']
  }
}

print('''
Menu:
1. Check in
2. Check out
''')

menu_choice = input('Enter number of your selection: ')
floor_number = input('Enter a floor number: ')
room_number = input('Enter a room number: ')

if menu_choice == '1':
    if floor_number not in hotel:
        hotel[floor_number] = {}
        
    if room_number not in hotel[floor_number]:

        occupants = input('Number of occupants? ')
        names = input('Names of occupants?' )
        split_names = names.split(', ', int(occupants)-1)

        hotel[floor_number][room_number] = split_names
    else:
        print('Room is already occupied')


elif menu_choice == '2':
    try:
        hotel[floor_number][room_number]
    except KeyError:
        print('Cannot check out. Room is not occupied')
    else:
        del hotel[floor_number][room_number]

print(hotel)