my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
print("Tuple:", my_tuple)
print("List:", my_list)

# Step 3: Update the list
my_list.append(60)      # Add an element
my_list[1] = 25         # Modify an element
my_list.remove(40)      # Remove an element

# Step 4: Print updated list
print("Updated List:", my_list)

# Step 5: Convert the list back to a tuple
updated_tuple = tuple(my_list)

# Step 6: Print the final tuple
print("Updated Tuple:", updated_tuple)

del my_tuple
print(my_tuple)

