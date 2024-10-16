# ------------------------------------------------
# -- Loop ==> For --
# --------------------
# for item in iterable_object:
#   Do Something with item
# --------------------
# Item is a variable you create and call whenever you want
# Item refer to the current position and will run and visit all items to the end
# iterable_object ==> Sequence [list, tuple, set, Dic, string of characters, rnage, etc ...]
# ------------------------------------------------

Numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for Number in Numbers:
    if Number % 2 == 0:
        print(f'{Number} is Even.')
    else:
        print(f'{Number} is odd.')

print('-' * 50)
# ------------------------------------------------

Name = 'Ahmed'

for letter in Name:
    print(letter)

print('-' * 50)
# ------------------------------------------------

peoples = ['Osama', 'Ahmed', 'Sayed', 'Ali']
skills = ['html', 'css', 'js']

for name in peoples: # Outer Loop
    print(f'{name} skills is:')
    for skill in skills: # Inner Loop
        print(skill)