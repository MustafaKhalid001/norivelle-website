const { OpenAI } = require('openai');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    if (!process.env.OPENAI_API_KEY) {
      return res.status(500).json({ error: 'OPENAI_API_KEY is missing in Vercel Environment Variables.' });
    }

    const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });

    const { messages } = req.body;

    if (!messages || !Array.isArray(messages)) {
      return res.status(400).json({ error: 'Messages array is required.' });
    }

    // Define the system prompt so the AI acts correctly for Norivelle
    const systemPrompt = {
      role: 'system',
      content: `You are a polite, helpful, and professional AI Assistant for Norivelle Solution, a premium IT and digital agency.
Your primary goal is to help visitors understand the services offered (Wordpress, Shopify, SEO, Content Writing, Video Editing, Social Media) and encourage them to use the Contact Us page for business inquiries or proposals.
Keep your answers relatively concise, friendly, and formatted nicely. Do not invent fake prices or fake phone numbers. Direct users to the contact page for specific pricing or advanced technical support.`
    };

    // Combine system prompt with user messages
    const apiMessages = [systemPrompt, ...messages];

    const completion = await openai.chat.completions.create({
      model: "gpt-3.5-turbo",
      messages: apiMessages,
      max_tokens: 300,
      temperature: 0.7,
    });

    return res.status(200).json({ reply: completion.choices[0].message.content });

  } catch (error) {
    console.error('Chat API Error:', error);
    
    // Handle OpenAI specific errors gracefully
    if (error.response) {
      return res.status(error.response.status).json({ error: error.response.data.error.message });
    }

    return res.status(500).json({ error: error.message || 'Internal Server Error' });
  }
}
