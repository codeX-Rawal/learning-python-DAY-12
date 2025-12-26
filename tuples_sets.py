# Day 12: Tuples and Sets in Python

# ---------------- TUPLES ----------------
# Tuple is ordered and immutable (cannot be changed)

colors = ("red", "green", "blue")
print("Colors tuple:", colors)

# Accessing elements
print("First color:", colors[0])
print("Last color:", colors[-1])

# Looping through tuple
for color in colors:
    print("Color:", color)

# Tuple with mixed data types
student = ("Rawal", 18, True)
print("Student tuple:", student)

# ---------------- SETS ----------------
# Set is unordered and unique elements only

numbers = {1, 2, 3, 4, 4, 5}
print("Numbers set:", numbers)  # duplicate removed

# Adding elements
numbers.add(6)
print("After adding 6:", numbers)

# Removing elements
numbers.remove(3)
print("After removing 3:", numbers)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)

# User input example
items = set()

n = int(input("How many items? "))
for i in range(n):
    item = input("Enter item: ")
    items.add(item)

print("Unique items:", items)
