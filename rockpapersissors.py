player_1=input("choose your weapon")
player_2=input("choose your weapon")
if player_1=="rock" and "player_2"=="sissors":
    print("player one wins, click play for next battle")
elif player_1=="sissors" and player_2=="paper":
    print("player one wins, click play for next battle")
elif player_1=="paper" and player_2=="rock":
    print("player one wins, click play for next battle")
elif player_2=="sissors" and player_1=="paper":
    print("player two wins, click play for next battle")
elif player_2=="rock" and player_1=="sissors":
    print("player two wins, click play for next battle")
elif player_2=="paper" and player_1=="rock":
    print("player two wins, click play for next battle")
elif player_1=="rock" and player_2== "rock":
    print("draw, click play for next battle")
elif player_1=="sissors" and player_2=="sissors":
    print("draw, click play for next battle")
elif player_1=="paper" and player_2=="paper":
    print("draw, click play for next battle")