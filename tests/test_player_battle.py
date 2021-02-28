from lib.battleship import Battleship
import re

def test_shoot():
  game = Battleship()

  game.generate_board(10)

  game.place_ship(1, '2d', 'vertical')
  game.place_ship(2, '5h', 'horizontal')

  assert game.shoot(1, 2, '8b') == 'Miss'
  assert game.shoot(1, 2, '8b') == False
  assert game.shoot(1, 2, '6h') == 'Hit'

def test_get_shots_taken():
  game = Battleship()

  game.generate_board(10)

  game.place_ship(1, '2d', 'vertical')
  game.place_ship(2, '5h', 'horizontal')

  assert game.shoot(1, 2, '8b') == 'Miss'
  assert game.get_shots_taken(1) == ['8b']
  assert game.shoot(1, 2, '9g') == 'Miss'
  assert game.get_shots_taken(1) == ['8b', '9g']
  assert game.shoot(1, 2, '8h') == 'Miss'
  assert game.get_shots_taken(1) == ['8b', '9g', '8h']
  assert game.shoot(1, 2, '1e') == 'Miss'
  assert game.get_shots_taken(1) == ['8b', '9g', '8h', '1e']

def test_random_shot():
  game = Battleship()

  game.generate_board(10)

  # Check a random shot is in the correct format and is in the axis choices
  shot = game.get_random_shot(1)
  assert re.match(r'\d+\D+', shot)
  letter = re.findall(r'\D+', shot)[0]
  number = int(re.findall(r'\d+', shot)[0])
  assert letter in game.y_axis
  assert number in game.x_axis

  shot = game.get_random_shot(2)
  assert re.match(r'\d+\D+', shot)
  letter = re.findall(r'\D+', shot)[0]
  number = int(re.findall(r'\d+', shot)[0])
  assert letter in game.y_axis
  assert number in game.x_axis

def test_game():
  game = Battleship()

  game.generate_board(10)

  game.place_ship(1, '2d', 'vertical')
  game.place_ship(2, '5h', 'horizontal')

  assert game.shoot(1, 2, '8b') == 'Miss'
  assert game.shoot(2, 1, '3g') == 'Miss'
  assert game.shoot(1, 2, '9g') == 'Miss'
  assert game.shoot(2, 1, '8c') == 'Miss'
  assert game.shoot(1, 2, '6h') == 'Hit'
  assert game.shoot(2, 1, '5i') == 'Miss'
  assert game.shoot(1, 2, '8h') == 'Miss'
  assert game.shoot(2, 1, '7e') == 'Miss'
  assert game.shoot(1, 2, '9g') == False
  assert game.shoot(2, 1, '2i') == 'Miss'
  assert game.shoot(1, 2, '1e') == 'Miss'
  assert game.shoot(2, 1, '1d') == 'Miss'
  assert game.shoot(1, 2, '5h') == 'Hit'
  assert game.shoot(2, 1, '4e') == 'Miss'
  assert game.shoot(1, 2, '4h') == 'Sunk'
