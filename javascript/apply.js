function printSum(a, b) {
  console.log(this + a + b);
}

printSum.apply(5, [2, 3]);
