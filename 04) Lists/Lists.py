# --------------------------------
# -- List --
# ----------
# [1] List items are enclosed in square brackets.
# [2] List are Ordered, to use index to access items.
# [3] List are Mutable ==> you can Add or Delete or Update a value.
# [4] List items is not Unique.
# [5] List can have different data types.
# --------------------------------

myList1 = [1, 2, 3.5, "Ahmed", "Labib", True, False, ["Hello", "World", 1, 2]]

# access items in the List
print(myList1)        # Will print the whole list.
print(myList1[0])     # Will print 1.
print(myList1[-1])    # Will print the last item.
print(myList1[7][0])  # Will prints the element at index (0) of the sublist located at index (7) within myList.

# access slices in the List
print(myList1[2:])    # Will print from index (2) till the end.
print(myList1[:5])    # Will print from index (0) up to (but not including) index 5.
print(myList1[0:3])   # Will print [1, 2, 3.5], and Note that index (3) is excluded.
print(myList1[0:7:2]) # Starting at index 0, up to (but not including) index 7, selecting every second element.
print(myList1[::-1])  # Will print the list in reversed order.
print(myList1[7][0:]) # Will print starting from index (0) to the end of the sublist at index (7) within myList.

# Update items in the List

myList1[2] = 3 # value of index updated from (3.5) to (3)
print(myList1)

myList1[0:3] = [3, 2, 1]
print(myList1)

myList1[7] = ["What's up", "World", 2, 1]
print(myList1)

# ------------------
# -- List Methods --
# ------------------

# [1] append(element) Append object to the end of the list.

myList2 = ["Python", "C++", "Dart"]
myList3 = ["C#", "Java", "Ruby"] 

myList2.append("PHP")
print(myList2)

myList2.append(myList3)
print(myList2)

# [2] extend(element)
myList4 = ["Python", "C++", "Dart"]
myList5 = ["C#", "Java", "Ruby"]

myList4.extend("Hello")
print(myList4)

myList4.extend(myList5)
print(myList4)

# [3] insert(index, element) Insert object before index.

myList6 = ["Ahmed", "Ali", "Osama"]

myList6.insert(0,"Labib")
print(myList6)

myList6.insert(-1, "Mohamed") # (-1) mean the last element in the list
print(myList6)

# [4] remove(element) Remove first occurrence of value.

myList7 = [1, 2, 3, 2]
myList7.remove(2)
print(myList7)

myList8 = ["Ahmed", "Ali", "Amr", "Ahmed"]
myList8.remove("Ahmed")
print(myList8)

# [5] Sort()
# sort method can sort list contain of intergers only or strings only not both

myList8 = [60, 0, 90, -15, 42]

myList8.sort() # sort list in ascending order
print(myList8)

myList8.sort(reverse = True) # sort list in decending order, reverse is by default equal to false in sort method
print(myList8)

# [6] reverse()

myList9 = [60, 0, 90, -15, 42]

myList9.reverse()
print(myList9)

# [7] pop(index) Remove and return item at index (default last).

myList10 = [60, 0, 90, -15, 42]

myList10.pop() # Will pop last element.
print(myList10)

print(myList10.pop(1)) # Will pop element which in index (1).
print(myList10)

# [8] clear() clear does not take any parameters.

myList11 = [60, 0, 90, -15, 42]

myList11.clear()
print(myList11)

# [9] copy() Note: copy does not take any parameters.
# copy method Return a shallow copy of the list.

myList11 = [60, 0, 90, -15, 42]
myList12 = myList11 

print(id(myList11))
print(id(myList12))

myList11.append(22) # will append (22) in (myList11) and (myList12) because they are pointing to the same memory address.
print(myList11)
print(myList12)

# (myList11) and (myList12) are pointing to the same memory address.
# The copy method allows creating a new list with the same elements but a different memory address.

myList13 = myList11.copy()

print(id(myList11)) # Main list
print(id(myList13)) # Copied list

# [10] count(element) Return number of occurrences of value.

myList14 = [1, 2, 3, 1, 5, 6, 1]
print(myList14.count(1)) # Will print (3)

# [11] index(element) Return first index of value.

myList15 = ["Ahmed", "Ali", "Ramy", "Yasser"]
print(myList15.index("Ramy")) # Will print index (2)
# Note: It will print the index of the first occurrence of the specified value.