import random

while True:
    a=input("Enter the choice:")
    b=["rock","scissor","papper"]
    c=random.choice(b)
    print("your choice:",a,"computer choice",c)
    if(a==c):
        print("Both players selected",a,"it is tie")
    elif(a=="rock"):
        if(c=="papper"):
            print("papper covers rock : you lose")
        else:
            print("scissors cuts papper: you win")
    elif(a=="papper"):
        if(c=="scissor"):
            print("scissor cuts papper: you lose ")
        else:
            print("rock smasches scissor: you win")
    elif(a=="scissor"):
        if(c=="rock"):
            print("rock smasches scissor: you lose")
        else:
            print("scissor cuts papper: you win")
    p=input(" Do you play Again:")
    if (p!="yes"):
        break
            
    
    
