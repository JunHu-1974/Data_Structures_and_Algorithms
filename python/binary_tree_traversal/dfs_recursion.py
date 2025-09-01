from typing import Optional

from binary_tree import TreeNode, listToTreeNode

def visit(node: Optional[TreeNode]) -> Optional[int]:
    if node:
        return node.val
    else:
        return None
    
def depth_first_search(root: Optional[TreeNode], order: str) -> list:
    output = []
    if not root:
        return [root]
    left_tree = depth_first_search(root.left, order)
    right_tree = depth_first_search(root.right, order)
    if order == 'pre':
        output = [visit(root)] + left_tree + right_tree
    elif order == 'in':
        output = left_tree + [visit(root)] + right_tree
    else:
        output = left_tree + right_tree + [visit(root)]
    return output

def main() -> None:
    tree = listToTreeNode()
    output= depth_first_search(tree, 'pre')
    print(output)
    output= depth_first_search(tree, 'in')
    print(output)
    output= depth_first_search(tree, 'post')
    print(output)
    tree = listToTreeNode([6, 2, 7, 1, 4, None, 9, None, None, 3, 5, 8])
    print(tree)
    output= depth_first_search(tree, 'pre')
    print(output)
    output= depth_first_search(tree, 'in')
    print(output)
    output= depth_first_search(tree, 'post')
    print(output)

if __name__ == '__main__':
    main()