movies = {
    "Memoirs of a Geisha": {
        'Adinay': 10,
        'Aizhan': 8,
        'Alina': 4
    },
    "Poor things": {
        'Aidai': 9,
        'Dima': 7,
        'Nursultan': 5
    }
}

while 1:
    def add_movies(movies):
        movie_name = input('Введите название фильма: ').capitalize()
        if movie_name in movies:
            print('Такой фильм уже существует')
        elif not movie_name in movies:
            movies.update({movie_name: {'Введите название нового фильма: '}})
        else:
            print('Не корректно')
        return movie_name

    add_movies(movies)

    def rating_movies(movies):
        movie_name = input('Введите название фильма: ')
        if not movie_name in movies:
            print('Такого фильма не сущевтует')
        if movie_name in movies:
            movies.update({movie_name: {'Введите свое имя и оценку фильма: '}})
            print('Ваш рейтинг добавлен')
        return movie_name

    rating_movies(movies)

    def watch_rating_movies(movies):
        for movies in movies:
            if movies.values() in movies:
                average_rating = sum(movies.values.values())/len(movies.values)
            elif not movie_name in movies:
                print('У этого фильма нет рейтинга')
            else:
                print('Не корректно')
        return movies

    watch_rating_movies(movies)


