# List
# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4, 5]
print("Numbers List:", numbers)

# A list of strings
fruits = ["apple", "banana", "cherry"]
print("Fruits List:", fruits)

# A list with mixed data types
mixed_list = [1, "hello", 3.14, True]
print("Mixed List:", mixed_list)

# A list of lists (nested lists)
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("Nested List:", nested_list)

# list operations
string_to_list = list("python")
print("String to List:", string_to_list)

# Accessing list elements
cars = ["BMW", "Audi", "Tesla"]
print("First Car:", cars[0])
print("Last Car:", cars[-1])

# Modifying list elements
cars[1] = "Toyota"
print("Modified Cars List:", cars)

# Adding elements to a list
# Using append() to add an element at the end
cars.append("Nissan")
print("After Append:", cars)
# Using insert() to add an element at a specific position
cars.insert(1, "Lamborghini")
print("After Insert:", cars)

# Removing elements from a list
# Using remove() to remove a specific element
cars.remove("BMW")
print("After Remove:", cars)
# Using pop() to remove an element at a specific index
removed_car = cars.pop(2)
print("After Pop:", cars)
print("Removed Car:", removed_car)
# Using del to remove an element at a specific index
del cars[0]
print("After Del:", cars)

# Organizing list elements
# Permanently sorting a list using sort()
numbers = [5, 2, 9, 1, 5, 6]
numbers.sort() # ascending order
print("Ascending Sorted Numbers:", numbers)
numbers.sort(reverse=True) # descending order 
print("Descending Sorted Numbers:", numbers)

# Temporarily sorting a list using sorted()
fruits = ["banana", "apple", "cherry"]
print("Original Fruits List:", fruits)
print("Temporarily Sorted Fruits List:", sorted(fruits))

# Reversing a list using reverse()
fruits.reverse()
print("Reversed Fruits List:", fruits) 

# Finding the length of a list using len()
print("Length of Fruits List:", len(fruits))

# Looping through a list using for loop
for fruit in fruits:
    print("Fruit:", fruit)

# Slicing a list
numbers = [10, 20, 30, 40, 50, 60]
print("First three numbers:", numbers[:3])
print("Last three numbers:", numbers[-3:])
print("Middle numbers:", numbers[2:5])  

# Copying a list
original_list = [1, 2, 3, 4, 5]
# Using slicing
copied_list1 = original_list[:]
print("Copied List using Slicing:", copied_list1)

# List comprehension
squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers using List Comprehension:", squared_numbers)


# Tuples
# An empty tuple
empty_tuple = ()
# A tuple of integers
int_tuple = (1, 2, 3, 4, 5)
# A tuple of strings
str_tuple = ("apple", "banana", "cherry")
# A tuple with mixed data types
mixed_tuple = (1, "hello", 3.14, True)
# A tuple of tuples (nested tuples)
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Tuples:")
print("Empty Tuple:", empty_tuple)
print("Integer Tuple:", int_tuple)
print("String Tuple:", str_tuple)
print("Mixed Tuple:", mixed_tuple)
print("Nested Tuple:", nested_tuple)
# Accessing tuple elements
print("First element of int_tuple:", int_tuple[0])
print("Last element of str_tuple:", str_tuple[-1])
# Tuples are immutable, so we cannot modify their elements
# However, we can concatenate tuples to create a new tuple
new_tuple = int_tuple + (6, 7, 8)
print("Concatenated Tuple:", new_tuple)
# Looping through a tuple
for item in str_tuple:
    print("Item in str_tuple:", item)
# Finding the length of a tuple
print("Length of mixed_tuple:", len(mixed_tuple))
# Tuple unpacking
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)
# Single element tuple (note the comma)
single_element_tuple = (42,)
print("Single Element Tuple:", single_element_tuple)
# Tuple comprehension (actually creates a generator)
squared_tuple = tuple(x**2 for x in range(1, 6))
print("Squared Numbers using Tuple Comprehension:", squared_tuple)