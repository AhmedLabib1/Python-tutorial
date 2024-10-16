# 1) Syntax 
# ==========
# [1] Lists  : Defined with square brackets [].
# [2] Tuples : Defined with parentheses ().
# [3] Sets   : Defined with curly brackets {}.
# [4] Dict   : Defined with curly brackets {} and each item have key and value.
# 
# 2) Mutability 
# ==============
#
# [1] Lists  : List are Mutable so you can Add or Delete or Update an item.
# [2] Tuples : tuples are Immutable so you can't add or delete or update a value.
# [3] Sets   : Sets are mutable so you can add or delete or update an item.
# [4] Dict   : Dict are mutable so you can add or delete or update an item.
#
#  
# 2) Stored Data 
# ===============
#
# [1] Lists  : Lists can store elements of any data type.
# [2] Tuples : Tuples can store elements of any data type.
# [3] Sets   : Sets can store immutable elements only like Numbers, Strings and Tuples
# [4] Dict   : Dictionaries store data in key-value pairs, keys are unique and immutable, and values can be from any data type.

# 3) Order 
# =========
#
# [1] Lists  : Ordered (maintains the order of elements).
# [2] Tuples : Ordered (maintains the order of elements).
# [3] Sets   : Unordered (does not maintain the order of elements).
# [4] Dict   : Ordered (maintains the order of elements).
#
# 4) Duplicates 
# ==============
#
# [1] Lists  : Allows duplicate elements.
# [2] Tuples : Allows duplicate elements.
# [3] Sets   : does not allow duplicate elements (automatically remove duplicate values).
# [4] Dict   : Does not allow duplicate keys, but values can be duplicates.
#
# 5) Common Methods 
# ==================
#
# [1] List 
# =========
# 01- append(element): Append element to the end of the list.
#
# 02- extend(iterable): takes an iterable as a parameter. It iterates through the elements of the iterable and adds each element to the end of the list.
#
# 03- insert(index, element): Insert element before index.
#
# 04- remove(element): Remove first occurrence of this element.
#
# 05- sort(key = None, reverse = False): sorts the elements of the list in place. It optionally takes two parameters: key and reverse,
#     and by default key = None and reverse = False, If reverse set to True, sorts the list in descending order.
#
# 06- reverse(): reverse items of the list and does not take any parameteres.
#
# 07- pop(index): Remove and return item at index (default last).
#
# 08- clear(): remove all elements from the list, It's does not take any parameters.
#
# 09- copy(): copy method Return a shallow copy of the list,  It's does not take any parameters.
#
# 10- count(element): Return number of occurrences of value.
#
# 11- index(element): Return first index of value.

# [1] tuple 
# ==========
# 1- count(element): Return number of occurrences of value.
#
# 2- index(element) Return first index of value.

# [3] Set 
# ========
# 01- add(element): This has no effect if the element is already present, because set doesn't allow duplicate values.
#
# 02- remove(element): If the element is not a member, raise a KeyError.
#
# 03- Discard(element): Unlike remove() method, the discard() method does not raise an exception when an element is missing from the set.
#
# 04- pop(): Remove and return item at index, pop does not take any parameters, unlike one which in list can take index as parametere.
#
# 05- clear(): remove all elements from the set, It's does not take any parameters.
#
# 06- copy(): copy method Return a shallow copy of the set,  It's does not take any parameters.
#
# 07- update(iterable): can take only iterable as a parametere like (list - tuple - set - dictionary - string).
#
# 08- union(set or iterable): returns a new set that contains all unique elements from the set and other sets or iterables provided as arguments.
#
# 09- intersection(set or iterable): returns a new set that contains only the elements that are common to two or more sets or iterables.
#
# 10- Difference(set or iterable): returns a new set that contains elements that are present in one set but not in another set or sets.
#
# 11- Symmetric Difference(set or iterable): returns a new set that contains elements that are present in either of the sets but not in both sets.
#
# 12- issubset(set or iterable): returns True if all elements of the set are present in another set or iterable; otherwise, it returns False.
#
# 13- issuperset(set or iterable): Returns True if all elements of another set or iterable are present in the set; otherwise, it returns False.
#
# 14- isdisjoint(set or iterable): Return True if two sets have a null intersection. Note: S1.isdisjoint(S2) == (not S1.intersection(S2))
#
# 15- intersection_update(): Update a set with the intersection of itself and another.
#
# 16- difference_update(): Remove all elements of another set from this set.
#
# 17- symmetric_difference_update(): Update a set with the symmetric difference of itself and another.

# [4] Dictionary 
# ===============
# 1- clear(): Removes all items from the dictionary, It's does not take any parameters.
# 
# 2- copy(): Returns a shallow copy of the dictionary, It's does not take any parameters.
# 
# 3- fromkeys(iterable, value = None): Creates a new dictionary with keys from an iterable and values set to a specified value.
# 
# 4- get(key, default = None): Return the value for key if key is in the dictionary, else return default.
# 
# 5- items(): Returns a view object that displays a list of dictionary's key-value tuple pairs (List of Tuples).
# 
# 6- keys(): Returns a view object that displays a list of all the keys in the dictionary.
# 
# 7- values(): Returns a view object that displays a list of all the values in the dictionary.
#
# 8- pop(key, default = None): Removes the specified key and returns the corresponding value. If the key is not found, the default value is returned.
# 
# 9- popitem(): Removes and returns a random (key, value) pair from the dictionary as a tuple. If the dictionary is empty, it raises a KeyError.
# 
# 10- setdefault(key, default = None): Returns the value of the specified key. If the key does not exist, inserts the key with the specified default value.
# 
# 11- update(iterable): Updates the dictionary with elements from another dictionary object or from an iterable of key-value pairs.