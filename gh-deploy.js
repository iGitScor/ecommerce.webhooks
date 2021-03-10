const a = {};
a.test = true;
  a.test = 1;
Object.freeze(a);
a.value = 'abc-1432'

console.log(a + "a.test");

