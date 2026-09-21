import random
# dice game
def dice(intial_throw):
    count = 0
    for i in range(intial_throw):
        player_throw = random.randint(1,6)
        count = count + player_throw
    return count

def dicegame():
    intial_throw1 = random.randint(1,6)
    print(intial_throw1, "player1 intial throw")
    player1 = dice(intial_throw1)
    intial_throw2 = random.randint(1,6)
    print(intial_throw2, "player2 intial throw")
    player2 = dice(intial_throw2)
    if player1 > player2:
        print("Player 1 wins!, player1 got " + str(player1) + " and player2 got " + str(player2))
    elif player1 < player2:
        print("Player 2 wins!, player2 got " + str(player2) + " and player1 got " + str(player1))
    else:
        print("It's a tie!")

dicegame()