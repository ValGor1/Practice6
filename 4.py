list = str.maketrans('abcdefgh', '12345678')
input = input().translate(list)
count = sum(map(int, input))
if count%2 == 0:
    print('черный')
else:
    print('белый')