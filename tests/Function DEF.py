def reversing(string):
    result_string = ''
    for i in range(len(string)-1, -1, -1):
        result_string += string[i]
    return result_string

print('Reversing: ', reversing('world'))

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

print('Multiplication: ', multiply((8, 2, 3, -1, 7)))

def printScores(student, *scores):
   print(f"Student Name: {student}")
   for score in scores:
      print(score)
printScores("Jonathan",100, 95, 88, 92, 99)