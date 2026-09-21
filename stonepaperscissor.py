import random
ch=["rock","paper","scissors"]
computer = random.choice(ch)
player = ''
while player not in ch:
    player=input("enter your choice rock/paper/scissor: ").lower()
print(f"player chose {player} and computer chose {computer}")
if player== computer:
    print("It's a tie")
elif player== "rock":
    if computer=="scissors":
        print("Computer wins")
    else:
        print("Player wins")
elif player== "paper":
    if computer=="scissors":
        print("Computer wins")
    else:
        print("Player wins")
elif player== "rock":
    if computer=="paper":
        print("Computer wins")
    else:
        print("Player wins")