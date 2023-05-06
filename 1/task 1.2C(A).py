import random
my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]
song1, song2, song3 = random.choice(my_favorite_songs), random.choice(my_favorite_songs),random.choice(my_favorite_songs)
time1 = float(song1[1])
time2 = float(song2[1])
time3 = float(song3[1])
time = time1 + time2 + time3


print(f'Three random songs last {time} minutes')