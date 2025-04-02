import sys

n = int(sys.stdin.readline().strip())
for i in range(1, n + 1):
    words = sys.stdin.readline().strip().split()
    reversed_words = ' '.join(reversed(words))
    print(f"Case #{i}: {reversed_words}")
