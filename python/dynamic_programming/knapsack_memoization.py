from typing import List

class knapsack_memoization:
    def __init__(self, values: List[int], weights: List[int]):
        self.values = values
        self.weights = weights
        self.count = 0
        self.memory = {}

    def knapsack(self, n: int, capacity: int) -> int:
        if not (n,capacity) in self.memory:
            self.count += 1
            print('{}: computing K({}, {})'.format(self.count, n, capacity))
            if n == 0 or capacity == 0:
                self.memory[(n,capacity)] = 0
            elif self.weights[n-1] > capacity:
                self.memory[(n,capacity)] = self.knapsack(n-1, capacity)
            else:
                exclude_item = self.knapsack(n-1, capacity)
                include_item = self.values[n-1] + self.knapsack(n-1, capacity - self.weights[n-1])
                self.memory[(n,capacity)] = max(exclude_item, include_item)
        return self.memory[(n,capacity)]
    
def main() -> None:
    alg = knapsack_memoization([300, 200, 400, 500], [2, 1, 5, 3])
    for i in range(5,11):
        print(alg.knapsack(4, i))

if __name__ == '__main__':
    main()