


min = 0
max = 100
print(f'Загадайте число от {min} до {max}')

while True:
    num = min + (max - min) // 2
    number = input(f'Ваше число больше {num}? (да или нет): ') == 'да'
    if number:
        min = (num, max)[min == num]
    else:
        max = num
    if min == max:
        print(f'Ваше число: {max}')
    with open ('results.txt', 'a') as file:
        file.write(str(num) + '\n')

