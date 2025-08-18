class fibonacci_memoization:
    def __init__(self):
        self.count = 0
        self.memory = {}

    def fibonacci(self, n: int) -> int:
        if n in self.memory:
            return self.memory[n]
        self.count += 1
        print('{}: computing F({})'.format(self.count, n))
        if n <= 1:
            self.memory[n] = n
        else:
            self.memory[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.memory[n]
    
def main() -> None:
    alg = fibonacci_memoization()
    print(alg.fibonacci(6))

if __name__ == '__main__':
    main()