from typing import Optional, List

class TreeNode:
    def __init__(self, key: int, val: int, left: Optional['TreeNode'] = None, right:  Optional['TreeNode'] = None):
        self.key = key
        self.val = val
        self.left = left
        self. right = right

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:

        def insert_recursive(root, key, val) -> Optional[TreeNode]:
            if not root:
                root = TreeNode(key, val)
            elif key < root.key:
                root.left = insert_recursive(root.left, key, val)
            elif key > root.key:
                root.right = insert_recursive(root.right, key, val)
            else:
                root = TreeNode(key, val, root.left, root.right)
            return root

        self.root = insert_recursive(self.root, key, val)


    def get(self, key: int) -> int:
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1


    def getMin(self) -> int:
        if not self.root: return -1
        curr = self.root
        while curr and curr.left:
            curr = curr.left
        return curr.val


    def getMax(self) -> int:
        if not self.root: return -1
        curr = self.root
        while curr and curr.right:
            curr = curr.right
        return curr.val

    def remove(self, key: int) -> None:
        def getMinNode(root):
            while root and root.left:
                root = root.left
            return root

        def remove_recursive(root, key):
            if not root: return None
            if key < root.key:
                root.left = remove_recursive(root.left, key)
            elif key > root.key:
                root.right = remove_recursive(root.right, key)
            else:
                if not root.left: return root.right
                if not root.right: return root.left
                minNode = getMinNode(root.right)
                root.key, root.val = minNode.key, minNode.val
                root.right = remove_recursive(root.right, minNode.key)
            return root

        self.root = remove_recursive(self.root, key)


    def getInorderKeys(self) -> List[int]:

        def inorder(root) -> List[int]:
            if not root: return []
            return inorder(root.left) + [root.key] + inorder(root.right)

        return inorder(self.root)
