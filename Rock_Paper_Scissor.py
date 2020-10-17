import random

def gameWin(comp, you):
    if comp == you:
        return None
    elif comp == "r":
        if you == "p":
            return True
        elif you == "s":
            return False
    elif comp == "p":
        if you == "s":
            return True
        elif you == "r":
            return False
    elif comp == "s":
        if you == "r":
            return True
        elif you == "p":
            return False




print("Comp turn: Rock(r), Paper(p), Scissor(s)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp = "r"
elif randNo == 2:
    comp = "p"
elif randNo == 3:
    comp = "s"

you = input("Your turn: Rock(r), Paper(p), Scissor(s)?")
a = gameWin(comp, you)
print(f"Computer choose: {comp}")
print(f"You choose: {you}")
if a == None:
    print("Tie")
elif a:
    print("You Win")
else:
    print("You Lose")