print('Enter two numbers to add them:')
ans = ''

while not ans:
    try:
        a = int(input('Number 1: '))
    except ValueError:
        print('Enter integer!')
        continue
    try:
        b = int(input('Number 2: '))
    except ValueError:
        print('Enter int, not string')
        continue
    else:
        ans = a + b
        print(ans)

