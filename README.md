# Data Structures and Algorithms: Python

This is a personal hobby project that implements some commonly used data structures and algorithms in Python.

## Hash table

A hash table is a data structure that implements an associative array. A hash function is used to compute an index, also called a hash code, into an array of buckets or slots, from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored. In a well-dimensioned hash table, the average time complexity for each lookup, addition and deletion is independent of the number of elements stored in the table. Hashing is a good example of space-time tradeoff.

### Hash set
Hash tables can be used in the implementation of set data structure, which can store unique values without any particular order. Set is typically used in testing the membership of a value in the collection, rather than element retrieval.

### Hash map
A hash map is a form of hash table that usually stores a large collection of (key, value) pairs, such that each possible key appears at most once in the collection. Using a hash map we can map keys to values. The association between a key and a value is often known as a "mapping". The same word may also be used to refer to the process of creating a new association. That's why a mapping implemented by a hash table is called a hash map.

## Binary tree traversal

Tree traversal is a special form of graph traversal and refers to the process of visiting each node in a tree data structure, exactly once. Unlike linear data structures such as one-dimensional arrays and linked lists, trees may be traversed in multiple ways. From a given node, there is more than one possible next node. Therefore traversals are classified by the order in which the nodes are visited.

### Depth-first search (DFS)
In depth-first search, we always attempt to visit the node farthest from the root node that we can, but with the caveat that it must be a child of a node we have already visited. Unlike a depth-first search on graphs, there is no need to remember all the nodes we have visited, because a tree cannot contain cycles. There are three common ways to traverse a tree in depth-first search.

1. In **pre-order**, we always visit the current node; next, we recursively traverse the current node's left subtree, and then we recursively traverse the current node's right subtree. The **pre-orde**r traversal is a topologically sorted traversal, because a parent node is processed before any of its child nodes is done.
2. In **in-order**, we always recursively traverse the current node's left subtree; next, we visit the current node, and lastly, we recursively traverse the current node's right subtree.
3. In **post-order**, we always recursively traverse the current node's left subtree; next, we recursively traverse the current node's right subtree and then visit the current node.

### Breadth-first search (BFS)
Contrasting with depth-first search is breadth-first search, which always attempts to visit the node closest to the root that it has not already visited. Breadth-first search is also called level-order traversal.

## Shortest path problem

In graph theory, the shortest path problem is the problem of finding a path between two vertices (or nodes) in a graph such that the sum of the weights of its constituent edges is minimized. The problem is also sometimes called the single-pair shortest path problem, to distinguish it from the following variations:
* The single-source shortest path problem, in which we have to find shortest paths from a source vertex v to all other vertices in the graph.
* The single-destination shortest path problem, in which we have to find shortest paths from all vertices in the directed graph to a single destination vertex v. This can be reduced to the single-source shortest path problem by reversing the arcs in the directed graph.
* The all-pairs shortest path problem, in which we have to find shortest paths between every pair of vertices v, v' in the graph.
These generalizations have significantly more efficient algorithms than the simplistic approach of running a single-pair shortest path algorithm on all relevant pairs of vertices.

### Dijkstra's algorithm
solves the single-source shortest path problem with only non-negative edge weights.

### Bellman–Ford algorithm
solves the single-source problem if edge weights may be negative.

### A* search algorithm
solves for single-pair shortest path using heuristics to try to speed up the search.

## Sorting algorithms

A sorting algorithm is an algorithm that puts elements of a list into an order. The most frequently used orders are numerical order and lexicographical order, and either ascending or descending. Efficient sorting is important for optimizing the efficiency of other algorithms (such as search and merge algorithms) that require input data to be in sorted lists. Sorting is also often useful for canonicalizing data and for producing human-readable output.

Formally, the output of any sorting algorithm must satisfy two conditions:

1. The output is in monotonic order (each element is no smaller/larger than the previous element, according to the required order).
2. The output is a permutation (a reordering, yet retaining all of the original elements) of the input.

### Selection Sort
Selection sort divides the input list into two parts: a sorted sublist of items which is built up from left to right at the front (left) of the list and a sublist of the remaining unsorted items that occupy the rest of the list. Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, and moving (or swapping) it to the sorted sublist.

### Insertion Sort
Insertion sort is a simple sorting algorithm that builds the final sorted array (or list) one item at a time by comparisons. The partial sorted list initially contains only the first element in the list. At each iteration, the algorithm removes one element from the the "not yet checked for order" input data, finds the correct location within the sorted list, and inserts it there. It repeats until no input elements remain.

### Quicksort
Quicksort is a divide-and-conquer algorithm. It works by selecting a "pivot" element from the array and partitioning the other elements into two sub-arrays, according to whether they are less than or greater than the pivot. For this reason, it is sometimes called partition-exchange sort. The sub-arrays are then sorted recursively. This can be done in-place, requiring small additional amounts of memory to perform the sorting.

### Mergesort
Mergesort is a divide-and-conquer algorithm. Conceptually, a merge sort works as follows:
1. Divide the unsorted list into n sub-lists, each containing one element (a list of one element is considered sorted).
2. Repeatedly merge sublists to produce new sorted sublists until there is only one sublist remaining. This will be the sorted list.

## Dynamic programming

There are two key attributes that a problem must have in order for dynamic programming to be applicable: _optimal substructure_ and _overlapping sub-problems_.

_Optimal substructure_ means that the solution to a given optimization problem can be obtained by the combination of optimal solutions to its sub-problems. Such optimal substructures are usually described by means of recursion. For example, the shortest path in a given graph can be split into sub-paths that, in turn, are the shortest paths between the corresponding vertices. Hence, one can easily formulate the solution for finding shortest paths in a recursive manner.

_Overlapping sub-problems_ means that the space of sub-problems must be small, that is, any recursive algorithm solving the problem should solve the same sub-problems over and over, rather than generating new sub-problems. Dynamic programming takes account of this fact and solves each sub-problem only once.

### Memoization
Memoization is a top-down approach, which is the direct fall-out of the recursive formulation of any problem. If the solution to any problem can be formulated recursively using the solution to its sub-problems, and if its sub-problems are overlapping, then one can easily memoize or store the solutions to the sub-problems in a table (often an array or hashtable in practice). Whenever we attempt to solve a new sub-problem, we first check the table to see if it is already solved. If a solution has been recorded, we can use it directly, otherwise we solve the sub-problem and add its solution to the table.

### Tabulation
Tabulation is a bottom-up approach. Once we formulate the solution to a problem recursively as in terms of its sub-problems, we can try reformulating the problem in a bottom-up fashion: try solving the most basic sub-problems first and use their solutions to build-on and arrive at solutions to the next sub-problems. This is also usually done in a tabular form by iteratively generating solutions to bigger and bigger sub-problems.

> **Note:** Work in progress. 
