# GOT name generator
import random
y = open("RAWGOT.txt")
k = y.read()
k = k.split(",")
X = []
T = []
for i in k:
    W = ""
    for v in i:
        if v.isspace() or v.isalpha():
            W += v
    X.append(W)
for i in X:
    T.append(i.strip())
first = []
last = []
for i in T:
    if " " in i:
        Q = i.index(" ")
        first.append(i[:Q])
    else:
        first.append(i)
for i in T:
    if " " in i:
        Q = i.index(" ")
        last.append(i[Q:])

while input != "n":
    Rfirst = random.randint(0, len(first))
    Rlast = random.randint(0, len(last))
    print(first[Rfirst] + last[Rlast])

    input("Go again?")
    
