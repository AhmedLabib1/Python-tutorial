# ------------------------------
# -- Continue & Breake & Pass --
# ------------------------------
# continue: Skips the current iteration and moves to the next.
# break: Exits the loop immediately.
# pass: Does nothing; used as a placeholder for code.
# ------------------------------

Numbers = [1, 4, 6, 8, 9, 11, 13, 15, 19]

# Continue
for Number in Numbers:
    if Number == 13:
        continue
    print(Number)

print('-' * 10)
# ------------------------------

# Breake
for Number in Numbers:
    if Number == 13:
        break
    print(Number)

print('-' * 10)
# ------------------------------

# Pass
for Number in Numbers:
    pass