# ------------------------------------
# -- Sets --
#-----------
# [1] Set items are enclosed in curly braces.
# [2] Set items are not ordered and not indexed.
# [3] Set indexing and slicing can't be done.
# [4] Sets are mutable ==> you can add or delete or update a value.
# [5] Sets has only Immutable data types (Numbers, Strings, Tuples) List and Dict are not.
# [6] Set items is Unique
# ------------------------------------


# ---------------- Start ----------------
# Sets syntax and type test

S1 = {"Ahmed", "Labib", 51}
print(S1)
print(type(S1))

# Set items are not ordered and index or slicing can't be done.

S2 = {"Amr", "Khalid", 789}
print(S2) # Not ordered
# print(S2[0]) Not indexed
# ----------------- end -----------------


# ---------------- Start ----------------
# Sets has only Immutable data types (Numbers, Strings, Tuples) List and Dict are not.
S3 = {1, 2, 3, 1.5, 5.25, "Ahmed", "Labib", True, False, (1, 2, 3)}
print(S3)
# ----------------- end -----------------


# ---------------- Start ----------------
# Set items is Unique.
S4 = {1, 2, 3, 1,"Ahmed", "Labib", "Ahmed",True, False, True}
print(S4)
# ----------------- end -----------------

# ------------------
# -- Sets Methods --
# ------------------

# [1] add(element) This has no effect if the element is already present.
S5 = {"Ahmed", "Labib", 51}

S5.add("Hello World")
S5.add("Labib") # "Labib" is already exsist in the set so it will not affect.
print(S5)

# [2] remove(element) If the element is not a member, raise a KeyError.
S6 = {"Ahmed", "Labib", 51}

S6.remove(51)
# S6.remove("Hello") # "Hello" is not a member so it will raise a KeyError.
print(S6)

# [3] Discard(element) Unlike set.remove(), the discard() method does not raise an exception when an element is missing from the set.
S7 = {"Ahmed", "Labib", 51}

S7.discard(51)
S7.discard("Hello")
print(S7)

# [4] pop() pop does not take any parameters.
S8 = {"Ahmed", "Labib", 51}

print(S8.pop()) # Output: 51 (or another element, sets are unordered)
print(S8)

# Note: pop in list can take index as argument.
# Note: pop in set does not take any parameters.

# [5] Clear() clear does not take any parameters.
S9 = {1, 2, 3}

S9.clear()
print(S9)

# [6] copy() copy does not take any parameters.
# copy method Return a shallow copy of the set.

S10 = {60, 0, 90, -15, 42}
S11 = S10 

print(id(S10))
print(id(S11))

# (S10) and (S11) are pointing to the same memory address.
# The copy method allows creating a new set with the same elements but a different memory address.

S12 = S10.copy()

print(id(S10)) # Main set
print(id(S12)) # Copied set

# [7] Update() Updates the set, adding elements from all other provided iterables.
# iterables like (list) - (tuple) - (set) - (string) - (range)
# Note: (int) - (float) - (complex) - (bool) is none iterable

S13 = {"Ahmed", "Labib", 51}

S13.update([1, 2, 3], (4,5,6), {7,8,9}, "Hello World", range(10, 13))
print(S13)

# [8] union()
S14 = {1, 2, 3}
S15 = {4, 5, 6}

print(S14 | S15)      # Using union operator.
print(S14.union(S15)) # Using union method.

# Note: Both union operator and union method do not modify the original sets
# They create and return a new set containing the union result.

# [9] intersection()
S16 = {1, 2, 3}
S17 = {2, 3, 4}

print(S16 & S17)             # Using intersection operator.
print(S16.intersection(S17)) # Using intersection method.

# Note: Both intersection operator and intersection method do not modify the original sets
# They create and return a new set containing the intersection result.

# [10] Difference()
S18 = {1, 2, 3}
S19 = {2, 3, 4}

print(S16 - S17)           # Using Difference operator.
print(S16.difference(S17)) # Using Difference method.

# Note: Both Difference operator and Difference method do not modify the original sets
# They create and return a new set containing the Difference result.

# [11] Symmetric Difference()
S19 = {1, 2, 3}
S20 = {2, 3, 4}

print(S19 ^ S20)                     # Using symmetric Difference operator.
print(S19.symmetric_difference(S20)) # Using symmetric Difference method.

# Note: Both symmetric Difference operator and symmetric Difference method do not modify the original sets
# They create and return a new set containing the symmetric Difference result.

# [12] issubset()
S21 = {1, 2, 3}
S22 = {1, 2, 3, 4, 5, 6}

print(S21 <= S22)        # Using Subset operator.
print(S21.issubset(S22)) # Using issubset method.

# [13] issuperset()
S23 = {1, 2, 3, 4, 5, 6}
S24 = {1, 2, 3}

print(S23 >= S24)        # Using Subset operator.
print(S23.issuperset(S24)) # Using issubset method.

# [14] isdisjoint()
S25 = {1, 2, 3}
S26 = {4, 5, 6}

print(S25.isdisjoint(S26))

# [15] intersection_update()
S27 = {1, 2, 3}
S28 = {2, 3, 4}

S27.intersection_update(S28)
print(S27)

# [16] difference_update()
S29 = {1, 2, 3}
S30 = {2, 3, 4}

S29.difference_update(S30)
print(S29)

# [17] symmetric_difference_update()
S31 = {1, 2, 3}
S32 = {2, 3, 4}

S31.symmetric_difference_update(S32)
print(S31)