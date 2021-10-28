import random 

def start():    
    print('I am thinking of a 2 digit number. Guess the number.')
    print('Here are some clues. When I say PICO, it means one digit is correct but in he wrong place.')
    print('when I say FERMI, it means one digit is correct and in the correct position')
    print('when I say BAGELS, no digits are correct.')
    print('guess below')
num_guess = input('Your guess:')
num_guess_split = [int(a) for a in str(num_guess)]
number = random.randint(10,99)
number_split = [int(a) for a in str(number)]
# print(number)
# print(number_split)

def check_digits(num_guess_split, number_split):
    for i in num_guess_split:
        if num_guess_split[i] == number_split[i]:
            print('FERMI')
        elif num_guess_split[i] == number_split[0,2]:
            print('PICO')
        else:
            print('BAGELS')

start()  
check_digits(num_guess_split, number_split)


# https://inventwithpython.com/bigbookpython/project1.html