const axios = require('axios');
require('dotenv').config();

const GEMINI_API_URL = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent';

async function askGemini(userInput) {
  try {
    const response = await axios.post(
      `${GEMINI_API_URL}?key=${process.env.GEMINI_API_KEY}`,
      {
        contents: [
          {
            parts: [
              { text: userInput }
            ]
          }
        ]
      }
    );

    const answer = response.data?.candidates?.[0]?.content?.parts?.[0]?.text;
    return answer || "Hmm, I couldn't understand that.";
  } catch (error) {
    console.error("Gemini Error:", error.response?.data || error.message);
    return "There was a problem connecting to Gemini.";
  }
}

module.exports = askGemini;
