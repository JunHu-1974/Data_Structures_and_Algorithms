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
    last = None
    node = root
    while stack or node:
        if node:
            #output.append(visit(node)) #pre-order
            stack.append(node)
            node = node.left
            if not node:
                output.append(visit(node))
        else:
            peek_node = stack[-1]
            if peek_node.right and not peek_node.right is last:
                #output.append(visit(peek_node)) #in-order
                node = peek_node.right
            else:
                if not peek_node.right:
                    #output.append(visit(peek_node)) #in-order
                    output.append(visit(peek_node.right))
                output.append(visit(peek_node)) #post-order
                last = stack.pop()
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