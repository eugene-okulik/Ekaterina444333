win_number = 5
while True:
    user_number = int(input('Enter random number: '))
    if user_number != win_number:
        print('Try again')
    else:
        print('Congratulations! You guessed the correct number!')
        break
