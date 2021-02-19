i = 0
asal = [2, 3, 5, 7, 11, 13, 17, 19, 23]
codex = [[[],[],[]],[[],[],[]],[[],[],[]]]
if i <= 9:
    for j in range(0,3):
        for k in range(0,3):
            codex[j][k] = asal[i]
            i += 1
for i in range(0,3):
    print(codex[i])