# DECLARING VARIABLES IN PYTHON
# ============================================================

# String variable
string_variable = "Hi welcome to python"
string_variable: str = "Hi welcome to python"

# Integer variable
int_variable = 3
int_variable: int = 3

# Float variable
float_variable = 3.11
float_variable: float = 3.11

# Boolean variable
bool_variable = True
bool_variable: bool = True

# List variable
list_variable = [
    "Number 0",
    "Number 1",
    "Number 2",
    "Number 3",
    "Number 4",
    "Number 5",
]
list_variable: list[str] = [
    "Number 0",
    "Number 1",
    "Number 2",
    "Number 3",
    "Number 4",
    "Number 5",
]

# Tuple variable
tuple_variable = (1, 0)
tuple_variable: tuple[int, int] = (1, 0)


# STRING FUNCTIONS
# ============================================================

# Convert the string to lowercase
string_variable.lower()

# Convert the string to uppercase and check if it's fully uppercase
string_variable.upper().isupper()

# Get the length of the string
len(string_variable)

# Access a specific character by index (0-based)
string_variable[0]

# Find the index of a specific character or substring (case-sensitive)
string_variable.index("W")  # Will raise ValueError if not found

# Replace all occurrences of a substring with another substring
string_variable.replace("i", "ey")

# Check if the string starts with a specific substring
string_variable.startswith("Hi")

# Check if the string ends with a specific substring
string_variable.endswith("python")

# Split the string into a list of words
string_variable.split()

# Strip whitespace from the beginning and end of the string
string_variable.strip()


# INT AND FLOAT FUNCTIONS
# ============================================================

# Convert an integer to a string
str(int_variable)

# Raise a number to a power (int_variable^2)
pow(int_variable, 2)

# Find the minimum value between int_variable and 4
min(int_variable, 4)

# Round the float variable to the nearest integer
round(float_variable)

# Find the absolute value of a number
abs(-int_variable)

# Find the maximum value between two or more numbers
max(int_variable, 4, 5)

# Convert a float to an integer (truncates decimal part)
int(float_variable)


# LIST FUNCTIONS
# ============================================================

# Access the first element of the list
list_variable[0]

# Access all elements from index 1 onwards
list_variable[1:]

# Access elements from index 1 to 2 (excluding index 3)
list_variable[1:3]

# Access the last element of the list
list_variable[-1]

# Extend the list by appending all elements from another list
list_variable.extend(list_variable)

# Add an element to the end of the list
list_variable.append("Number 6")

# Insert an element at a specific position
list_variable.insert(1, "Number 0.5")

# Remove a specific element from the list
list_variable.remove("Number 3")

# Remove and return the last element of the list
list_variable.pop()

# Sort the list in ascending order (works for numbers or strings)
list_variable.sort()

# Create a copy of the list
list_variable.copy()

# Count the occurrences of a specific element in the list
list_variable.count("Number 0")

# Reverse the order of the elements in the list
list_variable.reverse()

# Clear all elements from the list
list_variable.clear()

# TUPLE FUNCTIONS
# ============================================================

# Access the first element of the tuple
tuple_variable[0]

# Get the length of the tuple
len(tuple_variable)

# Count occurrences of a specific value in the tuple
tuple_variable.count(1)

# Find the index of a specific value in the tuple
tuple_variable.index(0)
