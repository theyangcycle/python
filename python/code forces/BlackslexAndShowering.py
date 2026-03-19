a = int(input())
for b in range(a):
    n = int(input())
    num = list(map(int,input().split()))
    sum = 0
    for i in range(1,n):
        sum += abs(num[i]-num[i-1])
    sums = []
    for i in range(n):
        if i == 0:
            newsum = sum-abs(num[i]-num[i+1])
        elif i == n-1:
            newsum = sum-abs(num[i]-num[i-1])
        else:
            newsum = sum-abs(num[i]-num[i-1])-abs(num[i]-num[i+1])+abs(num[i+1]-num[i-1])
        sums.append(newsum)
    print(min(sums))