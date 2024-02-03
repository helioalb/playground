<?php
class Node{
    public int $key;
    public ?Node $left;
    public ?Node $right;

    public function __construct(int $key, ?Node $left = null, ?Node $right = null) {
        $this->key = $key;
        $this->left = $left;
        $this->right = $right;
    }
}

$three = new Node(3);
$five = new Node(5);
$four = new Node(4, $three, $five);

$eight = new Node(8);
$seven = new Node(7, null, $eight);

$six_root = new Node(6, $four, $seven);

function inOrder(?Node $node) {
    if (is_null($node))
        return;

    inOrder($node->left);
    echo $node->key . ' ';
    inOrder($node->right);
}

inOrder($six_root);