import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def test_game_created(self):
        f = Frame(1, 5)
        self.game.add_frame(f)
        self.assertEqual(f, self.game.get_frame_at(0))

    def test_empty_game(self):
        self.assertRaises(BowlingError, self.game.get_frame_at, 0)

