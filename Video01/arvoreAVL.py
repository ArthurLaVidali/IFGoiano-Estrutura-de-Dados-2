import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def height(node):
    if not node:
        return 0
    return node.height

def update_height(node):
    if not node:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))
    return node.height

def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

def rotate_left(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    update_height(y)
    update_height(x)

    return x

def rotate_right(x):
    y = x.left
    T2 = y.right

    y.right = x
    x.left = T2

    update_height(x)
    update_height(y)

    return y

def insert(root, key):
    if not root:
        return Node(key)

    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    else:
        return root  
    
    update_height(root)

    balance = balance_factor(root)

    # Left Left Case
    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    # Right Right Case
    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    # Left Right Case
    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    # Right Left Case
    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.key)
        result += inorder_traversal(root.right)
    return result

def build_avl_tree(data):
    root = None
    for key in data:
        root = insert(root, key)
    return root

def print_avl_tree(root):
    result = inorder_traversal(root)
    print(result)

if __name__ == "__main__":
    # Carregar dados do arquivo
    with open("dados100_mil.txt", "r") as file:
        data = [int(num) for num in file.read().split(",")]

    # Construir árvore AVL 
    avl_tree = build_avl_tree(data)


    # Imprimir a árvore AVL em ordem e calcular o tempo
    start_time = time.time()
    print_avl_tree(avl_tree)
    end_time = time.time()

    seconds = (end_time - start_time)

    print(f"Árvore AVL impressa em ordem em {seconds:.3f} segundos" )
