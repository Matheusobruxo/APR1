
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2) 

def main():
    for i in range(1,7000):
        print(fibonacci(i))