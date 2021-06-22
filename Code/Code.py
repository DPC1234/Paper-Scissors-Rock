import random
counter = 0

psr = input("Would you like to play Rock, Paper, Scissors? The choices will be r, p and s which mean rock, paper and scissors. Type: ready when you are ready.")
if psr.lower() == "ready" :
        print("ok, now we will start playing Paper, Scissors, Rock")
while True :
    user = input("Enter a choice (r, p, s): ")
    possible_actions = ["r","p","s"]
    computer = random.choice(possible_actions)
    print(f"\nYou chose {user}, computer chose {computer}.\n")
    if user == computer:
        print(f"Both players selected {user}. It's a tie!")
    elif user == "r":
        if computer == "s":
            print("Rock smashes scissors! You win!")
            counter = counter+1
        else:
            print("Paper covers rock! You lose.")
            counter = counter-1
    elif user == "p":
         if computer == "r":
            print("Paper covers rock! You win!")
            counter = counter+1
         else:
            print("Scissors cuts paper! You lose.")
            counter = counter-1
    elif user == "s":
        if computer == "p":
            print("Scissors cuts paper! You win!")
        counter = counter+1
    else:
        print("Rock smashes scissors! You lose.")
        counter = counter-1

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing, you got a score of",counter)
        break
