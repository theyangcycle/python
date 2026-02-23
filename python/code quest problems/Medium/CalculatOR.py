from decimal import Decimal, ROUND_HALF_UP
def round(x):
    return Decimal(x).quantize(Decimal('0.0'), rounding=ROUND_HALF_UP)

a = int(input())
for b in range(a):
    num1,op,num2 = input().split()
    num1 = int(num1)
    num2 = int(num2)
    if op == '+':
        print(round(num1+num2),end=' ')
        print(round(num2+num1))
    elif op == '-':
        print(round(num1-num2),end=' ')
        print(round(num2-num1))
    elif op == '*':
        print(round(num1*num2),end=' ')
        print(round(num2*num1))
    else:
        print(round(num1/num2),end=' ')
        print(round(num2/num1))