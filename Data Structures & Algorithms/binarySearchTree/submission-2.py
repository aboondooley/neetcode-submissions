from typing import Self, Optional, List

class TreeNode:
    def __init__(self, key: int, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right


class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        def insert_recursive(node, key, val):
            if not node:
                return TreeNode(key, val)
            if key == node.key:
                node.val = val
            elif key < node.key:
                node.left = insert_recursive(node.left, key, val)
            else:
                node.right = insert_recursive(node.right, key, val)
            return node

        self.root = insert_recursive(self.root, key, val)


    def get(self, key: int) -> int:
        node = self.root
        while node:
            if key == node.key:
                return node.val
            if key > node.key:
                node = node.right
            else:
                node = node.left
        return -1


    def getMin(self) -> int:
        if not self.root:
            return -1
        node = self.root
        while node.left:
            node = node.left
        return node.val


    def getMax(self) -> int:
        if not self.root:
            return -1
        node = self.root
        while node.right:
            node = node.right
        return node.val


    def remove(self, key: int) -> None:
        
        def minNode(root):
            curr = root
            while curr and curr.left:
                curr = curr.left
            return curr

        def remove_recursive(root, key):
            if not root:
                return None
            if key > root.key:
                root.right = remove_recursive(root.right, key)
            elif key < root.key:
                root.left = remove_recursive(root.left, key)
            else:
                if not root.left:
                    return root.right
                if not root.right:
                    return root.left
                min = minNode(root.right)
                root.key = min.key
                root.val = min.val
                root.right = remove_recursive(root.right, min.key)
            return root

        self.root = remove_recursive(self.root, key)



    def getInorderKeys(self) -> List[int]:
        return inOrder(self.root)

def inOrder(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []
    return inOrder(root.left) + [root.key] + inOrder(root.right)
