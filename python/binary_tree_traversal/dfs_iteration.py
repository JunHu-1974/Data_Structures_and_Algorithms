from typing import Optional

from binary_tree import TreeNode, listToTreeNode

def visit(node: TreeNode) -> Optional[int]:
    if node:
        return node.val
    else:
        return None
    
def depth_first_search(root: TreeNode, order: str) -> list:
    output = []
    if not root:
        return output
    if order == 'pre':
        stack = [[root.right, root.left, root]]
    elif order == 'in':
        stack = [[root.right, root, root.left]]
    else:
        stack = [[root, root.right, root.left]]
    while stack:
        if stack[-1]:
            node = stack[-1].pop()
            if order == 'pre' and len(stack[-1]) == 2:
                output.append(visit(node))
            elif order == 'in' and len(stack[-1]) == 1:
                output.append(visit(node))
            elif order == 'post' and len(stack[-1]) == 0:
                output.append(visit(node))
            elif order == 'pre' and node:
                stack.append([node.right, node.left, node])
            elif order == 'in' and node:
                stack.append([node.right, node, node.left])
            elif order == 'post' and node:
                stack.append([node, node.right, node.left])
            else:
                output.append(visit(node))
        else:
            stack.pop()
    return output

def main() -> None:
    output= depth_first_search(None, 'pre')
    print(output)
    output= depth_first_search(None, 'in')
    print(output)
    output= depth_first_search(None, 'post')
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