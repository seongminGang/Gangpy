N = int(input())
spaceCnt = N-1

for i in range(1, N*2, 2):
    print(' ' * spaceCnt+'*' * i)
    spaceCnt -= 1
    
for i in range(N*2-3, 0, -2):
    spaceCnt += 1
    print(' ' * spaceCnt, '*' * i)