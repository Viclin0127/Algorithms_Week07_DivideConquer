from TreeNode import Node

def Height(T):
    if T is None:
        return -1
    else:
        return max(Height(T.left), Height(T.right))+1

def test():
    T = Node(17)
    T.left = Node(33)
    T.left.left = Node(19)
    T.left.right = Node(16)
    T.left.right.left = Node(38)
    T.left.right.right = Node(31)
    T.right = Node(48)
    T.right.left = Node(11)
    T.right.right = Node(14)
    print(Height(T))


if __name__ == "__main__":
    test()