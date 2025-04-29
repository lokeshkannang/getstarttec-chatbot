const { NlpManager } = require('node-nlp');

// Create a new NLP manager for English
const manager = new NlpManager({ languages: ['en'], forceNER: true });

// Add training data (questions and intents)
manager.addDocument('en', 'What services do you provide?', 'services');
manager.addDocument('en', 'Tell me about your services', 'services');
manager.addDocument('en', 'What do you offer?', 'services');
manager.addDocument('en', 'What kind of solutions do you provide?', 'services');

manager.addDocument('en', 'How much does web development cost?', 'pricing');
manager.addDocument('en', 'What is your pricing?', 'pricing');
manager.addDocument('en', 'How much do you charge?', 'pricing');
manager.addDocument('en', 'Tell me about your rates', 'pricing');

manager.addDocument('en', 'Do you offer consultations?', 'consultation');
manager.addDocument('en', 'Can I talk to an expert?', 'consultation');
manager.addDocument('en', 'Do you provide project discussions?', 'consultation');
manager.addDocument('en', 'Is consultation free?', 'consultation');

manager.addDocument('en', 'What is your refund policy?', 'refund');
manager.addDocument('en', 'Can I get a refund?', 'refund');
manager.addDocument('en', 'Do you give money back?', 'refund');
manager.addDocument('en', 'How do refunds work?', 'refund');

// Add answers (responses for each intent)
manager.addAnswer('en', 'services', 'We offer Web Development, App Development, and Cloud Consulting.');
manager.addAnswer('en', 'pricing', 'Our pricing starts at ₹20,000 depending on your project scope.');
manager.addAnswer('en', 'consultation', 'Yes, we provide free consultations. Book an appointment on our website.');
manager.addAnswer('en', 'refund', 'We offer a 30-day refund policy if you\'re not satisfied with our services.');

// Function to train and save the NLP model
async function trainNLP() {
  await manager.train();
  manager.save();
  console.log("🤖 NLP Model Trained!");
}

// Function to process user input and return a chatbot response
async function getResponse(userInput) {
  const response = await manager.process('en', userInput);
  return response.answer || "Sorry, I didn't understand that. Can you rephrase?";
}

// Export the functions
module.exports = {
  trainNLP,
  getResponse,
};
