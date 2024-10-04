

monday = float (input ('Введите расход за понедельник '))
tuesday = float (input ('Введите расход за вторник '))
wednesday = float (input ('Введите расход за среду '))
thursday = float (input ('Введите расход за четверг '))
friday = float (input ('Введите расход за пятницу '))
saturday = float (input ('Введите расход за субботу '))
sunday = float (input ('Введите расход за воскресенье '))

summa = monday + tuesday + wednesday + thursday + friday + saturday + sunday
print (f'Общая сумма {summa}')

average = round((summa/7), 1)

print(f'Средний расход: {average}')

if average > 1 < 500:
    print('мало потрачено')
elif average >= 501 and average >= 1500:
    print('потратили средне')
elif average >= 1501 and average >= 50000:
    print('потратили много')

else:
    print('ничего не потрачено')
