from utilities import *

drawing_asc2 =''' 
  ___                              _       ___                       _           
 | _ \__ _ _______ __ _____ _ _ __| |___  / __|___ _ _  ___ _ _ __ _| |_ ___ _ _ 
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` (_-< | (_ / -_) ' \/ -_) '_/ _` |  _/ _ \ '_|
 |_| \__,_/__/__/\_/\_/\___/_| \__,_/__/  \___\___|_||_\___|_| \__,_|\__\___/_|  
                                                                                                                                                                                                                                                                                                
'''
print('\033[32m' + drawing_asc2 + '\033[0;0m')


# Data entry and some checks take place
while True:
    try:
        passwords = int(input('How many passwords do you want? '))
        lenght = int(input('''What lenght for the passwords \033[31m(Min = 4)\033[0;0m? '''))
        if passwords < 1  or lenght < 1:
            print('\033[31m' + 'ERROR: Use positives numbers' + '\033[0;0m')
            continue
        if lenght < 4:
            print('\033[31m' + 'ERROR: lenght below 4 is not accepted ' + '\033[0;0m')
            continue
        if lenght < 8:
            print('\033[32m' + 'Tip: use passwords with at least 8 characters' + '\033[0;0m')
        break
    except ValueError:
        print('\033[31m' + 'ERROR: Use integers numbers' + '\033[0;0m')

list_passwords =[]

# Generator working
while len(list_passwords) < passwords:
    genereted_password = ''
    for _ in range(lenght - 1):
        genereted_password += give_char()
    genereted_password += give_special_char()

    if check_password(genereted_password): # The password needs to meet some requirements
        list_passwords.append(genereted_password)

for passwords in list_passwords:
    print(passwords)

save_password(list_passwords)