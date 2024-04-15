const express = require('express');
const { default: connectDB } = require('./db');
const app = express();
const port = 3001;
require('./db');

app.get('/', (req, res) => {
  res.send('Hello World!');
});


app.listen(port, () => {
  console.log(`Example app listening at http://localhost:${port}`);
});