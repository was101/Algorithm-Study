solution = lambda A, B: sum([x * y for x, y in zip(sorted(A), sorted(B,reverse=True))])