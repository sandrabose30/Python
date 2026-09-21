# create an rpg game
import random

def game():
    playerhp = 100
    enemyhp = 100
    turn = 1
    while playerhp >= 0 and enemyhp >= 0:
        print(f"Turm{turn}")
        print("Player attacks enemy")
        playerhp = playerhp - random.randint(1,20)
        print(f"Player hp {playerhp}")
        enemyhp= enemyhp - random.randint(1,20)
        print(f"enemey hp {enemyhp}")
        if playerhp <= 0:
            print("enemey wins")
            break
        if enemyhp <= 0:
            print("player wins")
            break
        turn = turn + 1
game()


