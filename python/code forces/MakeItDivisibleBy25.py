a = int(input())
for b in range(a):
    n = input()
    best = []
    count = 0
    boo = False
    for i in range(len(n)-1,-1,-1):
        if n[i] == '0':
            count += len(n)-1-i
            for j in range(i-1,-1,-1):
                if n[j] == '0' or n[j] == '5':
                    count += i-(j+1)
                    boo = True
                    break
            break
    if boo:
        best.append(count)
    count = 0
    boo = False
    for i in range(len(n)-1,-1,-1):
        if n[i] == '5':
            count += len(n)-1-i
            for j in range(i-1,-1,-1):
                if n[j] == '2' or n[j] == '7':
                    count += i-(j+1)
                    boo = True
                    break
            break
    if boo:
        best.append(count)
    print(min(best))