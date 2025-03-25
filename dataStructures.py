# Create an empty list called my_list
my_list = []

# Append elements to my_list 
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Insert the value 15 at the second position in the list
my_list.insert(1, 15)

# Create another list to extend my_list
my_second_list = [50, 60, 70]

# Extend my_list with another list
my_list.extend(my_second_list)

# Remove the last element from my_list
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find and print the index of the value 30 in my_list
print(my_list.index(30))