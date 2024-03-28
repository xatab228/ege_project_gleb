from functools import lru_cache
import sys
sys.setrecursionlimit(10000000)


def moves(h):
    return h + 1, h + 4, h * 5


@lru_cache(None)
def game(h):
    if h >= 68: return 'W'
    if any(game(m) == 'W' for m in moves(h)): return 'P1'
    if all(game(m) == 'P1' for m in moves(h)): return 'B1'
    if any(game(m) == 'B1' for m in moves(h)): return 'P2'
    if all(game(m) == 'P1' or game(m) == 'P2' for m in moves(h)): return 'B2'


for s in range(1, 69):
    res = game(s)
    if res == 'B1':
        print(s, res)
