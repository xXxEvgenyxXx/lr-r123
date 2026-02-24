require('dotenv').config();
const express = require('express');
const { Pool } = require('pg');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  database: process.env.DB_NAME,
});

pool.connect((err) => {
  if (err) {
    console.error('Ошибка подключения к БД:', err);
  } else {
    console.log('Подключено к PostgreSQL');
  }
});

app.get('/api/products', async (req, res) => {
  try {
    const category = req.query.category;
    const page = parseInt(req.query.page) || 1;
    const limit = 6;
    const offset = (page - 1) * limit;

    let categoryCondition = '';
    let queryParams = [];
    if (category) {
      categoryCondition = 'WHERE category = $1';
      queryParams = [category];
    }

    const countQuery = `SELECT COUNT(*) FROM products ${categoryCondition}`;
    const countResult = await pool.query(countQuery, queryParams);
    const totalCount = parseInt(countResult.rows[0].count);

    const dataQuery = `
      SELECT id, name, price, category, image_url
      FROM products
      ${categoryCondition}
      ORDER BY id
      LIMIT $${queryParams.length + 1} OFFSET $${queryParams.length + 2}
    `;
    const dataParams = [...queryParams, limit, offset];
    const dataResult = await pool.query(dataQuery, dataParams);

    res.json({
      products: dataResult.rows,
      total: totalCount,
      page,
      totalPages: Math.ceil(totalCount / limit),
    });
  } catch (error) {
    console.error(error);
    res.status(500).json({ error: 'Ошибка сервера' });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Сервер запущен на порту ${PORT}`);
});
