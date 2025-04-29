const askGemini = require('./gemini');

async function chatBotResponse(userInput) {
  const response = await askGemini(userInput);
  console.log("Bot says:", response);
}

chatBotResponse("what's your name");
