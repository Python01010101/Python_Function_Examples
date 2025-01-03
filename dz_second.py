import sys
sys.stdout.reconfigure(encoding='utf-8')
import array

my_music_favorite = ["rap","rock","djaz"]
my_music_favorite.append("fonk")
print(my_music_favorite)


#картеж

# Создаем список координат
cities_coordinates = [
    {"city": "Москва", "latitude": 55.7558, "longitude": 37.6173},
    {"city": "Санкт-Петербург", "latitude": 59.9343, "longitude": 30.3351},
    {"city": "Казань", "latitude": 55.8304, "longitude": 49.0661},
    {"city": "Астрахань", "latitude": 46.3493, "longitude": 48.0364}
]

# Используем переменную
for city in cities_coordinates:
    print(f"{city['city']} - Широта: {city['latitude']}, Долгота: {city['longitude']}")



#словарь

am_data ={
    "name": "Ivar",
    "age" : 21,
    "profession" : "Python Developer",
    "where_lives" : "Bishkek"
}
print(am_data)


popular_countries = ["Россия (СССР)", "Соединенные Штаты Америки (США)", "Германия", "Индия", "Великобритания"]

popular_countries.append("Франция")


popular_personalities = ["Юрий Гагарин", "Джон Ф. Кеннеди", "Альберт Эйнштейн", "Махатма Ганди", "Уинстон Черчилль"]

popular_personalities.append("Шарль де Голль")


all_data = popular_countries + popular_personalities
print(all_data)



# Список фильмов  в избранном
favorite_movies = ["Inception", "The Matrix", "Interstellar"]


# Добавляем новый фильм
favorite_movies.append("Avatar 2")


# Вывод всех фильмов
for movie in favorite_movies:
    print (movie) 


# Информация о фильме
movie_detals = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "release_year": 2010,
    "rating": 8.8
}


# Доступ к информации
print(f"{movie_detals ['title']} ({movie_detals['release_year']}) ({movie_detals['director']}) ({movie_detals['rating']})")



# Координаты кинотеатра
cinema_location = (55.7558, 37.6173)  # Москва

# Вывод координат
latitude, longitude = cinema_location
print(f"Кинотеатр находится по координатам: {latitude}, {longitude}")


# Уникальные жанры фильмов
ganres = {"Action", "Comedy", "Drama", "Sci-Fi"}


# Добавляем новый жанр
ganres.add("Horror")


# Проверяем наличие жанра
print("Horror" in ganres)

# Массив оценок фильма
ratings = array.array("f", [6.6, 8.7, 9.0, 8.8])


# Добавляем новую оценку 
ratings.append(4.5)


# Средний рейтинг
avarage_rating = sum(ratings) / len(ratings)
print(avarage_rating)

