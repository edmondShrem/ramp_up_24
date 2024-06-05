import Area_of_a_Triangle_Very_Easy
import RETURN_NEXT_VERY_EASY
import THE_SNAKE_HARD
import INVERT_COLORS_EASY
import IMAGINARY_CODING_INTERVIEW_HARD
import LENGTH_OF_NUMBER_MEDIUM
import FIND_THE_DISCOUNT_EASY
import CALCULATE_PROFIT_MEDIUM

import unittest

class Test_Challenges_unittest(unittest.TestCase):
    def test_Tri(self):
        self.assertEqual(Area_of_a_Triangle_Very_Easy.tri_area(10,3), 15)
    def test_next_num_test(self):
        self.assertEqual(RETURN_NEXT_VERY_EASY.return_next(6), 7)
    def test_profit_test(self):
        self.assertEqual(CALCULATE_PROFIT_MEDIUM.profit({
  "cost_price": 32.67,
  "sell_price": 45.00,
  "inventory": 1200
}) , 14796)
                
    def test_len_num_test(self):
        self.assertEqual(LENGTH_OF_NUMBER_MEDIUM.number_length(100),3)
        self.assertEqual(LENGTH_OF_NUMBER_MEDIUM.number_length(16600),5)
    def test_snek_test(self):
        self.assertEqual(THE_SNAKE_HARD.snakefill(3), 3)
        self.assertEqual(THE_SNAKE_HARD.snakefill(6), 5)
    def test_color_test(self):
        self.assertEqual(INVERT_COLORS_EASY.color_invert((255,255,255)), (0,0,0))
        self.assertEqual(INVERT_COLORS_EASY.color_invert((25,2,50)), (230,253,205))
    def test_discount_test(self):
        self.assertEqual(FIND_THE_DISCOUNT_EASY.dis(200, 10), 20)
        self.assertEqual(FIND_THE_DISCOUNT_EASY.dis(200, 60), 120)
    def test_interview_test(self):
        self.assertEqual(IMAGINARY_CODING_INTERVIEW_HARD.interview([5, 5, 10, 10, 15, 15, 20, 20], 120), "qualified")
        self.assertEqual(IMAGINARY_CODING_INTERVIEW_HARD.interview([2, 3, 8, 6, 5, 12, 10, 18], 64), "qualified")
        self.assertEqual(IMAGINARY_CODING_INTERVIEW_HARD.interview([5, 5, 10, 10, 25, 15, 20, 20], 120), "disqualified")
        self.assertEqual(IMAGINARY_CODING_INTERVIEW_HARD.interview([5, 5, 10, 10, 15, 15, 20], 120), "disqualified")
        self.assertEqual(IMAGINARY_CODING_INTERVIEW_HARD.interview([5, 5, 10, 10, 15, 15, 20, 20], 130), "disqualified")

        


        


