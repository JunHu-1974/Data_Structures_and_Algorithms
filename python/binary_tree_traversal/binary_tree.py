from typing import Optional

class TreeNode(object):
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return 'val: {}, left: ({}), right: ({})'.format(self.val, self.left, self.right)

def listToTreeNode(values: list = []) -> TreeNode:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    parent = 0
    curr = 1
    while curr < len(values):
        node = queue[parent]
        parent += 1
        value = values[curr]
        curr += 1
        if value:
            node.left = TreeNode(value)
            queue.append(node.left)

        if curr < len(values):
            value = values[curr]
            curr += 1
            if value:
                node.right = TreeNode(value)
                queue.append(node.right)
    return root

def main() -> None:
    tree = listToTreeNode()
    print(tree)
    tree = listToTreeNode([6, 2, 7, 1, 4, None, 9, None, None, 3, 5, 8])
    print(tree)

if __name__ == '__main__':
    main()