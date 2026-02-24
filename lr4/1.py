import os
import json


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    base = os.path.dirname(__file__)
    root = os.path.join(base, 'project')

    files = {
        # docker-compose
        os.path.join(root, 'docker-compose.yml'): '''version: '3.8'

services:
  postgres:
    image: postgres:15
    container_name: my_postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: password
      POSTGRES_DB: shopdb
    ports:
      - "5432:5432"
    volumes:
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql
      - pgdata:/var/lib/postgresql/data

  adminer:
    image: adminer
    restart: unless-stopped
    ports:
      - "8080:8080"

volumes:
  pgdata:
''',

        # init.sql
        os.path.join(root, 'init.sql'): '''CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category VARCHAR(50) NOT NULL,
    image_url TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Electronics (20 товаров)
INSERT INTO products (name, price, category, image_url) VALUES
('Смартфон Xiaomi Redmi Note 11', 199.99, 'electronics', 'https://via.placeholder.com/150?text=Phone'),
('Ноутбук Lenovo IdeaPad 3', 499.99, 'electronics', 'https://via.placeholder.com/150?text=Laptop'),
('Наушники Sony WH-1000XM4', 349.99, 'electronics', 'https://via.placeholder.com/150?text=Headphones'),
('Планшет Samsung Tab A8', 229.99, 'electronics', 'https://via.placeholder.com/150?text=Tablet'),
('Монитор Dell 24"', 179.99, 'electronics', 'https://via.placeholder.com/150?text=Monitor'),
('Клавиатура Logitech MX Keys', 119.99, 'electronics', 'https://via.placeholder.com/150?text=Keyboard'),
('Мышь Logitech MX Master 3', 99.99, 'electronics', 'https://via.placeholder.com/150?text=Mouse'),
('Внешний диск WD 1TB', 59.99, 'electronics', 'https://via.placeholder.com/150?text=HDD'),
('Роутер TP-Link Archer C6', 49.99, 'electronics', 'https://via.placeholder.com/150?text=Router'),
('Принтер HP LaserJet', 129.99, 'electronics', 'https://via.placeholder.com/150?text=Printer'),
('Фитнес-браслет Xiaomi Mi Band 6', 39.99, 'electronics', 'https://via.placeholder.com/150?text=Band'),
('Умные часы Samsung Galaxy Watch 4', 249.99, 'electronics', 'https://via.placeholder.com/150?text=Watch'),
('Игровая приставка Sony PS5', 499.99, 'electronics', 'https://via.placeholder.com/150?text=PS5'),
('Фотоаппарат Canon EOS 2000D', 399.99, 'electronics', 'https://via.placeholder.com/150?text=Camera'),
('Микрофон Blue Yeti', 129.99, 'electronics', 'https://via.placeholder.com/150?text=Microphone'),
('Веб-камера Logitech C920', 79.99, 'electronics', 'https://via.placeholder.com/150?text=Webcam'),
('Электронная книга Amazon Kindle', 89.99, 'electronics', 'https://via.placeholder.com/150?text=Kindle'),
('Портативная колонка JBL Flip 5', 69.99, 'electronics', 'https://via.placeholder.com/150?text=Speaker'),
('Зарядное устройство Anker 65W', 29.99, 'electronics', 'https://via.placeholder.com/150?text=Charger'),
('SSD Samsung 870 EVO 500GB', 54.99, 'electronics', 'https://via.placeholder.com/150?text=SSD'),

-- Clothing (20 товаров)
('Футболка мужская хлопок', 14.99, 'clothing', 'https://via.placeholder.com/150?text=T-shirt'),
('Джинсы Levi''s 501', 69.99, 'clothing', 'https://via.placeholder.com/150?text=Jeans'),
('Куртка зимняя', 129.99, 'clothing', 'https://via.placeholder.com/150?text=Jacket'),
('Платье вечернее', 89.99, 'clothing', 'https://via.placeholder.com/150?text=Dress'),
('Кроссовки Nike Air', 79.99, 'clothing', 'https://via.placeholder.com/150?text=Sneakers'),
('Рубашка офисная', 34.99, 'clothing', 'https://via.placeholder.com/150?text=Shirt'),
('Шорты летние', 19.99, 'clothing', 'https://via.placeholder.com/150?text=Shorts'),
('Свитер шерстяной', 49.99, 'clothing', 'https://via.placeholder.com/150?text=Sweater'),
('Пальто', 159.99, 'clothing', 'https://via.placeholder.com/150?text=Coat'),
('Брюки классические', 44.99, 'clothing', 'https://via.placeholder.com/150?text=Trousers'),
('Юбка', 29.99, 'clothing', 'https://via.placeholder.com/150?text=Skirt'),
('Худи', 39.99, 'clothing', 'https://via.placeholder.com/150?text=Hoodie'),
('Носки', 4.99, 'clothing', 'https://via.placeholder.com/150?text=Socks'),
('Шапка', 9.99, 'clothing', 'https://via.placeholder.com/150?text=Hat'),
('Перчатки', 7.99, 'clothing', 'https://via.placeholder.com/150?text=Gloves'),
('Шарф', 12.99, 'clothing', 'https://via.placeholder.com/150?text=Scarf'),
('Толстовка', 29.99, 'clothing', 'https://via.placeholder.com/150?text=Sweatshirt'),
('Пиджак', 79.99, 'clothing', 'https://via.placeholder.com/150?text=Blazer'),
('Комбинезон', 59.99, 'clothing', 'https://via.placeholder.com/150?text=Jumpsuit'),
('Купальник', 24.99, 'clothing', 'https://via.placeholder.com/150?text=Swimsuit'),

-- Books (20 товаров)
('Война и мир. Том 1', 12.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('1984', 9.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Мастер и Маргарита', 11.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Преступление и наказание', 10.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Маленький принц', 7.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Гарри Поттер и философский камень', 15.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Унесенные ветром', 14.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Три товарища', 9.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Портрет Дориана Грея', 8.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Гордость и предубеждение', 9.49, 'books', 'https://via.placeholder.com/150?text=Book'),
('Анна Каренина', 11.49, 'books', 'https://via.placeholder.com/150?text=Book'),
('Идиот', 10.49, 'books', 'https://via.placeholder.com/150?text=Book'),
('Братья Карамазовы', 13.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Сто лет одиночества', 12.49, 'books', 'https://via.placeholder.com/150?text=Book'),
('Над пропастью во ржи', 8.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Великий Гэтсби', 9.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Шантарам', 14.49, 'books', 'https://via.placeholder.com/150?text=Book'),
('Алхимик', 7.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Тень ветра', 10.99, 'books', 'https://via.placeholder.com/150?text=Book'),
('Код да Винчи', 11.99, 'books', 'https://via.placeholder.com/150?text=Book');
''',

        # backend
        os.path.join(root, 'backend', 'server.js'): '''require('dotenv').config();
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
''',

        os.path.join(root, 'backend', 'package.json'): json.dumps({
            "name": "backend",
            "version": "1.0.0",
            "main": "server.js",
            "scripts": {"start": "node server.js", "dev": "nodemon server.js"},
            "dependencies": {"express": "^4.18.2", "pg": "^8.0.0", "cors": "^2.8.5", "dotenv": "^16.0.0"}
        }, ensure_ascii=False, indent=2),

        os.path.join(root, 'backend', '.env'): '''DB_USER=user
DB_PASSWORD=password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=shopdb
PORT=5000
''',

        # frontend
        os.path.join(root, 'frontend', 'public', 'index.html'): '''<!doctype html>
<html lang="ru">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>Shop</title>
  </head>
  <body>
    <div id="root"></div>
    <script src="/static/js/bundle.js"></script>
  </body>
</html>
''',

        os.path.join(root, 'frontend', 'src', 'index.js'): '''import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';
import './App.css';

const container = document.getElementById('root');
const root = createRoot(container);
root.render(<App />);
''',

        os.path.join(root, 'frontend', 'src', 'App.js'): '''import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Sidebar from './components/Sidebar';
import ProductList from './components/ProductList';
import Pagination from './components/Pagination';
import './App.css';

function App() {
  const [category, setCategory] = useState('electronics');
  const [products, setProducts] = useState([]);
  const [currentPage, setCurrentPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchProducts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [category, currentPage]);

  const fetchProducts = async () => {
    setLoading(true);
    try {
      const response = await axios.get('http://localhost:5000/api/products', {
        params: { category, page: currentPage },
      });
      setProducts(response.data.products);
      setTotalPages(response.data.totalPages);
    } catch (error) {
      console.error('Ошибка загрузки товаров:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCategoryChange = (newCategory) => {
    setCategory(newCategory);
    setCurrentPage(1);
  };

  const goToPage = (page) => {
    if (page >= 1 && page <= totalPages) {
      setCurrentPage(page);
    }
  };

  return (
    <div className="app">
      <Sidebar selectedCategory={category} onSelectCategory={handleCategoryChange} />
      <main className="main-content">
        {loading ? (
          <div className="loader">Загрузка...</div>
        ) : (
          <>
            <ProductList products={products} />
            <Pagination currentPage={currentPage} totalPages={totalPages} onPageChange={goToPage} />
          </>
        )}
      </main>
    </div>
  );
}

export default App;
''',

        os.path.join(root, 'frontend', 'src', 'App.css'): '''* { box-sizing: border-box; margin:0; padding:0 }
body { font-family: Arial, sans-serif }
.app { display:flex }
.main-content { margin-left:220px; flex:1; padding:20px }
.loader { text-align:center; font-size:20px; margin-top:50px }
''',

        # components
        os.path.join(root, 'frontend', 'src', 'components', 'Sidebar.js'): '''import React from 'react';
import './Sidebar.css';

const categories = [
  { id: 'electronics', label: 'Электроника' },
  { id: 'clothing', label: 'Одежда' },
  { id: 'books', label: 'Книги' },
];

function Sidebar({ selectedCategory, onSelectCategory }) {
  return (
    <aside className="sidebar">
      <h3>Категории</h3>
      <ul>
        {categories.map((cat) => (
          <li key={cat.id}>
            <button className={selectedCategory === cat.id ? 'active' : ''} onClick={() => onSelectCategory(cat.id)}>
              {cat.label}
            </button>
          </li>
        ))}
      </ul>
    </aside>
  );
}

export default Sidebar;
''',

        os.path.join(root, 'frontend', 'src', 'components', 'Sidebar.css'): '''.sidebar { width:200px; background:#f4f4f4; padding:20px; height:100vh; position:fixed; left:0; top:0 }
.sidebar h3 { margin-top:0 }
.sidebar ul { list-style:none; padding:0 }
.sidebar li { margin-bottom:10px }
.sidebar button { width:100%; padding:10px; background:#ddd; border:none; cursor:pointer; font-size:16px; border-radius:4px }
.sidebar button.active { background:#007bff; color:white }
.sidebar button:hover { background:#ccc }
''',

        os.path.join(root, 'frontend', 'src', 'components', 'ProductList.js'): '''import React from 'react';
import ProductCard from './ProductCard';
import './ProductList.css';

function ProductList({ products }) {
  if (products.length === 0) {
    return <p className="no-products">Нет товаров в этой категории</p>;
  }

  return (
    <div className="product-list">
      {products.map((product) => (
        <ProductCard key={product.id} product={product} />
      ))}
    </div>
  );
}

export default ProductList;
''',

        os.path.join(root, 'frontend', 'src', 'components', 'ProductList.css'): '''.product-list { display:grid; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); gap:20px; padding:20px }
''',

        os.path.join(root, 'frontend', 'src', 'components', 'ProductCard.js'): '''import React from 'react';
import './ProductCard.css';

function ProductCard({ product }) {
  return (
    <div className="product-card">
      <img src={product.image_url} alt={product.name} />
      <h4>{product.name}</h4>
      <p className="price">{product.price} ₽</p>
    </div>
  );
}

export default ProductCard;
''',

        os.path.join(root, 'frontend', 'src', 'components', 'ProductCard.css'): '''.product-card { border:1px solid #ddd; border-radius:8px; padding:15px; text-align:center; box-shadow:0 2px 5px rgba(0,0,0,0.1) }
.product-card img { max-width:100%; height:150px; object-fit:cover; border-radius:4px }
.product-card h4 { margin:10px 0 5px; font-size:1.1rem }
.product-card .price { font-weight:bold; color:#007bff }
''',

        os.path.join(root, 'frontend', 'src', 'components', 'Pagination.js'): '''import React from 'react';
import './Pagination.css';

function Pagination({ currentPage, totalPages, onPageChange }) {
  return (
    <div className="pagination">
      <button onClick={() => onPageChange(1)} disabled={currentPage === 1}>&lt;&lt;</button>
      <button onClick={() => onPageChange(currentPage - 1)} disabled={currentPage === 1}>&lt;</button>
      <span className="page-info">Страница {currentPage} из {totalPages}</span>
      <button onClick={() => onPageChange(currentPage + 1)} disabled={currentPage === totalPages}>&gt;</button>
      <button onClick={() => onPageChange(totalPages)} disabled={currentPage === totalPages}>&gt;&gt;</button>
    </div>
  );
}

export default Pagination;
''',

        os.path.join(root, 'frontend', 'src', 'components', 'Pagination.css'): '''.pagination { display:flex; justify-content:center; align-items:center; gap:10px; padding:20px }
.pagination button { padding:8px 12px; border:1px solid #007bff; background:white; color:#007bff; cursor:pointer; border-radius:4px }
.pagination button:disabled { border-color:#ccc; color:#ccc; cursor:not-allowed }
.pagination .page-info { font-size:16px }
''',

        os.path.join(root, 'frontend', 'package.json'): json.dumps({
            "name": "frontend",
            "version": "1.0.0",
            "private": True,
            "dependencies": {"react": "^18.2.0", "react-dom": "^18.2.0", "axios": "^1.4.0"},
            "scripts": {"start": "react-scripts start", "build": "react-scripts build"}
        }, ensure_ascii=False, indent=2),

        os.path.join(root, 'frontend', 'README.md'): '# Frontend\n\nReact app that fetches products from backend API and displays them with pagination.'
    }

    for path, content in files.items():
        write_file(path, content)

    print('Проект создан в:', root)
    print('Далее: запустите `docker-compose up -d` в папке проекта, затем backend и frontend согласно README.')


if __name__ == '__main__':
    main()
