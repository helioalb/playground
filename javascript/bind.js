function sumWithUndefinedThis(a, b) {
  return this + a + b;
}

const sumWithDefinedThis = sumWithUndefinedThis.bind(5);

console.log(sumWithDefinedThis(2, 3));
