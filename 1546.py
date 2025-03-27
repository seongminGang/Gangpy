n = int(input())
num = list(map(float, input().split()))

myMax = max(num)
sum = sum(num)

print(sum * 100 / myMax / int(n))