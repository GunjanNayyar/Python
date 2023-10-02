ages =  [29, 22 13]

print(ages)
# list with elements of different data types
list1 = [1, "Morning", 14.46]

# list with duplicate elements
list1 = [10, "Morning", 13.34, "Morning", 10]

# empty list
list3 = []
languages = ["Python", "Java", "C++"]

# access item at index 0
print(languages[0])   # Python

# access item at index 2
print(languages[2])   # C++
languages = ["Python", "Java", "C++"]

# access item at index 0
print(languages[-1])   # C++

# access item at index 2
print(languages[-3])   # Python


# List slicing in Python

my_list = ['p','r','o','g','r','a','m','i','z']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])
numbers = [21, 34, 54, 12]

print("Before Append:", numbers)

# using append method
numbers.append(38)

print("After Append:", numbers)