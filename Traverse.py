from TreeNode import Node
from queue import Queue

def PreorderTraverse(T):
    if T is not None:
        print(T.val)
        PreorderTraverse(T.left)
        PreorderTraverse(T.right)

def InorderTraverse(T):
    if T is not None:
        InorderTraverse(T.left)
        print(T.val)
        InorderTraverse(T.right)

def PostorderTraverse(T):
    if T is not None:
        PostorderTraverse(T.left)
        PostorderTraverse(T.right)
        print(T.val)

def LevelorderTraverse(T):
    Q = Queue()
    Q.put(T)
    while not Q.empty():
        x = Q.get()
        print(x.val)
        if x.left is not None:
            Q.put(x.left)
        if x.right is not None:
            Q.put(x.right)

def test():
    T = Node(17)
    T.left = Node(13)
    T.right = Node(26)
    T.left.left = Node(14)
    T.left.right = Node(5)
    print("Preorder : ")
    PreorderTraverse(T)
    print("-------")
    print("Inorder : ")
    InorderTraverse(T)
    print("-------")
    print("Postorder : ")
    PostorderTraverse(T)
    print("-------")
    print("Levelorder : ")
    LevelorderTraverse(T)

if __name__ == "__main__":
    test()