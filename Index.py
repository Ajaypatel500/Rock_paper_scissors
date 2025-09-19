import random
move = random.choice(['rock', 'paper', 'scissors'])
keep_playing = True
while keep_playing == True:
    user = input("Enter rock, paper, or scissors: ")
    print("The computer plays: " + move)
    if user == move:
        print("It's a tie!")
    elif user == 'rock':
        if move == 'scissors':
            print("You win!")
        else:
            print("You lose!")
    elif user == 'paper':
        if move == 'rock':
            print("You win!")
        else:
            print("You lose!")
    elif user == 'scissors':
        if move == 'paper':
            print("You win!")
        else:
            print("You lose!")
    else:
        print("Invalid input. Please try again.")
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        keep_playing = False
        print("Thanks for playing!")





