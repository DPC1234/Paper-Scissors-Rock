import random
counter = 0
while True :
psr = input("Would you like to play Paper, Scissors, Rock? The choices will be r, p and s which mean rock, paper,scissors. Type: ready when     you are ready.")
if psr.lower() == "ready" :
    print("ok, now we will start playing Paper, Scissors, Rock")
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
elif user == "p":
    if computer == "r":
        print("Paper covers rock! You win!")
        counter = counter+1
    else:
        print("Scissors cuts paper! You lose.")
elif user == "s":
    if computer == "p":
        print("Scissors cuts paper! You win!")
        counter = counter+1
    else:
        print("Rock smashes scissors! You lose.")
play_again = input("Play again? (y/n): ")
if play_again.lower() != "y":
    print("Thanks for playing, you got a score of",counter)
