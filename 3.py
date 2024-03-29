N, M = map(int, input().split('x'))
K = int(input())
if ((N * M) - K ) % 2 == 0:
    print('успешно')
else:
    print('неосуществимо')