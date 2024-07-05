const fields = [
  {
    "name": "col1",
    "data_type": "string"
  },
  {
    "name": "col2",
    "data_type": "string"
  },
  {
    "name": "col3",
    "data_type": "string"
  },
  {
    "name": "ins1",
    "data_type": "string"
  },
  {
    "name": "col4",
    "data_type": "string"
  },
  {
    "name": "com espaço",
    "data_type": "string"
  }
];

const data = fields.reduce((acc, field) => {
  return {
    ...acc,
    [field.name]: 'x'
  };
}, {});

console.log(data); // { col1: 'x' }
