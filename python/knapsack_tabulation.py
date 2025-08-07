from typing import List

class knapsack_tabulation:
    def __init__(self, values: List[int], weights: List[int]):
        self.values = values
        self.weights = weights
        self.count = 0
        self.table = []
        self.count += 1 
        print('{}: computing K({}, {})'.format(self.count, 0, 0))
        self.table.append([0])

    def knapsack(self, n: int, capacity: int) -> int:
        for w in range(len(self.table[0]),capacity+1):
            self.count += 1 
            print('{}: computing K({}, {})'.format(self.count, 0, w))
            self.table[0].append(0)
        for i in range(1,n+1):
            if i < len(self.table):
                start = len(self.table[i])
            else:
                self.count += 1 
                print('{}: computing K({}, {})'.format(self.count, i, 0))
                self.table.append([0])
                start = 1
            for w in range(start,capacity+1):
                self.count += 1 
                print('{}: computing K({}, {})'.format(self.count, i, w))
                if self.weights[i-1] > w:
                    self.table[i].append(self.table[i-1][w])
                else:
                    exclude_item = self.table[i-1][w]
                    include_item = self.values[i-1] + self.table[i-1][w - self.weights[i-1]]
                    self.table[i].append(max(exclude_item, include_item))
        return self.table[n][capacity]
    
def main() -> None:
    alg = knapsack_tabulation([300, 200, 400, 500], [2, 1, 5, 3])
    print(alg.knapsack(4, 10))

if __name__ == '__main__':
    main()