# --------------------
# --  Control Flow  --
# -- if, elif, else --
# -- Make Decisions --
# --------------------

# User information
Username = 'A7med Labib'
User_country = 'Saudi Arabia'
Course_name = 'C++ Course'
Course_Price = 100
Course_Discount = 0  # Initial discount


# Applying discount based on the country
if User_country == 'Egypt' or User_country == 'Saudi Arabia':
    Course_Discount = 60
else:
    Course_Discount = 30


print(f"User Information:")
print(f"-----------------")
print(f"Username       : {Username}")
print(f"User Country   : {User_country}")
print(f"Course Name    : {Course_name}")
print(f"Original Price : ${Course_Price}")
print(f"Discount       : ${Course_Discount}")
print(f"Final Price    : ${Course_Price - Course_Discount}")
print('==============================')

# -------------------------
# -- Nested if Condition --
# -------------------------

isStudent = 'Yes'

if User_country == 'Egypt' or User_country == 'Saudi Arabia':
    if isStudent == 'Yes':
        Course_Discount = 80
    else:
        Course_Discount = 60
else:
        Course_Discount = 30

print(f"User Information:")
print(f"-----------------")
print(f"Username       : {Username}")
print(f"User Country   : {User_country}")
print(f"Course Name    : {Course_name}")
print(f"Original Price : ${Course_Price}")
print(f"Discount       : ${Course_Discount}")
print(f"Final Price    : ${Course_Price - Course_Discount}")

# ----------------------------------
# -- Ternary Conditional Operator --
# --         Short Hand IF        --
# ----------------------------------

# Ternary Conditional Operator: 
#       ● is a concise way to write an if-else statement in a single line.
#       ● It must include both the if and else parts.
#       ● The general syntax is: <value_if_true> if <condition> else <value_if_false>
# Examble:

age = 18

print('Adult') if age >= 18 else print('Minor')

# Short Hand IF:
#       ● A way to write a simple if statement in a single line, without an else part.
#       ● The general syntax is:  if <condition>: <do_something>
# Examble:

if age >= 18: print('Adult')