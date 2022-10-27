from time import perf_counter
from functools import wraps

class Solution1:
    def fibIterative(self, n):
        stack = []
        stack.append(n)
        sum = 0
        while(len(stack) > 0):
            n = stack.pop()
            if n == 0:
                sum += 0
            elif n == 1:
                sum +=1
            else:
                stack.append(n-1)
                stack.append(n-2)
            return sum

class Solution2:
    def fibMemoized(self, n, cache = {}):
        if n not in cache.keys():
            cache[n] = self._fibMemoizedHelper(n, cache)
        return cache[n]

    def _fibMemoizedHelper(self, n, cache):
        if n < 2:
            return n
        else:
            return self.fibMemoized(n-1, cache) + self.fibMemoized(n-2, cache)

class Solution3:
    def memoize(func):
        cache = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            key = str(*args) + str(**kwargs)

            if key not in cache:
                cache[key] = func(*args, **kwargs)

            return cache[key]

        return wrapper

    @memoize
    def fibonacci(n) -> int:
        if n < 2:
            return n
        return Solution3.fibonacci(n - 1) + Solution3.fibonacci(n - 2)

if __name__ == '__main__':
    start = perf_counter()
    number = 10
    a = Solution1.fibIterative(number)
    b = Solution2.fibMemoized(number)
    c = Solution3.fibonacci(number)
    end = perf_counter()

    print(c)
    print("It took {} seconds to perform the task".format(end-start))
