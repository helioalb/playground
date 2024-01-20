class Node:
  def __init__(self, key, left = None, right = None):
    self.key = key
    self.left = left
    self.right = right

three = Node(3);
five = Node(5);
four = Node(4, three, five);

eight = Node(8);
seven = Node(7, None, eight);

six_root = Node(6, four, seven);


def pre_order(node: Node) -> None:
  if node is None:
    return

  print(node.key)
  pre_order(node.left)
  pre_order(node.right)


pre_order(six_root)