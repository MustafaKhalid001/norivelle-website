const { Pool } = require('pg');
const { Resend } = require('resend');

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    if (!process.env.DATABASE_URL) {
      return res.status(500).json({ error: 'DATABASE_URL is missing in Vercel Environment Variables.' });
    }

    const pool = new Pool({
      connectionString: process.env.DATABASE_URL,
      ssl: { rejectUnauthorized: false }
    });

    const { name, company, email, phone, country, services, subject, message } = req.body;

    if (!name || !email || !message) {
      return res.status(400).json({ error: 'Name, email, and message are required.' });
    }

    const query = `
      INSERT INTO contacts (name, company, email, phone, country, services, subject, message)
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
      RETURNING id;
    `;
    
    const servicesStr = Array.isArray(services) ? services.join(', ') : (services || '');

    const values = [
      name, company || '', email, phone || '', country || '', servicesStr, subject || '', message
    ];

    const result = await pool.query(query, values);

    // Send email
    if (process.env.RESEND_API_KEY && process.env.ADMIN_EMAIL) {
      const resend = new Resend(process.env.RESEND_API_KEY);
      await resend.emails.send({
        from: 'Norivelle Solution <onboarding@resend.dev>',
        to: process.env.ADMIN_EMAIL,
        subject: `New Contact Form Lead: ${name}`,
        html: `<h2>New Lead from Norivelle Website</h2><p><strong>Name:</strong> ${name}</p><p><strong>Email:</strong> ${email}</p><p><strong>Message:</strong> ${message}</p>`
      });
    }

    return res.status(200).json({ success: true, id: result.rows[0].id });
  } catch (error) {
    console.error('API Error:', error);
    
    if (error.code === '42P01') {
      return res.status(500).json({ error: 'Database table not found. Please create the "contacts" table.' });
    }

    return res.status(500).json({ error: error.message || 'Internal Server Error' });
  }
}