import json


def stored():
    filename = '../Data/numbers.json'
    try:
        with open(filename) as f:
            user = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return user

def get_new():
    user = input('What is your name? ')
    filename = '../Data/numbers.json'
    with open(filename, 'w') as f:
        json.dump(user, f)
    return user

def greet_user():
    user = stored()
    if user:
        print(f'Welcome back, {user}')
    else:
        user = get_new()
        print(f'We will remember you, {user}')


greet_user()