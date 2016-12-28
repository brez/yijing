# -*- coding: utf-8 -*-
"""

"Countless words count less than the silent balance between yin and yang"
  - Lao Tzu, Tao Te Ching

"""
import random

YIN   = 0
YANG  = 1
TAILS = 2
HEADS = 3
THREE = 3
HEXAGRAMS = {
    1: '䷁', 2: '䷖', 3: '䷇', 4: '䷓', 5: '䷏', 6: '䷢', 7: '䷬', 8: '䷋', 9: '䷎', 10: '䷳', 11: '䷦', 12: '䷴',
    13: '䷽', 14: '䷷', 15: '䷞', 16: '䷠', 17: '䷆', 18: '䷃', 19: '䷜', 20: '䷺', 21: '䷧', 22: '䷿', 23: '䷮',
    24: '䷅', 25: '䷭', 26: '䷑', 27: '䷯', 28: '䷸', 29: '䷟', 30: '䷱', 31: '䷛', 32: '䷫', 33: '䷗', 34: '䷚',
    35: '䷂', 36: '䷩', 37: '䷲', 38: '䷔', 39: '䷐', 40: '䷘', 41: '䷣', 42: '䷕', 43: '䷾', 44: '䷤', 45: '䷶',
    46: '䷝', 47: '䷰', 48: '䷍', 49: '䷒', 50: '䷨', 51: '䷻', 52: '䷼', 53: '䷵', 54: '䷥', 55: '䷹', 56: '䷉',
    57: '䷊', 58: '䷙', 59: '䷄', 60: '䷈', 61: '䷡', 63: '䷪', 64: '䷀'
}


def _heads_or_tails():
    return random.randint(TAILS, HEADS)


# rolls three coins and sums the total, even are yin, odd are yang
def _line():
    six_thru_nine = 0
    for coin in range(THREE):
        six_thru_nine += _heads_or_tails()
    return (six_thru_nine % 2)


def _convert_bitmap_to_int_and_add_offset(bitmap):
    return int(bitmap, 2) + 1


# main prediction method, requires a seed, reversed because they grow from the bottom
def predict(seed):
    random.seed(seed)
    hexagram = []
    for line in range(6):
        hexagram.append(str(_line()))
    return _convert_bitmap_to_int_and_add_offset("".join(reversed(hexagram)))


# lastly get the unicode value if interested
def lookup(hexagram_base10):
    return HEXAGRAMS[hexagram_base10]




