class Node {
  constructor(key, left, right) {
    this.key = key;
    this.left = left;
    this.right = right;
  }
}

three = new Node(3);
five = new Node(5);
four = new Node(4, three, five);

eight = new Node(8);
seven = new Node(7, null, eight);

six_root = new Node(6, four, seven);

function postOrder(node) {
  if (node == null)
    return;

  postOrder(node.left);
  postOrder(node.right);
  console.log(node.key);
}

postOrder(six_root);