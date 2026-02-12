tuple = (1, 2, 3, 4, 5)
print(tuple[0]) # Accessing the first element of the tuple
#tuple[1] = 10 # This will raise an error because tuples are immutable
tuple_1 = (1, 2, [1,2,3], 4, 5)
tuple_1[2][0] = 10 # This will work because the list inside the tuple is mutable
print(tuple_1) # Output: (1, 2, [10, 2, 3], 4, 5)