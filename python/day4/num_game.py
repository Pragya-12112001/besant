# guss the number game
# randomly computer select teh number between 1 and 20
# display welcom message
# max attemps - 6
#  if less then print too less
#  if more then print too high
  
import random

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 20.")
print("You have 6 attempts to guess the correct number.")

attempts = 6
num = random.randint(1, 20)

# while attempts >= 1:
#     guess = int(input("Enter a number between 1 and 20: "))

#     attempt_number = 7 - attempts

#     if guess == num:
#         print(f"Congratulations! You guessed the correct number: {num}")
#         print(f"You guessed it correctly on attempt {attempt_number}!")
#         break

#     elif guess < num:
#         print("Too low! Try a higher number.")

#     else:
#         print("Too high! Try a lower number.")

#     attempts -= 1


for attempt in range(1, 7):
    guess = int(input("Enter a number between 1 and 20: "))

    if guess == num:
        print(f"Congratulations! You guessed the correct number: {num}")
        print(f"You guessed it correctly on attempt {attempt}!")
        break

    elif guess < num:
        print("Too low! Try a higher number.")

    else:
        print("Too high! Try a lower number.")

else:
    print("Sorry, you've run out of attempts!")
    print(f"The correct number was {num}.")