# BONUS
# 1. В этом задании мы будем отслеживать дни рождения наших друзей. Создайте
# dictionary с именами и датами друзей (кого угодно). При запуске программы вы должны
# ввести имя и после чего программа должна вернуть Имя + дата рождения.
# Взаимодействие должно выглядеть так:
# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.

def birth():
    
    birthday = {"Anna": "01/12/1996", "Emma": "23/07/1981", "John": "11/11/1991"}
    firstly = print("Welcome to the birthday dictionary. We know the birthdays of:")
    for key in birthday:    
        print(key)
        continue
    for key in birthday:
        your_friend = input("Who's birthday do you want to look up? ")
        if your_friend == key:
            print(key + "'s birtday is " + birthday[key])
            break

birth()