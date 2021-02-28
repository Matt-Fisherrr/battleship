from lib.battleship import Battleship

def test_generate_board():
  game = Battleship()

  assert game.generate_board(-1) == True
  assert game.generate_board('F') == False
  assert game.generate_board(10) == True
  assert game.generate_board(7) == True

  game.generate_board(5)
  assert game.x_axis == [1, 2, 3, 4, 5]
  assert game.y_axis == ['a', 'b', 'c', 'd', 'e']

  game.generate_board(10)
  assert game.x_axis == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  assert game.y_axis == ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def test_place_ships():
  game = Battleship()

  game.generate_board(10)

  game.place_ship(1, '2d', 'vertical')
  game.place_ship(2, '5h', 'horizontal')
  assert game.players[1]['ship_location'] == ['2c', '2d', '2e']
  assert game.players[2]['ship_location'] == ['4h', '5h', '6h']

  game.place_ship(1, '6a', 'vertical')
  game.place_ship(2, '1h', 'horizontal')
  assert game.players[1]['ship_location'] == ['6c', '6a', '6b']
  assert game.players[2]['ship_location'] == ['3h', '1h', '2h']

  game.place_ship(1, '6j', 'vertical')
  game.place_ship(2, '10h', 'horizontal')
  assert game.players[1]['ship_location'] == ['6i', '6j', '6h']
  assert game.players[2]['ship_location'] == ['9h', '10h', '8h']
