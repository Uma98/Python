hard_coded = 50
guess_num = int(input('Enter a number'))

if guess_num > hard_coded:
    print(guess_num, "greater")
else:
    print(guess_num, "lesser")