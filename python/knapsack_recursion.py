from typing import List

class knapsack_recursion:
    def __init__(self, values: List[int], weights: List[int]):
        self.values = values
        self.weights = weights
        self.count = 0

    def knapsack(self, n: int, capacity: int) -> int:
        self.count += 1
        print('{}: computing K({}, {})'.format(self.count, n, capacity))
        if n == 0 or capacity == 0:
            return 0
        elif self.weights[n-1] > capacity:
            return self.knapsack(n-1, capacity)
        else:
            exclude_item = self.knapsack(n-1, capacity)
            include_item = self.values[n-1] + self.knapsack(n-1, capacity - self.weights[n-1])
            return max(exclude_item, include_item)
    
def main() -> None:
    alg = knapsack_recursion([300, 200, 400, 500], [2, 1, 5, 3])
    print(alg.knapsack(4, 10))

if __name__ == '__main__':
    main()