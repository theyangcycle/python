from decimal import Decimal,ROUND_HALF_UP
a = int(input())
for b in range(a):
    f0,f1,f2,quality = list(map(float,input().split()))
    quality = int(quality)
    if f2 > 9.99:
        print(max(1,quality-2))
    elif f2 > 9.44:
        x1 = Decimal(f0 + (3/2) * (f2-f0)).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
        x2 = Decimal(f1 + 2 * (f2-f1)).quantize(Decimal('0.00'),rounding=ROUND_HALF_UP)
        if max(x1,x2) > 9.99:
            print(max(1,quality-2))
        else:
            print(quality)
    elif max(f0,f1,f2) < 7.77:
        print(min(10,quality+1))
    else:
        print(quality)