"""
Dictionary 

collection -- key+value = pair = data1

left-side = key
right-side = value

{key1: value1, key2: value2}
"""

# var = {'key1': 100, 'key2': 200}
# print(var)


# Create a Student Grade System.

"""
add
update
delete
view
exit
"""

# items: items methods jo bhi key value ki form mai ap ke dictionry pe element present hain on ko display karday ga.

# create a dictionary

students = {
    'Haris': 100,
    'Qasim': 200
}

# Accessing a element (If you want to display value is dictionary you should access its key)
print(students['Qasim'])


# Update
students['Qasim'] = 300
print(students)


# Delete
del students['Haris']
print(students)