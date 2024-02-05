class Node:
  def __init__(self, key, left = None, right = None):
    self.key = key
    self.left = left
    self.right = right

  def __repr__(self) -> str:
    return f"key = {self.key}"

three = Node(3)
five = Node(5)
four = Node(4, three, five)

eight = Node(8)
seven = Node(7, None, eight)

six_root = Node(6, four, seven)

def search(node, key):

  while node is not None and node.key != key:
    if key < node.key:
      print_node(node, 'left')
      node = node.left
    else:
      print_node(node, 'right')
      node = node.right

  print_node(node)
  return node

def print_node(node, direction = None):
  if node is None:
    print('Current node is null')
  else:
    print(f"Current node: {node.key}  - {direction}")



search(six_root, key=3)

# print('-------\n')

# print(search(six_root, key=5))

# print('-------\n')

# search(six_root, key=18)
