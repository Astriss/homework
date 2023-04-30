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
time1, time2, time3 = (my_favorite_songs_dict['Waste a Moment']), (my_favorite_songs_dict['In This World']), (my_favorite_songs_dict['A Sorta Fairytale'])
time=time1 + time2 + time3
print(f'Three songs last {time} minutes')