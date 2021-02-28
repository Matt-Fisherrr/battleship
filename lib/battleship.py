import string, re, random

class Battleship():
  players = None
  x_axis = None
  y_axis = None

  def __init__(self):
    self.players = {
      1: {
        'ship_location': [],
        'miss_locations': [],
        'hit_locations': []
      },
      2: {
        'ship_location': [],
        'miss_locations': [],
        'hit_locations': []
      }
    }

    self.x_axis = []
    self.y_axis = []  

  def generate_board(self, size):
    if not isinstance(size, int):
      return False
    # Minimum size of 5
    if size < 5:
      size = 5
    self.x_axis = list(range(1, size + 1))
    self.y_axis = [string.ascii_lowercase[x % 26] * ((x // 26) + 1) for x in range(0, size)] # Multiple letters once you get through the alphabet
    return True

  def place_ship(self, player, location, direction):
    letter = re.findall(r'\D+', location)[0]
    number = int(re.findall(r'\d+', location)[0])

    if direction == 'vertical':
      letter_location = self.y_axis.index(letter)
      # Check and correct if the ship is on the edge of the map
      first_letter = self.y_axis[(letter_location - 1) if letter_location > 0 else (letter_location + 2)]
      third_letter = self.y_axis[(letter_location + 1) if letter_location < (len(self.y_axis) - 1) else (letter_location - 2)]
      self.players[player]['ship_location'] = [
        f'{number}{first_letter}',
        f'{number}{letter}',
        f'{number}{third_letter}'
      ]
    elif direction == 'horizontal':
      # Check and correct if the ship is on the edge of the map
      first_number = (number - 1) if number > 1 else (number + 2)
      third_letter = (number + 1) if number < (len(self.x_axis) - 1) else (number - 2)
      self.players[player]['ship_location'] = [
        f'{first_number}{letter}',
        f'{number}{letter}',
        f'{third_letter}{letter}'
      ]

  def get_shots_taken(self, player):
    return self.players[player]['hit_locations'] + self.players[player]['miss_locations']


  def get_random_shot(self, attacker):
    while True:
      shot = f'{random.choice(self.x_axis)}{random.choice(self.y_axis)}'
      if shot not in self.get_shots_taken(attacker):
        return shot

  def shoot(self, attacker, defender, location):
    if location not in self.get_shots_taken(attacker):
      if location in self.players[defender]['ship_location']:
        self.players[attacker]['hit_locations'].append(location)
        if len(self.players[attacker]['hit_locations']) == 3:
          return 'Sunk'
        return 'Hit'
      else:
        self.players[attacker]['miss_locations'].append(location)
        return 'Miss'
    return False

