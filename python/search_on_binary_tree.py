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
  print_node(node)
  if node is None or node.key == key:
    return node;

  if key < node.key:
    print(' -> goes to left\n')
    return search(node.left, key)

  print(' -> goes to right')
  return search(node.right, key)

def print_node(node):
  if node is None:
    print('Current node is null')
  else:
   print('Current node: ', node.key)


search(six_root, key=3)

print('-------\n')

search(six_root, key=5)

print('-------\n')

search(six_root, key=18)
