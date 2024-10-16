# ---------------------------------
# -- Dictionary --
# ----------------
# [1] Dict items are enclosed in curly braces.
# [2] each item in Dict contains of kay and value.
# [3] Dict is not ordered so you can't access it's element with index but with it's keys
# [4] Dict itself is mutable so you can add or delete or overwrite an item.
# [5] Dict key must be immutable. This means once a key is created, its value cannot be changed like (String) - (Nymber) - (Tuple).
# [6] Dict key must be unique. If you try to use a duplicate key, the new value will overwrite the existing value.
# [7] Dict value can be from any data type including mutable types like lists, dictionaries, and sets, as well as immutable types like strings, numbers, and tuples.
# [8] Dict value can be mutable or immutable. You can modify a mutable value directly, but you cannot change an immutable value.
# ---------------------------------


# ------------ Start ---------------
# Dict syntax and type check
user = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

print(type(user))
print(user)
# ------------- end ----------------


# ------------ Start ---------------
# Dict itself is mutable so you can add or delete or overwrite an item.
Person1 = {
    "Name" : "Ahmed Labib",
    "Job"  : "Programmer",
    "Age"  : 19
}

# updating dictionary by adding new value
Person1["City"] = "New York"  # Adding a new key-value pair
print(Person1)

# updating dictionary by deleting a value
del Person1["City"]
print(Person1)

# updating dictionary by overwrite a value
Person1["Age"] = 25
print(Person1)
# ------------- end ----------------


# ------------ Start ---------------
# Dict key must be immutable. This means once a key is created, its value cannot be changed like (String) - (Nymber) - (Tuple).
# Dict key must be unique. If you try to use a duplicate key, the new value will overwrite the existing value.
Person2 = {
    "Name": "John Wick",
    "Job" : "murderer",
    "Age" : 40,
    "Age" : 45 # overwrite the old value of Age
}

print(Person2)

# ------------- end ----------------


# ------------ Start ---------------
# dictionaries values can be of any data type. This includes both mutable types (which can be changed after creation) and immutable types (which cannot be changed after creation).

Person3 = {"Name": "Ahmed"} # The value "Alice" is a string, which is immutable.
Person4 = {"Age": 30} # The value 30 is an integer, which is immutable.
Person5 = {"Coordinates": (10, 20)} # The value (10, 20) is a tuple, which is immutable.
Person6 = {"Scores": [90, 85, 77]} # The value [90, 85, 88] is a list, which is mutable.
Person7 = {"Numbers": {1, 2, 3}}  # The value {1, 2, 3} is a set, which is mutable
Person8 = {"Profile": {"name": "Wael", "age": 30}}  # The value is another dictionary, which is mutable
# ------------- end ----------------


# ------------ Start ---------------
# Two Dimensional Dictionary
lang = {
    "one": {
        "name" : "html",
        "Progress": "80%" 
    },
    "two": {
        "name" : "c++",
        "Progress": "70%" 
    },
}

print(lang)
print(lang["one"]["name"])
print(lang["one"]["Progress"])
print(lang["two"]["name"])
print(lang["two"]["Progress"])
# ------------- end ----------------


# ------------ Start ---------------
# Dictionary from variables

frameWorkOne = {
    "Name" : "C++",
    "Preogress" : "70%"
}

frameWorkTwo = {
    "Name" : "Python",
    "Preogress" : "20%"
}

frameWorkThree = {
    "Name" : "R",
    "Preogress" : "50%"
}

allFrameWorks = {
    "one" : frameWorkOne,
    "two" : frameWorkTwo,
    "three" : frameWorkThree
}
print(allFrameWorks)
# ------------- end ----------------


# ------------------------
# -- Dictionary Methods --
# ------------------------

# [1] clear()
#Removes all items from the dictionary.

user1 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

user1.clear()
print(user1)

# [2] copy()
# Returns a shallow copy of the dictionary.

user2 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

new_user1 = user2.copy()
print(new_user1)

# [3] fromkeys(iterable, value = None)
# Creates a new dictionary with keys from an iterable and values set to a specified value.
# iterable can be (List) - (tuple) - (set) - (dictionary) - (string) - (range)

# Using a list as iterable
list_iterable = ["a", "b", "c"]
result_list = dict.fromkeys(list_iterable, None)
print(result_list)

# Using a tuple as iterable
tuple_iterable = ["a", "b", "c"]
result_tuple = dict.fromkeys(tuple_iterable, None)
print(result_tuple)

# Using a set as iterable
set_iterable = {"a", "b", "c"}
result_set = dict.fromkeys(set_iterable, None)
print(result_set)

# Using a dict as iterable
dict_iterable = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}
result_dict = dict.fromkeys(dict_iterable, None)
print(result_dict)

# Using a string as iterable
string_iterable = "abc"
result_string = dict.fromkeys(string_iterable, None)
print(result_string)

# Using a range as iterable
range_iterable = range(1,4)
result_range = dict.fromkeys(range_iterable, None)
print(result_range)

# [4] get(key, default = None)
# Return the value for key if key is in the dictionary, else return default.

user3 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

value1 = user3.get("Name","Not exsist")
print(value1)

value2 = user3.get("Job","Not exsist")
print(value2)

# [5 - 6 - 7] items() - keys() - values()
# item(): Returns a view object that displays a list of dictionary's key-value tuple pairs (List of Tuples).
# keys(): Returns a view object that displays a list of all the keys in the dictionary.
# values(): Returns a view object that displays a list of all the values in the dictionary.

user4 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

print(user4)
print(user4.items())
print(user4.keys())
print(user4.values())

# [8] pop(key, default = None)
# Removes the specified key and returns the corresponding value. If the key is not found, the default value is returned.

user5 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

print(user5.pop("Country", "Not exsist"))
print(user5.pop("Job", "Not exsist"))
print(user5)

# [9] popitem()
# Removes and returns the last (key, value) pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.

user6 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}

print(user6.popitem())

# [10] setdefault(key, default = None)
# Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.

user7 = {
    "Name" : "Ahmed",
    "Age" : 19,
    "Country" : "Alexandria"
}
print(user7.setdefault("Name",))
print(user7.setdefault("Job", "Programmer"))

# [11] update(iterable)
# Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.
# iterable of key-value pair can be (Another Dictionary) - (List of Lists) - (List of Tuples) - (Tuple of Tuples) - (Set of Tuples).

# Updating with another Iterable
dict1 = {"one" : 1, "two" : 2}
key_value_pair1 = {"three" : 3, "four" : 4}
dict1.update(key_value_pair1)
print(dict1)

# Updating with an Iterable of Key-Value Pairs (List of Lists)
dict2 = {"one" : 1, "two" : 2}
key_value_pair2 = [["three", 3], ["four", 4]]
dict2.update(key_value_pair2)
print(dict2)

# Updating with an Iterable of Key-Value Pairs (List of Tuples)
dict3 = {"one" : 1, "two" : 2}
key_value_pair3 = [("three", 3), ("four", 4)]
dict3.update(key_value_pair3)
print(dict3)

# Updating with an Iterable of Key-Value Pairs (Tuple of Tuples)
dict4 = {"one" : 1, "two" : 2}
key_value_pair4 = (("three", 3), ("four", 4))
dict4.update(key_value_pair4)
print(dict4)

# Updating with an Iterable of Key-Value Pairs (Set of Tuples)
# Remember: set is Unordered.
dict5 = {"one" : 1, "two" : 2}
key_value_pair5 = {("three", 3), ("four", 4)}
dict5.update(key_value_pair5)
print(dict5)