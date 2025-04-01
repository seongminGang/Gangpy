N = int(input())  
answer = 1  

def factorial(n):
    if n == 0:  
        return 1  
    return n * factorial(n - 1)

print(factorial(N))  