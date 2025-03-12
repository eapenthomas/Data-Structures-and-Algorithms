from functools import cache
import time

def fib(n):
    if n < 0:
        return 0
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

@cache
def finb(n):
    if n < 0:
        return 0
    if n ==0:
        return 0
    if n ==1:
        return 1
    else:
        return finb(n-1)+finb(n-2)
start = time.time()
print(finb(50))  # Time-consuming without cache
end = time.time()
print(f" Cache: {end - start} seconds")
start = time.time()
print(fib(32))
end = time.time()

print(f"Without Cache: {end - start} seconds")
