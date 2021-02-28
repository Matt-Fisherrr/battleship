from lib.utils import *
from lib.battleship import Battleship

def test_get_board_size(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: 6)
  assert get_board_size(2) == 6
  monkeypatch.setattr('builtins.input', lambda _: 7)
  assert get_board_size(2) == 7
  monkeypatch.setattr('builtins.input', lambda _: 'F')
  assert get_board_size(2) == False

def test_get_location(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: '6d')
  game = Battleship()
  game.generate_board(10)
  assert get_location(game, 2) == '6d'
  monkeypatch.setattr('builtins.input', lambda _: '16g')
  game.generate_board(20)
  assert get_location(game, 2) == '16g'
  monkeypatch.setattr('builtins.input', lambda _: 'none')
  game.generate_board(20)
  assert get_location(game, 2) == False

def test_get_direction(monkeypatch):
  monkeypatch.setattr('builtins.input', lambda _: 'vertical')
  assert get_direction(2) == 'vertical'
  monkeypatch.setattr('builtins.input', lambda _: 'horizontal')
  assert get_direction(2) == 'horizontal'
  monkeypatch.setattr('builtins.input', lambda _: 'Sideways')
  assert get_direction(2) == False

def teardown_method(self, method):
  module.input = input