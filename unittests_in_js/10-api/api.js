const express = require('express');
const app = express();

app.use(express.json());

app.get('/', (req, result) => {
  result.send('Welcome to the payment system');
});

app.get('/cart/:id(\\d+)', (req, result) => {
    const { id } = req.params;
    result.send(`Payment methods for cart ${id}`);
  });
  
app.get('/available_payments', (req, result) => {
  const availablePayments = {
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  };
  result.json(availablePayments);
});

app.post('/login', (req, result) => {
  const { userName } = req.body;
  result.send(`Welcome ${userName}`);
});


const port = 7865;
app.listen(port, () => {
  console.log(`API available on localhost port ${port}`);
});

module.exports = app;
