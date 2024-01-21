addition=0
while addition<=100:
    player_1=int(input("player_1:"))
    addition += player_1
    if addition>=100:
        print("player_1 is the winner")
        break
    player_2=int(input("player_2:"))
    addition +=player_2
    if addition>=100:
        print("player_2 is the winner")
        break
    print("a=",addition)
