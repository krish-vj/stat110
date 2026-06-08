#params: N, i, p
import random
def win(N=100, i=50, p=0.5):
    if (i==0):
        return 0
    if (i==N):
        return 1
    if random.random() <p:
        return win(N, i+1, p)
    else:
        return win(N, i-1, p)
trials=int(input("Enter number of trials: "))
N=int(input("Enter total capital on table: "))
i=int(input("Enter total capital of player A: "))
p=float(input("Enter prbability of A winning a round: "))
c=0
for _ in range(trials):
    c+=win(N, i, p)
print(f"A won: {c} out of {trials} times; prob={c/trials}")