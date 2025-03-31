import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    print("합:", sum_recursive(n))
    print("팩토리얼:", factorial(n))