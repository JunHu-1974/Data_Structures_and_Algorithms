class fibonacci_recursion:
    def __init__(self):
        self.count = 0

    def fibonacci(self, n: int) -> int:
        self.count += 1
        print('{}: computing F({})'.format(self.count, n))
        if n <= 1:
            return n 
        else:
            return self.fibonacci(n-1) + self.fibonacci(n-2)
    
def main() -> None:
    alg = fibonacci_recursion()
    for i in range(7):
        print(alg.fibonacci(i))

if __name__ == '__main__':
    main()