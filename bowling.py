from logging import raiseExceptions

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if len(self.frames) >= 10:
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self.frames):
            raise BowlingError
        return self.frames[i]

    def calculate_score(self) -> int:
        sum_score = 0
        for element, i in enumerate(self.frames):
            if i.is_strike() and element != len(self.frames)-1:
                sum_score += i.score()
                j = element + 1
                while self.frames[j].is_strike() and j < len(self.frames):
                    sum_score += self.frames[j].get_first_throw() + self.frames[j].get_second_throw()
                    j += 1
                if j == element + 1:
                    sum_score += self.frames[j].get_first_throw() + self.frames[j].get_second_throw()
                elif j != element + 1 and j < len(self.frames):
                    sum_score += self.frames[j].get_first_throw()

            elif i.is_spare() and element != len(self.frames)-1:
                sum_score += i.score() + self.frames[element+1].get_first_throw()
            else:
                sum_score += i.score()

        return sum_score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
