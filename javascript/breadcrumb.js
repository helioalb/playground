const product = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];

function buildCatetoryPath(product) {
  return product.map((category, index) => {
    const path = product.slice(0, index + 1).join('/');
    return {
      category,
      path
    }
  });
}

console.log(buildCatetoryPath(product));

