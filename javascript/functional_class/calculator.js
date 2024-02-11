function calculator() {
  return {
    sum: function(a, b) {
      return a + b;
    },
    multiply: function(a, b) {
      return a * b;
    }
  }
}

const calc = calculator();

sum = calc.sum(1, 2);
multiply = calc.multiply(2, 3);

console.log('Sum: ', sum, ', Multiply: ', multiply);
