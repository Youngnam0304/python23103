#ChatGPT로 생성한 코드

# List, Tuple, Set, and Dict Comparison Demo

# Lists
my_list = [1, 2, 3, 4, 5]

# Tuples
my_tuple = (1, 2, 3, 4, 5)

# Sets
my_set = {1, 2, 3, 4, 5}

# Dictionaries
my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}

# List vs Tuple
list_vs_tuple = my_list == list(my_tuple)
print(f"List vs Tuple: {list_vs_tuple}")

# List vs Set
list_vs_set = set(my_list) == my_set
print(f"List vs Set: {list_vs_set}")

# List vs Dict
list_vs_dict = False  # Lists cannot be directly compared to dictionaries
print(f"List vs Dict: {list_vs_dict}")

# Tuple vs Set
tuple_vs_set = set(my_tuple) == my_set
print(f"Tuple vs Set: {tuple_vs_set}")

# Tuple vs Dict
tuple_vs_dict = False  # Tuples cannot be directly compared to dictionaries
print(f"Tuple vs Dict: {tuple_vs_dict}")

# Set vs Dict
set_vs_dict = False  # Sets cannot be directly compared to dictionaries
print(f"Set vs Dict: {set_vs_dict}")
