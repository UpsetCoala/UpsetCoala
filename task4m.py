import random
def opponent(n):      
    print("Opponent's turn.")
    c = random.randint(3)
    n-=c
    print (f"Opponent has made it's turn. Number of rocks taken: {c}, number of rocks in the pile: {n}")
    turn = 1
def player(n):
    print ("It's your turn now. Choose amount of rocks you want to take")
    q=int(input())
    if q<1 or q>3:
        print("You have to take at least 1 rock and at most - 3")
        q = int(input())
    n=n-q
    print (f"You have taken {q} rocks from the pile. Number of rocks left: {n} ")
    turn = 2
    
n= random.randint(4, 30)
print(f"The game begins. Number of rocks in the pile is: {n}.")
turn = random.randint(1,2)
while n>4:
    if turn == 2:
        opponent(n)
    if turn == 1:
        player(n)
if turn == 2:
        print (f"Opponent has made it's turn. Number of rocks taken: {n-1}, number of rocks in the pile: 1") 
        print ("Opponent won! (I bet he was cheating. Try again, you'll surely make it!")
if turn == 1:
        player(n)
        if n<1: 
            print ("You can't leave less than 1 stone in the pile")
        print ("You won!")


