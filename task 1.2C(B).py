import random
my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

lasting = my_favorite_songs_dict.values()
time1 = random.choice(list(lasting))
time2 = random.choice(list(lasting))
time3 = random.choice(list(lasting))

time=time1 + time2 + time3
print(f'Three random songs last {time} minutes')