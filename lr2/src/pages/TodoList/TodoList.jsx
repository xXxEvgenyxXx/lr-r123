import { useState } from 'react';
export default function TodoList() {
	const [todos, setTodos] = useState([]);
	const [input, setInput] = useState('');
	const addTodo = () => { if (input.trim()) { setTodos([...todos, { id: Date.now(), text: input, completed: false }]); setInput(''); } };
	const toggleTodo = id => setTodos(todos.map(t => t.id === id ? { ...t, completed: !t.completed } : t));
	const deleteTodo = id => setTodos(todos.filter(t => t.id !== id));
	return (<div><input value={input} onChange={e => setInput(e.target.value)} placeholder="Введите задачу" /><button onClick={addTodo}>Добавить</button><ul>{todos.map(t => <li key={t.id}><span style={{ textDecoration: t.completed ? 'line-through' : 'none' }} onClick={() => toggleTodo(t.id)}>{t.text}</span><button onClick={() => deleteTodo(t.id)}>Удалить</button></li>)}</ul></div>);
}