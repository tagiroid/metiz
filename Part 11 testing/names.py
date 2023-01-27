from name_function import get_formatted_name


print('Enter "q" to quit.')
while True:
    first = input('\nFirst: ')
    if first == 'q':
        break
    last = input('\nLast: ')
    if last =='q':
        break

    formated = get_formatted_name(first, last)
    print(f'Formatted name: {formated}')

