import { useState } from 'react';
export default function Notes() {
	const [notes, setNotes] = useState([]);
	const [text, setText] = useState('');
	const addNote = () => { if (text.trim()) { setNotes([...notes, { id: Date.now(), text }]); setText(''); } };
	const deleteNote = id => setNotes(notes.filter(n => n.id !== id));
	return (<div><input value={text} onChange={e => setText(e.target.value)} placeholder="Новая заметка" /><button onClick={addNote}>Добавить</button><ul>{notes.map(n => <li key={n.id}>{n.text}<button onClick={() => deleteNote(n.id)}>Удалить</button></li>)}</ul></div>);
}