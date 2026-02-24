import React from 'react';
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
