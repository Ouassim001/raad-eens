import random
random = random.randint(1,1001)

secret_number = "20"
guess = ""
guess_count = 0
guess_limit = 10
guess_rounds = 20
out_of_guesses = False


while guess != secret_number and not (out_of_guesses):
    guess = input("enter a number: ")
    if  guess_count < guess_limit:
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("no more guesses. You Lose ")
else:
    print("you guessed the number! ")
