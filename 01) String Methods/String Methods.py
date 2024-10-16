# ----------------------
# ----String Methods----
# ----------------------

Str1 = "Hello World"
Str2 = "12345"
Str3 = "Ahmed999"
lst = ["Hello", "World"]

# index:  0 1 2 3 4 5 6 7 8 9 10
# String: H e l l o   W o r l d

#----------------Start----------------
print(Str1.lower()) # Converts all characters in a string to lowercase.
print(Str1.upper()) # Converts all characters in a string to uppercase.
print(Str1.capitalize()) # Converts the first character to uppercase and the rest to lowercase.

print(Str1.title())
# Converts the first character of each word to uppercase and the rest to lowercase,
# also Converts the first character after any digit to uppercase and the rest to lowercase.

print(Str3.swapcase())
# (O/P) ==> aHMED999 because it swap all capital letters to small and vice versa,
# and if it encounter any digits or whitespaces doesn't affect them in any way.
#-----------------end-----------------


#----------------Start----------------
Str4 = "      I Love Python      "
Str5 = "######I Love Python######"
Str6 = "#@#@#@I Love Python#@#@#@"

# Note: in strip, lstrip and rstrip the parameter is optioal and by default this parametere is delte whitespaces 
# but you can modify it

print(Str4.strip())  # delete all whitespace from the left and right of the string
print(Str4.lstrip()) # delete whitespace which only in the left of string
print(Str4.rstrip()) # delete whitespace which only in the right of string

print(Str5.strip('#'))  # delete all hashs from the left and right of the string
print(Str5.lstrip('#')) # delete hashs which only in the left of string
print(Str5.rstrip('#')) # delete hashs which only in the right of string

print(Str6.strip('#@'))  # delete all #@ from the left and right of the string
print(Str6.lstrip('#@')) # delete #@ which only in the left of string
print(Str6.rstrip('#@')) # delete #@ which only in the right of string
#-----------------end-----------------


#----------------Start----------------
print(Str1.find("World")) # Returns the lowest index in the string where substring is found and if not found return -1.
print(Str1.find("o", 5)) # it will start from index 5 to search about (o).
print(Str1.find("W", 3, 9)) # it will start from index 3 to index 9 to search about (o).
# The 2 parameters start and end in find and rfind is optipnal and start is included but end is excluded when search about the substring.

print(Str1.index("World")) # Returns the lowest index in the string where substring is found and if not found it will through error message.
print(Str1.index("o", 5)) # it will start from index 5 to search about (o).
print(Str1.index("W", 3, 9)) # it will start from index 3 to index 9 to search about (o).
# The 2 parameters start and end in find and rfind is optipnal and start is included but end is excluded when search about the substring.

print(Str1.rfind("l"))
# rfind method returns the highest index in the string where the specified substring is found. If the substring is not found,
# it returns -1. This method is similar to find, but it searches from the end of the string rather than the beginning.

print(Str1.rindex("l")) # same like rfind and the only differnece if the substring not found it will through error message
#-----------------end-----------------


#----------------Start----------------
# str.replace(old, new, count): Replaces all occurrences of substring old with new.
test0 = "Hello one two three one one"
print(test0.replace("one", "1"))
print(test0.replace("one", "1", 1))
print(test0.replace("one", "1", 2))

print(Str1.count("l")) # (O/P) ==> 3 str.count(sub): Returns the number of occurrences of substring sub.

# Note: count() method can take 2 other optioanl parameters which are start and end of the index in the string
print(Str1.count("l", 0, 4)) # (O/P) ==> 2
#-----------------end-----------------


#----------------Start----------------
print(Str1.startswith("Hello")) # (O/P) ==> True because str.startswith(prefix) Returns True if the string starts with the specified prefix.
print(Str1.endswith("World"))   # (O/P) ==> True because str.endswith(suffix): Returns True if the string ends with the specified suffix.

print(Str1.startswith("ello")) # (O/P) ==> False
print(Str1.endswith("Worl"))   # (O/P) ==> False

# Note: startswith() and endwith() methods can take 2 other optioanl parameters which are start and end of the index in the string.
# The start parameter is inclusive: the check starts from the character at this index.
# The end parameter is exclusive: the check stops just before the character at this index.
print(Str1.startswith("l", 2, 5))
print(Str1.endswith("o", 2, 5))
#-----------------end-----------------


#----------------Start----------------
# str.split(sep): Splits the string at the specified sep and returns a list of substrings,
# split() method uses whitespace as the default delimiter.

print(Str1.split()) 
print(type(Str1.split())) # (O/P) ==> list

# The split method can take up to two parameters:
#   [1] Separator: The delimiter string where the split occurs.
#       If not provided or None, the string is split at any whitespace.
#
#   [2] Maxsplit: The maximum number of splits to do.
#       If not provided or -1, there is no limit on the number of splits.
#       The resulting list can have at most maxsplit + 1 elements.

test1 = "I-love-c++-and-python"
print(test1.split("-", 2)) # (O/P) ==> ['I', 'love', 'python-and-php']

# When using the rsplit method, the maxsplit parameter can highlight the difference between splitting
# from the right (rsplit) and the default behavior of splitting from the left (split).
test2 = "I love c++ and python"
print(test2.rsplit(" ",2))

# The splitlines() method is used to split a string at line breaks and returns a list of the lines in the string.
# This method can handle different types of line breaks, including \n (newline), \r (carriage return), \r\n 
# (carriage return followed by newline) and can handle triple-quoted strings (""" or ''')
test3 = "First Line\nSecond Line\nThird Line"
print(test3.splitlines())

test7 = """First Line
           Second Line
           Third Line"""
print(test3.splitlines())

print(" ".join(lst)) # str.join(iterable): Joins the elements of an iterable (e.g., list) into a single string.
#-----------------end-----------------


#----------------Start----------------
# f"...": An f-string (formatted string literal) allows
# expressions to be embedded directly within string literals.
print(f"Welcome to python, {Str1}") 

# cenetr() method: how Width Calculation work?
#   [1] If the specified width is greater than the length of the string, the difference (padding) is evenly distributed on both sides.
#   [2] If the difference is an odd number, the left side will get one more padding character than the right side.

Name = "Ahmed"

print(Name.center(9))
print(Name.center(10, "*"))

# The rjust() and ljust() methods are used to adjust the alignment of a string by padding it
# with a specified character (space by default) to ensure the string reaches a specified width.
# The rjust() and ljust() methods are take two parameter:
#   [1] width: The total width of the resulting string after padding.
#   [2] fillchar (optional): The character to use for padding. The default is a space (' ').

print(Name.rjust(15, "*"))
print(Name.ljust(15, "*"))
#-----------------end-----------------


#----------------Start----------------
print(Str1.isalpha())  # (O/P) ==> False because of there are a whitespace in Str1 string.
print(Str2.isdigit())  # (O/P) ==> True because of Str2 contain of digits only and if there only one character it will return false.
print(Str3.isalnum())  # (O/P) ==> True because of Str3 contain of characters and digits only and if there any whitespace it will return false.
# Note: isalnum() Method will return true if the string contain chars or digits and It is not mandatory to conatin both

test4 = "I Love Python And 3G"
print(test4.istitle()) # (O/P) ==> True

test5 = " "
print(test5.isspace()) # (O/P) ==> True

test6 = "i love python"
print(test5.islower()) # (O/P) ==> True

#-----------------end-----------------


#----------------Start----------------
Num1 = "1"
Num2 = "11"
Num3 = "111"

print(Num1.zfill(3)) # the string "1" is padded with zeros to make it 3 characters long.
print(Num2.zfill(3)) # the string "11" is padded with zeros to make it 3 characters long.
print(Num3.zfill(3)) # The string "111" is already 3 characters long, so no padding is added.
#-----------------end-----------------


#----------------Start----------------
test7 = "Hello\tWorld\tI\tLove\tPython"
print(test7.expandtabs(2))
print(test7.expandtabs(4))
print(test7.expandtabs(8))
#-----------------end-----------------