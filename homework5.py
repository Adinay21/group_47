while 1:
    country_flags = {'kg': {'red', 'yellow'},
                     'ru': {'red', 'blue', 'white'},
                     'kz': {'blue', 'yellow'},
                     'ps': {'red', 'green', 'white', 'black'},
                     'tr': {'red', 'white'}}


    color = input("Введите нужный цвет или выйти: ").lower()

    if color == 'выйти':
        break


    for i in country_flags:
        if color in country_flags[i]:
            print(i)


else:
    print('Введите цвет правильно!')





