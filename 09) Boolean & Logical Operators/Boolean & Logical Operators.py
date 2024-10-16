# -------------
# -- Boolean --
# -------------
# [1] True and False are the two Boolean values in Python.
# [2] They are used to represent truth values.
# [3] True is equivalent to 1, and False is equivalent to 0.
# --------------------------------------------

# Exambles
Name = " "
print(Name.isspace())

print("=" * 50)

print(100 > 200)
print(100 > 100)
print(100 > 90)

print("=" * 50)

# The bool() function in Python is used to convert a value to a Boolean (True or False). It evaluates the given
# value and returns True if the value is considered "truthy" and False if the value is considered "falsy".

# True values
print(bool("Ahmed"))
print(bool(15))
print(bool(15.5))
print(bool([1, 2, 3]))
print(bool((1, 2, 3)))
print(bool({1, 2, 3}))
print(bool({"one" : 1, "two" : 2}))
print(bool(True))

print("=" * 50)

# False values
print(bool(""))
print(bool(0))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(None))
print(bool(False))

print("=" * 50)

# -------------------------------------------
# -- logical Operators (Boolean Operators) --
# -------------------------------------------
# [1] and
# [2] or
# [3] not
# -------------------------------------------

age = 35
country = "Egypt"

# and logical operator
# ------- and --------
#  A      B    A and B
# --------------------
# True  True   True   
# True  False  False  
# False True   False  
# False False  False  
# --------------------
print(age > 16 and country == "Egypt")      # True and true = True.
print(age > 16 and country == "Alexandria") # True and False = False.
print(age < 16 and country == "Egypt")      # False and True = Fasle.
print(age < 16 and country == "Alexandria") # False and False = Fasle.
print("=" * 50)

# or logical operator
# -------- or --------
#  A      B    A and B
# --------------------
# True  True   True   
# True  False  True   
# False True   true   
# False False  False  
# --------------------
print(age > 16 or country == "Egypt")      # True and true = True
print(age > 16 or country == "Alexandria") # True and False = True 
print(age < 16 or country == "Egypt")      # False and True = True
print(age < 16 or country == "Alexandria") # False and False = Fasle
print("=" * 50)

# not logical operator
# ---- not ----
#  A      not A
# -------------
#  True   False
#  False  True 
# -------------
print(not (age > 16)) # not(True) = False
print(not (age < 16)) # not(False) = True