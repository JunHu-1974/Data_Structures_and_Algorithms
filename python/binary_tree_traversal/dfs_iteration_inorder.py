from typing import Optional

from binary_tree import TreeNode, listToTreeNode

def visit(node: Optional[TreeNode]) -> Optional[int]:
    if node:
        return node.val
    else:
        return None
    
def depth_first_search(root: Optional[TreeNode]) -> list:
    output = []
    if not root:
        return [root]
    stack = []
    node = root
    while stack or node:
        if node:
            stack.append(node)
            node = node.left
        else:
            output.append(visit(node))
            node = stack.pop()
            output.append(visit(node))
            node = node.right
    return output

def main() -> None:
    tree = listToTreeNode()
    output= depth_first_search(tree)
    print(output)
    tree = listToTreeNode([6, 2, 7, 1, 4, None, 9, None, None, 3, 5, 8])
    print(tree)
    output= depth_first_search(tree)
    print(output)

if __name__ == '__main__':
    main()