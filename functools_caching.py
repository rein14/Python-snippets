from functools import cache, lru_cache
from urllib.parse import MAX_CACHE_SIZE

@lru_cache(maxsize=5)
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-1)

def main():
    for i in range(200):
        print(i, fib(i))
    print("done")

if __name__ == "__main__":
    main()