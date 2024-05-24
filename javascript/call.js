const person = {
  name: 'John',
  lastname: 'Doe',
};

function print() {
  console.log(this.name, ' ', this.lastname);
}

print.call(person);
