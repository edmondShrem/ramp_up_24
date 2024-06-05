import Area_of_a_Triangle_Very_Easy
import RETURN_NEXT_VERY_EASY
import THE_SNAKE_HARD
import INVERT_COLORS_EASY
import IMAGINARY_CODING_INTERVIEW_HARD
import LENGTH_OF_NUMBER_MEDIUM
import FIND_THE_DISCOUNT_EASY

import unittest

class Test_Challenges_unittest(unittest.TestCase):
    def test_Tri(self):
        self.assertEqual(Area_of_a_Triangle_Very_Easy.tri_area(10,3), 15)
    def next_num_test(self):
        self.assertEqual(RETURN_NEXT_VERY_EASY.return_next(6), 7)
    def profit_test(self):
        