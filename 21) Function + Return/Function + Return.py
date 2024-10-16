# --------------------------
# -- Function And Return --
# --------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function is For All Team and All Apps
# ---------------------------------------

def function_name():
    # Write your Task Here
    print('Hello Python, This is my Firts Function')

function_name()

print('-' * 10)
# ---------------------------------------

def say_hello(name):
    print(f'Hello {name}')

say_hello('Ahmed')

# name  is a parameter
# Ahmed is an argument

print('-' * 10)
# ---------------------------------------

def Sum_2_Numbers(num1, num2):
    sum = num1 + num2
    return sum

sum = Sum_2_Numbers(15, 25)
print(sum)