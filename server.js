const express = require('express');
const bodyParser = require('body-parser');
const { trainNLP, getResponse } = require('./nlp/manager');

const app = express();
const PORT = 5000;

app.use(bodyParser.json());

// Train NLP when the server starts
trainNLP();

// Chat endpoint
app.post('/api/chat', async (req, res) => {
  const { message } = req.body;
  const response = await getResponse(message);
  res.json({ reply: response });
});

app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});
