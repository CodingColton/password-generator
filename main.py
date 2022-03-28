import random

password = []
character_options = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
                    'o','p','q','r','s','t','u','v','w','x','y','z',
                    '1','2','3','4','5','6','7','8','9','0']

password_length = int(input("How long do you want the password to be: "))

while True:
    password.append(password_length)

    password_length -= 1
    if password_length < 1:
        break

get_length = len(password)
item_number = 0

while item_number < get_length:  
    password[item_number] = random.choice(character_options)
    item_number += 1

print("\nYour generated password is: " + "".join(password))