import re

def get_board_size(retries=0): # retries used only to exit during testing of function
  while True:
    try:
      return int(input('Please enter size of board axes\n'))
    except:
      print('Input error, please enter a number')
      retries -= 1
      if retries == 0:
        return False


def get_location(game, retries=0): # retries used only to exit during testing of function
  while True:
    x_range = f'{game.x_axis[0]}-{game.x_axis[-1]}'
    y_range = f'{game.y_axis[0]}-{game.y_axis[-1]}'
    location = input(f'Please enter center location of ship, as a number and letter\nex: 3d\nwithin ranges:\n x: {x_range}\n y: {y_range}\n')
    if re.match(r'\d+\D+', location):
      return location
    else:
      print('Input error, please enter a number and letter')
      retries -= 1
      if retries == 0:
        return False

def get_direction(retries=0): # retries used only to exit during testing of function
  while True:
    direction = input('Please enter which direction the ship should face\nvertical or horizontal\n').lower()
    if direction == 'vertical' or direction == 'horizontal':
      return direction
    else:
      print('Input error, please enter vertical or horizontal')
      retries -= 1
      if retries == 0:
        return False