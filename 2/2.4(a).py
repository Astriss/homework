data = input("Enter text: ")
new_data=[]
string_data=''
def remove_exclamation_marks(data):
    for i in data:
        if i != '!':
            new_data.append(i)
    return new_data
   

data = remove_exclamation_marks(data)
print("".join(data))


