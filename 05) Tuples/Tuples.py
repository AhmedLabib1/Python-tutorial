# ----------------------------------------
# -- Tuples --
# [1] Tuple items are enclosed in parentheses.
# [2] You can remove parentheses if you want.
# [3] Tuple are ordered, to use index to access items.
# [4] tuples can store other tuples, lists, sets, dictionaries or other data types.
# [5] tuples are Immutable ==> you can't add or delete or update a value.
# [6] tuples items is not unique.
# ----------------------------------------


# ----------------------------------------
# -- Common Tuple Operations --
# [1] Concatenation: Combining two tuples.
# [2] Repetition: Repeating the elements of a tuple.
# [3] Membership Test: Checking if an element exists in a tuple.
# [4] Accessing Elements: Accessing elements by index.
# [5] Slicing: Accessing a subset of the tuple.
# [6] Unpacking: Assigning elements of a tuple to multiple variables.
# ----------------------------------------


#----------------Start----------------
# Tuple syntax and type test
t1 = (1, 2, 3)
t2 = 1, 2, 3, 4, 5, 6

print(t1)
print(t2)

print(type(t1))
print(type(t2))

# Tuple can store different type of items 
t3 = (1, 2, 3, 4.5, "Ahmed", "Labib", True, False, (1, 2, 3, True), [15,"Hello", "World"])
print(t3)
#-----------------end-----------------


#----------------Start----------------
# Accessing Elements: Accessing elements by index.
print(t1[0])
print(t1[1])
print(t1[2])
print(t3[8][0])   # Will print the element at index (0) of the subset located at index (8) within myTuple3.

# Slicing: Accessing a subset of the tuple.
print(t1[0:2])    # Will print from index (0) up to (but not included) index (2).
print(t1[::])     # Will print all items.
print(t2[0:5:2])  # Starting at index 0, up to (but not including) index 5, selecting every second element.
print(t1[::-1])   # Will print all items starting from the end.
print(t3[8][0:3]) # Will print the element start from index (0) up to (but not included) index (3) of the subset located at index (8) within myTuple3.
#-----------------end-----------------


#----------------Start----------------
# How to add, delete or update items in tuples?
# tuples are immutable, meaning you cannot change their contents after they are created.
# This immutability means you cannot add, delete, or update a value in a tuple directly.
# However, you can perform operations that create a new tuple with the desired changes:

# adding elements: You cannot add an element to an existing tuple.
# However,you can concatenate tuples to create a new tuple.
t4 = (1, 2, 3)
t4 = t4 + (4,)
print(t4)

# deleting elements: You cannot delet an element of a tuple. If you need to delete elements,
# you can convert the tuple to a list, delete the element, and then convert it back to a tuple.
t5 = (1, 2, 3)

t5 = list(t5)
t5.remove(2)
t5 = tuple(t5)

print(t5)

# Updating elements: You cannot update an element of a tuple. If you need to update elements,
# you can convert the tuple to a list, update the list, and then convert it back to a tuple.
t6 = (1, 2, 3)

t6 = list(t6)
t6[::] = ["one", "two", "three"]
t6 = tuple(t6)

print(t6)
#-----------------end-----------------


#----------------Start----------------
# when you want to create a tuple with a single element, you need to include a comma
# after the element. Without the comma, Python interprets the parentheses as just regular
# parentheses used for grouping expressions, and the variable is not considered a tuple.
t7 = ("Ahmed",) # this is a single element tuple
t8 = "Ahmed",   # this is a single element tuple

print(type(t7))
print(type(t8))
#-----------------end-----------------


#----------------Start----------------
# Concatenation: Combining two tuples.
a = (1, 2, 3)
b = (4,5,6)

c = a + b + ("Hello","World")
print(c)
#-----------------end-----------------


#----------------Start----------------
# string, list and tuple repeat
myString1 = "Ahmed"
mylist1 = [1, 2]
mytuple1 =(1, 2)

myString1 = myString1 * 6
mylist1 = mylist1 * 6
mytuple1 = mytuple1 * 6

print(myString1)
print(mylist1)
print(mytuple1)

# Note: you can also repeat in this way
myString2 = "Ahmed"
mylist2 = [1, 2]
mytuple2 =(1, 2)

print(myString2 * 6)
print(mylist2   * 6)
print(mytuple2  * 6)
#-----------------end-----------------


#----------------Start----------------
# Membership Test: Checking if an element exists in a tuple.
t9 = (1, 2, 3)
print(2 in t9)  # Output: True
print(4 in t9)  # Output: False
#-----------------end-----------------


#----------------Start----------------
# Unpacking: Assigning elements of a tuple to multiple variables.
t11 = (1, 2, 3)
x, y, z = t11
print(x)
print(y)
print(z)
#-----------------end-----------------


# -------------------
# -- Tuple Methods --
# -------------------

# tuples in Python have only two built-in methods: count() and index(). This is because tuples are immutable,
# meaning their elements cannot be changed once they are created. Due to their immutability, they do not have
# methods that modify the tuple, such as append(), remove(), or sort(), which are available for lists.

# [1] count(element) Return number of occurrences of value.
t12 = (1, 2, 3, 1, 2, 1)
print(t12.count(1)) # Output: 1

# [2] index(element) Return first index of value.
t13 = (1, 2, 3)
print(t12.index(3)) # Output: 2

# -----------------------------
# -- Tuple built-In Functions --
# -----------------------------
# [1] len(): Returns the number of items in a tuple.
# [2] max(): Returns the largest item in the tuple.
# [3] min(): Returns the smallest item in the tuple.
# [4] sum(): Returns the sum of all items in the tuple.
# [5] sorted(): Returns a sorted list of the tuple's elements.
# [6] tuple(): Converts a sequence (like a list) to a tuple.
# -----------------------------

# Note: Built-in functions are global functions provided by Python that can operate on a variety of data types,
# including tuples. They are not called on the tuple instance itself but are passed the tuple as an argument.