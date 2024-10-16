# ----------------
# -- User Input --
# ----------------

fName = input("what's your first name?")
mName = input("what's your middle name?")
lName = input("what's your last name?")

fName = fName.strip().capitalize()
mName = mName.strip().capitalize()
lName = lName.strip().capitalize()

print(f"Your name is: {fName} {mName} {lName}")