# --------------------------
# -- Comparison Operators --
# --------------------------
# [1] [==] Equal to: check if (RHS) equal to (LHS)
# [2] [!=] Not equal to: check if (RHS) not equal to (LHS)
# [3] [>]  Greater than: check if (RHS) greater than (LHS)
# [4] [<]  less than: Greater than: check if (RHS) less than (LHS)
# [5] [>=] Greater than or equal: Greater than: check if (RHS) greater than or equal to (LHS)
# [6] [<=] less than or equal: Greater than: check if (RHS) less than or equal to (LHS)
# --------------------------
a, b, c = 10, 10, 5

# Equal to [==]
print(a == b)
print(a == c)
print("=" * 20)

# Not equal to [!=]
print(a != c)
print(a != b)
print("=" * 20)

# Greater than [>]
print(a > c)
print(a > b)
print("=" * 20)

# Greater than or equal [>=]
print(a >= c)
print(a >= b)
print("=" * 20)

# Greater than [<]
print(a < c)
print(a < b)
print("=" * 20)

# Greater than or equal [<=]
print(a <= c)
print(a <= b)