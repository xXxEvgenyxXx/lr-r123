import React from 'react';
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
