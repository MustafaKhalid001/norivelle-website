const { Pool } = require('pg');
const { Resend } = require('resend');

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false
  }
});

const resend = new Resend(process.env.RESEND_API_KEY);

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  const { name, company, email, phone, country, services, subject, message } = req.body;

  if (!name || !email || !message) {
    return res.status(400).json({ error: 'Name, email, and message are required.' });
  }

  try {
    const query = `
      INSERT INTO contacts (name, company, email, phone, country, services, subject, message)
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
      RETURNING id;
    `;
    
    // Services might be an array, so convert to string if it is
    const servicesStr = Array.isArray(services) ? services.join(', ') : (services || '');

    const values = [
      name,
      company || '',
      email,
      phone || '',
      country || '',
      servicesStr,
      subject || '',
      message
    ];

    const result = await pool.query(query, values);

    // After successful database insert, send the email!
    if (process.env.RESEND_API_KEY && process.env.ADMIN_EMAIL) {
      await resend.emails.send({
        from: 'Norivelle Solution <onboarding@resend.dev>', // Resend's default testing domain
        to: process.env.ADMIN_EMAIL,
        subject: `New Contact Form Lead: ${name}`,
        html: `
          <h2>New Lead from Norivelle Website</h2>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Company:</strong> ${company || 'N/A'}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Phone:</strong> ${phone}</p>
          <p><strong>Country:</strong> ${country}</p>
          <p><strong>Services Interested:</strong> ${servicesStr || 'N/A'}</p>
          <p><strong>Subject:</strong> ${subject}</p>
          <h3>Message:</h3>
          <p>${message.replace(/\n/g, '<br>')}</p>
        `
      });
    }

    return res.status(200).json({ success: true, id: result.rows[0].id });
  } catch (error) {
    console.error('Database/Email Error:', error);
    
    // If table doesn't exist, provide a helpful message
    if (error.code === '42P01') {
      return res.status(500).json({ 
        error: 'Database table not found. Please create the "contacts" table in your Neon dashboard.' 
      });
    }

    return res.status(500).json({ error: 'Internal Server Error' });
  }
}
