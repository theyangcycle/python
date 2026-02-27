'''from fractions import Fraction
import copy
a = int(input())
for b in range(a):
    x,n = list(map(int,input().split()))
    tanks = list(map(int,input().split()))
    tanks1 = copy.deepcopy(tanks)
    x = Fraction(x)
    while x > 0:
        no0 = [i for i in tanks1 if i > 0]
        if x/len(no0) >= min(no0):
            x -= min(no0)*len(no0)
            for k in range(len(tanks1)):
                if tanks1[k] > 0:
                    tanks1[k] -= min(no0)
        else:
            val = Fraction(x,len(no0))
            x -= val*len(no0)
            for k in range(len(tanks1)):
                if tanks1[k] > 0:
                    tanks1[k] -= val
    for j in range(len(tanks)):
        print(Fraction(tanks[j]-tanks1[j]),end=' ')
    print()'''

from fractions import Fraction

t = int(input())
for _ in range(t):
    x, n = map(int, input().split())
    tanks = list(map(int, input().split()))
    remaining = [Fraction(c) for c in tanks]
    fuel = Fraction(x)

    while fuel > 0:
        unfilled = [i for i in range(n) if remaining[i] > 0]
        equal_share = fuel / len(unfilled)
        min_remaining = min(remaining[i] for i in unfilled)

        if equal_share >= min_remaining:
            for i in unfilled:
                remaining[i] -= min_remaining
            fuel -= min_remaining * len(unfilled)
        else:
            for i in unfilled:
                remaining[i] -= equal_share
            fuel = Fraction(0)

    result = [Fraction(tanks[i]) - remaining[i] for i in range(n)]
    print(' '.join(str(r) for r in result))