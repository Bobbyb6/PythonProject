# Password/username project

#import pandas as py


def get_attempted_username():
    return input('Enter Username: ')


def get_attempted_password():
    return input('Enter Password: ')


def get_stored_password():
    try:
        return data[attempted_username]
    except KeyError:
        print('This Username is not recognised Enter a valid Username!')


def check_passwords_are_equal():
    return password == attempted_password


data = {'Bobby_96': 'Password1', 'Gamer101': 'Xboxxx2021', 'dave000': 'GUESS', 'ExAmPlE1': 'passworddude'}
print('_____Log in dashboard_____')
attempts = 0
while attempts < 3:
    attempted_username = get_attempted_username()
    attempted_password = get_attempted_password()
    password = get_stored_password()
    if check_passwords_are_equal():
        print('Logged in')
        break
    else:
        print('Incorrect Username or Password')
        attempts = attempts + 1
    if attempts == 3:
        print("Maximum attempt's reached you are locked out see further assistance")


# add pandas data or something to input like a proper program