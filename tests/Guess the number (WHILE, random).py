import random
target_num = random.randint(1, 10)
guess_num = 0
while target_num != guess_num:
    guess_num = int(input('Угадайте число между 1 и 10: '))
print('Верно!')