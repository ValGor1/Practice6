A = [0, 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
step1, step2 = input('Входные данные: ').split('-')
x1, y1 = A.index(step1[0]), int(step1[1])
x2, y2 = A.index(step2[0]), int(step2[1])

if abs(x1 - x2) * abs(y1 - y2) == 2:
    print("верно")
else:
    print("ошибка")