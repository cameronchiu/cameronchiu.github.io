import random

def guess_the_number():
  # Generate a random number between 1 and 10
  secret_number = random.randint(1, 10)

  # Ask the user to guess the number
  guess = int(input("Guess a number between 1 and 10: "))

  # Keep track of the number of guesses
  num_guesses = 1

  # Keep looping until the user guesses correctly
  while guess != secret_number:
    # Increment the number of guesses
    num_guesses += 1

    # Give the user a hint
    if guess > secret_number:
      print("Your guess is too high, try again.")
    else:
      print("Your guess is too low, try again.")

    # Get the user's next guess
    guess = int(input("Guess a number between 1 and 10: "))

  # If the loop exits, the user has guessed correctly
  print("Congratulations, you guessed the number in {} guesses!".format(num_guesses))

# Start the game
guess_the_number()
