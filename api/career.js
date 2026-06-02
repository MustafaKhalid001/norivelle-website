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

    const { 
      type, name, email, phone, address, age,
      job_title, experience, salary, education, 
      certifications, resume_link, cover_link, files 
    } = req.body;

    if (!name || !email || !phone || !type) {
      return res.status(400).json({ error: 'Name, email, phone, and application type are required.' });
    }

    // Auto-create table if it doesn't exist
    const createTableQuery = `
      CREATE TABLE IF NOT EXISTS applications (
        id SERIAL PRIMARY KEY,
        application_type VARCHAR(50),
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(100),
        address TEXT,
        age VARCHAR(10),
        job_title VARCHAR(255),
        experience VARCHAR(100),
        salary VARCHAR(100),
        education VARCHAR(255),
        certifications TEXT,
        resume_link TEXT,
        cover_link TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
      );
    `;
    await pool.query(createTableQuery);

    try {
      await pool.query('ALTER TABLE applications ADD COLUMN IF NOT EXISTS age VARCHAR(10);');
    } catch (e) {
      console.log('Age column might already exist or table creation failed.');
    }

    // Insert data
    const insertQuery = `
      INSERT INTO applications (
        application_type, name, email, phone, address, age,
        job_title, experience, salary, education, 
        certifications, resume_link, cover_link
      )
      VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13)
      RETURNING id;
    `;
    
    const values = [
      type, name, email, phone, address || '', age || '',
      job_title || '', experience || '', salary || '', education || '', 
      certifications || '', resume_link || '', cover_link || ''
    ];

    const result = await pool.query(insertQuery, values);
    const applicationId = result.rows[0].id;

    // Send email with attachments
    if (process.env.RESEND_API_KEY && process.env.ADMIN_EMAIL) {
      const resend = new Resend(process.env.RESEND_API_KEY);
      
      const attachments = [];
      if (files && files.length > 0) {
        files.forEach(f => {
          attachments.push({
            filename: f.name,
            content: f.content
          });
        });
      }

      await resend.emails.send({
        from: 'Norivelle Solution Careers <onboarding@resend.dev>',
        to: process.env.ADMIN_EMAIL,
        subject: `New ${type} Application: ${name}`,
        html: `
          <h2>New Application Received</h2>
          <p><strong>Type:</strong> ${type}</p>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Phone:</strong> ${phone}</p>
          <p><strong>Address:</strong> ${address}</p>
          <p><strong>Age:</strong> ${age}</p>
          <br/>
          <h3>Professional Details</h3>
          <p><strong>Job Title:</strong> ${job_title}</p>
          <p><strong>Experience:</strong> ${experience} years</p>
          <p><strong>Expected Salary:</strong> ${salary}</p>
          <p><strong>Education:</strong> ${education}</p>
          <p><strong>Certifications:</strong> ${certifications}</p>
          <br/>
          <h3>Links provided</h3>
          <p><strong>Resume Link:</strong> ${resume_link || 'N/A'}</p>
          <p><strong>Cover Letter / Link:</strong> ${cover_link || 'N/A'}</p>
          <br/>
          <p><em>Any uploaded files (Resume, CNIC, etc.) should be attached to this email.</em></p>
        `,
        attachments: attachments.length > 0 ? attachments : undefined
      });
    }

    return res.status(200).json({ success: true, id: applicationId });
  } catch (error) {
    console.error('API Error:', error);
    return res.status(500).json({ error: error.message || 'Internal Server Error' });
  }
}
