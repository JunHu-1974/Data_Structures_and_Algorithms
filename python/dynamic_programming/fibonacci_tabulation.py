class fibonacci_tabulation:
    def __init__(self):
        self.count = 0
        self.table = []
        self.count += 1
        print('{}: computing F({})'.format(self.count, 0))
        self.table.append(0)
        self.count += 1
        print('{}: computing F({})'.format(self.count, 1))
        self.table.append(1)

    def fibonacci(self, n: int) -> int:
        if n >= len(self.table):
            for i in range(len(self.table), n+1):
                print('{}: computing F({})'.format(self.count, i))
                self.count += 1
                self.table.append(self.table[i-1] + self.table[i-2])
        return self.table[n]
    
def main() -> None:
    alg = fibonacci_tabulation()
    for i in range(7):
        print(alg.fibonacci(i))

if __name__ == '__main__':
    main()