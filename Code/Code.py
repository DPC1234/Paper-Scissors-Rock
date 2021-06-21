import random
counter = 0
psr = input("Would you like to play Paper, Scissors, Rock? The choices will be r, p and s which mean rock, paper,scissors. Type: ready when you are ready.")
if psr.lower() == "ready" :
    print("ok, now we will start playing Paper, Scissors, Rock")
user = input("Enter a choice (r, p, s): ")
possible_actions = ["r","p","s"]
computer = random.choice(possible_actions)
print(f"\nYou chose {user}, computer chose {computer}.\n")
