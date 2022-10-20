import pandas as pd

movie_table = pd.DataFrame({
    "TITLE": ['Demon Slayer Movie: Infinity Train', 'A Silent Voice', 'Jujutsu Kaisen 0',
                'Kimi no Na wa (Your Name)', 'Doukyuusei (Classmates)', 'KazeTachinu (The Wind Rises)',
                'Kenpuu Denki Berserk (Berserk)', 'Piano no Mori (The Perfect World of Kai)', 'Mushishi'],
    "GENRE": ["Shonen", "Shonen", "Shonen", "Shoujo", "Shoujo", "Shoujo", "Seinen", "Seinen", "Seinen"],
    "RATING": [8.2, 8.1, 7.9, 8.4, 7.7, 7.7, 8.7, 7.1, 8.5],
    "YEAR": [2020, 2016, 2021, 2016, 2016, 2013, 1997, 2007, 2005]
})

series_table = pd.DataFrame({
    "TITLE": ['Fullmetal Alchemist', 'Hunter x Hunter', 'Jujutsu Kaisen',
              'Orange', 'Banana Fish', 'Bloom into You',
              'Berserk', 'Vinland Saga', 'Parasyte', 'Erased'],
    "GENRE": ["Shonen", "Shonen", "Shonen", "Shoujo", "Shoujo", "Shoujo", "Seinen", "Seinen", "Seinen", "Seinen"],
    "RATING": [9.1, 9, 8.6, 7.6, 8.2, 7.9, 6.3, 8.8, 8.3, 8.5],
    "YEAR": [2003, 2011, 2017, 2016, 2018, 2018, 1997, 2019, 2015, 2016]
})


#print(series_table)

movie_or_series = input("Would you like to watch a movie or a series? (movie/series) ").lower()

while sum != "yes":
    if movie_or_series == "movie":
        choose_genre_movie = input("Choose a genre you're interested in: Shonen, Shoujo, Seinen. ").lower()
        if choose_genre_movie == "shonen":
            list = movie_table[:2]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
        elif choose_genre_movie == "shoujo":
            list = movie_table[3:5]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
        elif choose_genre_movie == "seinen":
            list = movie_table[6:8]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
    elif movie_or_series == "series":
        choose_genre_series = input("Choose a genre you're interested in: Shonen, Shoujo, Seinen. ").lower()
        if choose_genre_series == "shonen":
            list = series_table[:2]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
        elif choose_genre_series == "shoujo":
            list = series_table[3:5]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
        elif choose_genre_series == "seinen":
            list = series_table[6:9]
            chosen_anime = list.sample(axis=0)
            print(f"We recommend you to watch - \n {chosen_anime}")
    else:
        print("Invalid input. Try again!")


    sum = input("Are you satisfied with your choice? (yes/no) ").lower()
    if sum == "yes":
        print("See you. Enjoy!")
        break
    elif sum == "no":
        continue