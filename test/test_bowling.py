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

    def test_game_created_11_frames(self):
        self.game.add_frame(Frame(1, 5))
        self.game.add_frame(Frame(2, 5))
        self.game.add_frame(Frame(1, 1))
        self.game.add_frame(Frame(4, 2))
        self.game.add_frame(Frame(8, 0))
        self.game.add_frame(Frame(2, 3))
        self.game.add_frame(Frame(1, 3))
        self.game.add_frame(Frame(1, 6))
        self.game.add_frame(Frame(2, 0))
        self.game.add_frame(Frame(10, 0))
        self.assertRaises(BowlingError, self.game.add_frame, Frame(1,1))