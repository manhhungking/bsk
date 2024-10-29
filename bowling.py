from logging import raiseExceptions

from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
        self.bonus_first = 0
        self.bonus_second = 0
    
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
            if i.is_strike():
                sum_score += i.score()
                if element == len(self.frames)-1:
                    sum_score += self.bonus_first + self.bonus_second
                    break
                j = element + 1
                while j < len(self.frames) and self.frames[j].is_strike():
                    sum_score += self.frames[j].get_first_throw() + self.frames[j].get_second_throw()
                    j += 1
                    break
                if j == element + 1 and j < len(self.frames):
                    sum_score += self.frames[j].get_first_throw() + self.frames[j].get_second_throw()
                elif j != element + 1 and j < len(self.frames):
                    sum_score += self.frames[j].get_first_throw()
                elif j == len(self.frames):
                    sum_score += self.frames[j % int(len(self.frames))].get_first_throw()

            elif i.is_spare() and element != len(self.frames)-1:
                sum_score += i.score() + self.frames[element+1].get_first_throw()
            else:
                sum_score += i.score()

        return sum_score

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        self.bonus_first = bonus_throw

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        self.bonus_second = bonus_throw
