numbers = {
'1': 'one',
'2': 'two',
'3': 'three',
'4': 'four',
'5':'five',
'6':'six',
'7':'seven',
'8':'eight',
'9':'nine',
}

num = input("Enter the number: ")
def switch_it_up(number):
 result = numbers[num]
 return result
try:
    your_number = switch_it_up(num)
    print(your_number)
except KeyError:
   print("None")