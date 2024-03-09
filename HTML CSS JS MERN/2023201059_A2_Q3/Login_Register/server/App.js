const express = require('express');
const app = express();
const port = 3001;
const questionsRouter = require('./questions'); 

app.use(express.json());

app.use('/questions', questionsRouter);

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});
