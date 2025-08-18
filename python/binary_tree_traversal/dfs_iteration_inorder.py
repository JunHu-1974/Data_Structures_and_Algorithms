from typing import Optional

from binary_tree import TreeNode, listToTreeNode

def visit(node: TreeNode) -> Optional[int]:
    if node:
        return node.val
    else:
        return None
    
def depth_first_search(root: TreeNode) -> list:
    output = []
    if not root:
        return [None]
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
            if not node:
                output.append(visit(node))
        else:
            node = stack.pop()
            output.append(visit(node))
            node = node.right
            if not node:
                output.append(visit(node))
    return output

def main() -> None:
    tree = listToTreeNode([6, 2, 7, 1, 4, None, 9, None, None, 3, 5, 8])
    print(tree)
    output= depth_first_search(tree)
    print(output)

if __name__ == '__main__':
    main()