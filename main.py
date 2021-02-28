from lib.battleship import Battleship
from lib.utils import *
import time, sys, random

def game_loop(game, automated=False):
  current_attacker = 1
  current_defender = 2
  while True:
    while True:
      if automated:
        location = game.get_random_shot(current_attacker)
        print(f'{current_attacker}: {location}')
      else:
        shots_taken = ', '.join(game.get_shots_taken(current_attacker))
        print(f'Shots taken: {shots_taken}')
        location = get_location(game)
      shot_result = game.shoot(current_attacker, current_defender, location)
      # time.sleep(1)
      if shot_result == 'Sunk':
        print(f'You sunk my battleship. Player {current_attacker} wins')
        quit()
      elif not shot_result:
        print('Shot already taken')
      else:
        print(shot_result)
        # time.sleep(1)
        break
    current_attacker = 2 if current_attacker == 1 else 1
    current_defender = 2 if current_defender == 1 else 1

def main():
  game = Battleship()
  
  size = get_board_size()
  game.generate_board(size)
  
  for player in range(1,3): # exclusive
    location = get_location(game)
    direction = get_direction()
    game.place_ship(player, location, direction)

  game_loop(game)

def automated_main():
  game = Battleship()
  board_size = random.randrange(5, 100)
  print(board_size)
  game.generate_board(board_size)
  
  directions = ['vertical', 'horizontal']

  player_one_shot = game.get_random_shot(1)
  player_one_direction = random.choice(directions)
  print(f'Player one ship location: {player_one_shot}, {player_one_direction}')
  game.place_ship(1, player_one_shot, player_one_direction)
  
  player_two_shot = game.get_random_shot(2)
  player_two_direction = random.choice(directions)
  print(f'Player two ship location: {player_two_shot}, {player_two_direction}')
  game.place_ship(2, player_two_shot, player_two_direction)

  game_loop(game, True)

if __name__ == "__main__":
  if len(sys.argv) > 1: # add extra arg to command to run in auto
    automated_main()
  else:
    main()