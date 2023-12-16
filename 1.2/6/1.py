import json

def create_survey():
    survey = {}
    
    print("Анкетирование")
    print("Ответьте на следующие вопросы:")
    
    name = input("1. Ваше имя: ")
    age = input("2. Ваш возраст: ")
    survey['name'] = name
    survey['age'] = age
    
    print("3. Какие жанры фильмов вам нравятся?")
    genres = []
    while True:
        genre = input("Введите жанр или нажмите Enter, чтобы закончить: ")
        if genre == '':
            break
        genres.append(genre)
    survey['genres'] = genres
    
    print("4. Какие фильмы вы считаете своими любимыми?")
    movies = []
    while True:
        movie = input("Введите название фильма или нажмите Enter, чтобы закончить: ")
        if movie == '':
            break
        movies.append(movie)
    survey['favorite_movies'] = movies
    
    return survey

def save_survey_results(survey):
    #сохраняет
    with open('survey_results.json', 'a') as file:
        file.write(json.dumps(survey) + '\n')

def load_survey_results():
    # загружает
    try:
        with open('survey_results.json', 'r') as file:
            for line in file:
                survey = json.loads(line)
                print(f"Имя: {survey['name']}")
                print(f"Возраст: {survey['age']}")
                print(f"Любимые жанры: {', '.join(survey['genres'])}")
                print(f"Любимые фильмы: {', '.join(survey['favorite_movies'])}")
                print()
    except FileNotFoundError:
        print("Файл с результатами анкетирования не найден.")

def main():
    while True:
        print()
        print("1. Анкетирование")
        print("2. Просмотр результатов")
        print("3. Выход")
        
        choice = input("Выберите действие: ")
        
        if choice == '1':
            survey = create_survey()
            save_survey_results(survey)
            print("Результаты анкетирования сохранены.")
        elif choice == '2':
            load_survey_results()
        elif choice == '3':
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == '__main__':
    main()