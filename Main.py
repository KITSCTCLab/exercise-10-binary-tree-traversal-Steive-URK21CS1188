class BinaryTreeNode:
     def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
   
    
def insert(root, new_value) -> BinaryTreeNode:
    """If binary search tree is empty, make a new node, declare it as root and return the root.
        If tree is not empty and if new_value is less than value of data in root, add it to left subtree and proceed recursively.
        If tree is not empty and if new_value is >= value of data in root, add it to right subtree and proceed recursively.
        Finally, return the root.
        """
    # Write your code here
    if self.data:
        if data < self.data:
            if self.data is None:
                self.left_child = BinaryTreeNode(data)
            else:
                self.left_child.insert(root, data)
        elif data > self.data:
            if self.data is None:
                self.right_child = BinaryTreeNode(data)
            else:
                self.right_child.insert(root, data)
    else:
        self.data=data
          
def inorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res = self.inorder(root.left_child)
        res.append(root.data)
        res = res + self.inorder(root.right_child)
    return res

def preorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res.append(root.data)
        res = res + self.preorder(root.left_child)
        res = res + self.preorder(root.right_child)
    return res


def postorder(root) -> None:
    # Write your code here
    res = []
    if root is not None:
        res = self.postorder(root.left_child)
        res = res + self.postorder(root.right_child)
        res.append(root.data)
    return res


# Do not change the following code
input_data = input()
flag = True
root = None
for item in input_data.split(', '):
    if flag is True:
        root = insert(None, int(item))
        flag = False
    else:
        insert(root, int(item))
inorder(root)
print()
preorder(root)
print()
postorder(root)
