x = int(input('Введите номер: '))
k = 0
for n in range(0, x+1):
    k += len(str(n))
    if k >= x:
        if x % 2 == 0 and x > 10:
            print(n % 10)
        elif x % 2 != 0 and x > 10:
            print(n // 10)
        else:
            print(n)
        break