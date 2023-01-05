print('Collecting unique values')
myList = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
mySet = set(myList)
print('Unique values: ', mySet)

print('or')

a = [9, 1, 5, 9, 4, 2, 7, 2, 9, 5, 3]
b = []
for i in range(0, len(a)):
    if a.count(i) == 1:
        b.append(i)

print('Unique values: ', b)