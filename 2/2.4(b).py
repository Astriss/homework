data = input("Enter text: ")
new_data = ''


def remove_last_em(data):
        l = len(data)
       
        if data[-1] != '!':
            new_data = data
        else:
              l = l-1
              new_data = data[:l]
        return new_data

print(remove_last_em(data))
    

