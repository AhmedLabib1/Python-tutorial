# -------------------------
# -- Strings Formatting  --
# -------------------------

# String formatting in Python allows you to create strings that include variables in a specific format.
# There are several ways to do string formatting in Python, but the two most common methods are
# using the % operator and using formatted string literals (f-strings) (in 3.6+).

F_Name = "Ahmed"
L_Name = "Labib"
list = ["Ahmed", "Labib"]
Age = 19
#----------------Start----------------
# How to format strings?

# [1] Using formatted string literals (f-strings) (new style formatting 3.6+):
formatted_Str2 = f"Name: {F_Name}, Age: {Age}"
print(formatted_Str2)

# [2] Using (%) operator (old style formatting):
formatted_Str1 = "Name: %.5s, Age: %.3d" % (F_Name, Age)
print(formatted_Str1)

# (%s) is used for string substitution.
# (%d) is used for integer substitution.
# (%f) is used for floating-point substitution.

# [3] Using .format() Method (old style formatting):
formatted_Str3 = "Name: {:.5s}, Age: {:03d}".format(F_Name, Age)
print(formatted_Str3)
#-----------------end-----------------


#----------------Start----------------
# How to truncate String?

myLongString = "Hello world, I love c++ and python"
myBigMoney = 550224397149

print("%s" % (myLongString)) # The whole string
print("%.11s" % (myLongString)) # Turncated string using % operator
print("{:.11s}".format(myLongString)) # Turncated string using .format method

print("{:_d}".format(myBigMoney)) # will put (_) after every three numbers.
print("{:,d}".format(myBigMoney)) # will put (,) after every three numbers.
#-----------------end-----------------


#----------------Start----------------
# How to rearrange items in format method?
# items or variables in format method is zero bases index

a, b, c = "One", "Two", "Three"
print("Hello {} {} {}".format(a, b, c)) # Hello One Two Three
print("Hello {2} {1} {0}".format(a, b, c)) # Hello Three Two One
print("Hello {1} {1} {1}".format(a, b, c)) #  Hello Two Two Two

x, y, z = 1, 2, 3

print("Hello {0:03d} {1:03d} {2:03d}".format(x, y, z))
print("Hello {2:04d} {0:04d} {1:04d}".format(x, y, z))

l, m, n = 1.5, 2.5, 3.5

print("{0:.2f} {1:.4f} {2:.8f}".format(l, m, n))
print("{1:.2f} {2:.4f} {0:.8f}".format(l, m, n))
#-----------------end-----------------


#----------------Start----------------
# how to concatenate strings?

# [1] Using the (+) operator:
Concatenated_str1 = F_Name + " " + L_Name
print(Concatenated_str1)

# [2] Using f-strings (formatted string literals):
Concatenated_str2 = f"{F_Name} {L_Name}"
print(Concatenated_str2)

# [3] Using the (+=) operator:
F_Name += " " + L_Name
print(F_Name)

# Note: When you use the (+=) operator to concatenate strings,
# you modify the original string (F_Name in this case)
#-----------------end-----------------