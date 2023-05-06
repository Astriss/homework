months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31

}

month = int(input('Type month number: '))
if month>0 and month<=12:
    print(months.get(month))
    
else:
    print("There is no month with this number!")