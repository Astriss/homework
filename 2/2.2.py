quartal = {
'january': 'first quartal',
'february': 'first quartal',
'march': 'first quartal',
'april': 'first quartal',
'may':'second quartal',
'june':'second quartal',
'july':'second quartal',
'august':'second quartal',
'september':'third quartal',
'october':'third quartal',
'november':'third quartal',
'december': 'third quartal'
}

month = input("Enter the month: ")
def get_quartal(month):
 result = quartal[month]
 return result
your_quartal = get_quartal(month)
print(f"{month} is the part of a {your_quartal}")
