from unittest import TestCase

from  yijing.iching import _heads_or_tails, _convert_bitmap_to_int_and_add_offset, _line, predict 

class IChingTests(TestCase):

    def test_heads_or_tails(self):
        self.assertTrue(2 <= _heads_or_tails() <= 3)
        self.assertTrue(2 <= _heads_or_tails() <= 3)
        self.assertTrue(2 <= _heads_or_tails() <= 3)
        self.assertTrue(2 <= _heads_or_tails() <= 3)
        self.assertTrue(2 <= _heads_or_tails() <= 3)

    def test_line(self):
        self.assertTrue(0 <= _line() <= 1)
        self.assertTrue(0 <= _line() <= 1)
        self.assertTrue(0 <= _line() <= 1)
        self.assertTrue(0 <= _line() <= 1)
        self.assertTrue(0 <= _line() <= 1)

    def test_bit_conversion(self):
        # 64: '䷀', 1: '䷁', 35: '䷂', 18: '䷃', 59: '䷄', 24: '䷅'
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('111111'), 64)
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('000000'), 1)
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('100010'), 35)
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('010001'), 18)
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('111010'), 59)
        self.assertEqual(_convert_bitmap_to_int_and_add_offset('010111'), 24)

    def test_predict(self):
        prediction = predict(23498732.234323)
        self.assertTrue(1 <= prediction <= 64)
