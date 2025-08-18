from typing import Optional

from binary_tree import TreeNode, listToTreeNode

def visit(node: TreeNode) -> Optional[int]:
    if node:
        return node.val
    else:
        return None
    
def breadth_first_search(root: TreeNode) -> list:
    output = []
    queue = [[root]]
    depth = 0
    while queue[depth]:
        queue.append([])
        for node in queue[depth]:
            output.append(visit(node))
            if node:
                queue[depth+1].append(node.left)
                queue[depth+1].append(node.right)
        depth += 1
    return output

def main() -> None:
    output= breadth_first_search(None)
    print(output)
    tree = listToTreeNode([6, 2, 7, 1, 4, None, 9, None, None, 3, 5, 8])
    print(tree)
    output= breadth_first_search(tree)
    print(output)

if __name__ == '__main__':
    main()