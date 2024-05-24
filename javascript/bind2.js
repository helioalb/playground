function explain(first, second) {
  console.log(this, first, second)
}

const bound = explain.bind(1, 2);
bound(3);
