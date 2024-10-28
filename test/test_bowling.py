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
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertRaises(BowlingError, self.game.add_frame, Frame(1,1))

    def test_calculate_score(self):
        self.game.add_frame(Frame(1, 5))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(81, self.game.calculate_score())

    def test_spare_game_score(self):
        self.game.add_frame(Frame(1, 9))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(88, self.game.calculate_score())

    def test_spare_game_score_2(self):
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.game.add_frame(Frame(1, 9))
        self.assertEqual(85, self.game.calculate_score())

    def test_strike_game_score(self):
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(94, self.game.calculate_score())

    def test_strike_and_spare_game_score(self):
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(4, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(103, self.game.calculate_score())

    def test_multiple_strikes_game_score(self):
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(10, 0))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(112, self.game.calculate_score())

    def test_multiple_spares_game_score(self):
        self.game.add_frame(Frame(8, 2))
        self.game.add_frame(Frame(5, 5))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        self.game.add_frame(Frame(2, 6))
        self.assertEqual(98, self.game.calculate_score())

    def test_spare_as_the_last_frame_game_score(self):
        self.game.add_frame(Frame(1, 5))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        f = Frame(2, 8)
        f.set_bonus(7)
        self.game.add_frame(f)
        self.assertEqual(90, self.game.calculate_score())

    def test_strike_as_the_last_frame_game_score(self):
        self.game.add_frame(Frame(1, 5))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(7, 2))
        self.game.add_frame(Frame(3, 6))
        self.game.add_frame(Frame(4, 4))
        self.game.add_frame(Frame(5, 3))
        self.game.add_frame(Frame(3, 3))
        self.game.add_frame(Frame(4, 5))
        self.game.add_frame(Frame(8, 1))
        f = Frame(10, 0)
        self.game.add_frame(f)
        self.game.set_first_bonus_throw(7)
        self.game.set_second_bonus_throw(2)
        self.assertEqual(92, self.game.calculate_score())