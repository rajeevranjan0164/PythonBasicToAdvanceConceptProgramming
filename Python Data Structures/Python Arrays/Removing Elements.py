import array
a = array.array('i', [1, 2, 3, 1, 5])

# remove first occurence of 1
a.remove(1)
print(a)

# remove item at index 2
a.pop(2)
print(a)