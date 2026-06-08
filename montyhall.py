import random 
#it was always obvious to me (after seening the scale to million doors eg), simulating for mom
def winn(switch=True, doors=3):
    actualWin=random.randint(1, doors)
    choice=random.randint(1, doors)
    if (switch==True):
        if (choice==actualWin):
            #and they switched so they lose
            return 0
        else:
            return 1
n=int(input("Enter number of trials:"))
st=bool(input("Enter 1 for switch strat, 0 for no switch strat:"))
d=int(input("Enter number of doors:"))
c=0
for t in range(n):
    c+=winn(st, d)
print(c/n)



