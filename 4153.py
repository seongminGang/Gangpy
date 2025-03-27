while True:
    number = list(map(int, input().split()))
    if number == [0, 0, 0]:
        break
    number.sort()

    if pow(number[0],2) + pow(number[1],2) == pow(number[2], 2):
        print("right")
    else:
        print("wrong")