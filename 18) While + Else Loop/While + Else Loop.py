# ------------------------------------------------
# -- Loop ==> While --
# --------------------
# A while loop is used to repeat a block of code
# as long as a given condition is True.
# ------------------------------------------------

count = 0

while count < 10:
    print(count)
    count += 1
else:
    print('Loop is ended')

print('-' * 50)
# ------------------------------------------------

while False:
    print('Loop will not Start at all')
    print('Because Condition is False')

# ------------------------------------------------

myFriends = ["Os", "Ah", "Ga", "Al", "Ra", "Sa", "Ta", "Ma", "Mo", "Wa"]
count = 0

while count < len(myFriends):
    print(f'#{str(count+1).zfill(2)} {myFriends[count]}')
    count += 1