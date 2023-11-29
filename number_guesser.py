from random import randint

low = 1
high = 50

guesses_left = 5
random_number = randint(low, high)

while True:
    print(random_number)
    print("I'm thinking of a number between {} and {}".format(low, high))
    print("You have {} guesses left".format(guesses_left))
    guess = int(input("Enter your guess: "))

    if guess == random_number:
        print("You Win")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            guesses_left = 5
            random_number = randint(low, high)
            continue
        else:
            print("Goodbye!")
            break
    elif guess > random_number:
        print("Correct answer is smaller!")
    elif guess < random_number:
        print("Correct answer is greater!")

    guesses_left -= 1

    if guesses_left == 0:
        print("You lose!")
        play_again = input("Do you want to play again? (y/n): ")
        if play_again == "y":
            guesses_left = 5
            random_number = randint(low, high)
            continue
        else:
            print("Goodbye!")
            break
        
        