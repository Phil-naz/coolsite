print('Create a tuple')
tuplex = (4, 6, 2, 8, 3, 1)
print(tuplex)

print('\nAdd an element to the end of the tuple')
tuplex = tuplex + (9,)
print(tuplex)

print('\nAdd elements to a specific position')
tuplex = tuplex[:5] + (15, 20, 25) + tuplex[:5]
print(tuplex)

print('\nConvert tuple to list, add items to list, then convert list to tuple')
listx = list(tuplex)
listx.append(30)
tuplex = tuple(listx)
print(tuplex)