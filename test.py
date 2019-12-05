#-*- encoding:utf-8 -*—
while True:
    try:
        x = int(input('Please enter a number:'))
        break
    except ValueError:
        print('Not a valid number.Try again...')
print('Your number is:', x)