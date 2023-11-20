import random

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    elif key > root.key:
        root.right = insert(root.right, key)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.key)
        in_order_traversal(root.right, result)

def dsw_balance(root):
    nodes = []
    in_order_traversal(root, nodes)

    def create_right_skewed_tree(nodes):
        skewed_root = TreeNode(None)
        current = skewed_root
        for node in nodes:
            current.right = TreeNode(node)
            current = current.right
        return skewed_root.right

    def create_balanced_tree(skewed_root, n):
        balanced_root = TreeNode(None)
        current = balanced_root
        m = n + 1 - 2 ** (n.bit_length() - 1)
        q = skewed_root

        for _ in range(m):
            current.right = TreeNode(q.key)
            current = current.right
            q = q.right

        while m > 1:
            m //= 2
            current = balanced_root
            q = current.right

            for _ in range(m):
                current.right = TreeNode(q.key)
                current = current.right
                q = q.right

            current.right = q

        return balanced_root.right

    skewed_tree_root = create_right_skewed_tree(nodes)
    balanced_tree_root = create_balanced_tree(skewed_tree_root, len(nodes))

    return balanced_tree_root

# Criar árvore inicial
initial_tree_root = None
for _ in range(100):
    num = random.randint(0, 100)
    initial_tree_root = insert(initial_tree_root, num)

# Adicionar 20 números à árvore
for _ in range(20):
    num = random.randint(0, 100)
    initial_tree_root = insert(initial_tree_root, num)

# Imprimir árvore inicial
print("Árvore inicial:")
initial_tree_values = []
in_order_traversal(initial_tree_root, initial_tree_values)
print(initial_tree_values)

# Balancear a árvore usando o algoritmo DSW
balanced_tree_root = dsw_balance(initial_tree_root)

# Imprimir árvore balanceada
print("\nÁrvore balanceada:")
balanced_tree_values = []
in_order_traversal(balanced_tree_root, balanced_tree_values)
print(balanced_tree_values)
