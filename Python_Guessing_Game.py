import random

print ("welcome to the number guessing game")

print ("i am thinking of a number between 1 and 100")

number = random.randint(1, 100)

easy_hard = input ("choose a difficulty type 'east' or 'hard' "). lower()

lives = 10
if easy_hard == "hard":

    lives = 5
    print ("you have 5 attempts remaining to guess the number ")

else:
      print("you have 10attempts remaining to guess the number:")

      while True:
            if lives == 0:
                break
            guess = int(input("make a guess: " ))

            if guess == number:

                print (f"you got it: the answer was {number}")
                break

            elif guess < number:

              print("Too low")

              print("guess again")

              lives -= 1

              print(f"you have {lives }attempts remaining to guess the number")

            elif guess > number:

              print("Too high")

              print("guess again")

              lives -= 1

              print (f"you have {lives} attempts remaining to guess  the number")
