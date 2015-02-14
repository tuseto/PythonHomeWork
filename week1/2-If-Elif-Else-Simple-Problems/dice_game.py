from random import randint

N=int(input("Dice`s sides: "))

firstplayer_name=input("Enter first player name: ")
secondplayer_name=input("Enter second player name: ")

firstplayer_throw=randint(1,N)
secondplayer_throw=randint(1,N)

print(firstplayer_name+" rolls: "+str(firstplayer_throw))
print(secondplayer_name+" rolls: "+str(secondplayer_throw))

if firstplayer_throw>secondplayer_throw:
    print(firstplayer_name+" WINS!")
elif firstplayer_throw<secondplayer_throw:
    print(secondplayer_name+" WINS!")
else:
    print("TIE!")
    
