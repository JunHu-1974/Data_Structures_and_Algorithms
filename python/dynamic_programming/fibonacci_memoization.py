class fibonacci_memoization:
    def __init__(self):
        self.count = 0
        self.memory = {}

    def fibonacci(self, n: int) -> int:
        if not n in self.memory:
            self.count += 1
            print('{}: computing F({})'.format(self.count, n))
            if n <= 1:
                self.memory[n] = n
            else:
                self.memory[n] = self.fibonacci(n-1) + self.fibonacci(n-2)
        return self.memory[n]
    
def main() -> None:
    alg = fibonacci_memoization()
    for i in range(7):
        print(alg.fibonacci(i))

if __name__ == '__main__':
    main()