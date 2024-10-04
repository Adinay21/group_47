while True:
    word = input('Напишите слово на латинице или кириллице: ').lower()
    if word == 'выйти':
        break
    count_letters = 0
    count_glasnye = 0
    count_soglasnye = 0
    glasnye = 'aeiouyауоиэыяюе'
    for i in word:
        count_letters += 1
        if i in glasnye:
            count_glasnye += 1
        else:
            count_soglasnye += 1

    percent_glasnye = round(count_glasnye/count_letters * 100, 2)
    percent_soglasnye = round(count_soglasnye/count_letters * 100, 2)
    print(f'количество всех букв: {count_letters}')
    print(f'гласные: {count_glasnye}')
    print(f'согласные: {count_soglasnye}')
    print(f'процент гласных: {percent_glasnye}')
    print(f'процент соглансых: {percent_soglasnye}')

