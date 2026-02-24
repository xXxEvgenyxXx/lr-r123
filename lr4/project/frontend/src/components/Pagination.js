import React from 'react';
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
