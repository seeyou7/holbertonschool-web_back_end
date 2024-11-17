const express = require('express');
const app = express();

app.get('/', (req, result) => {
  result.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, result) => {
    const { id } = req.params;
    result.send(`Payment methods for cart ${id}`);
  });  

const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;