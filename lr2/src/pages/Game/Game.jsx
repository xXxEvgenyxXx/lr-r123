import { useState } from 'react';
const secret = Math.floor(Math.random()*100)+1;
export default function Game() {
	const [guess, setGuess] = useState('');
	const [msg, setMsg] = useState('');
	const check = () => { const g = Number(guess); if (g === secret) setMsg('Угадали!'); else if (g < secret) setMsg('Больше'); else setMsg('Меньше'); };
	return (<div><input value={guess} onChange={e => setGuess(e.target.value)} placeholder="Угадайте число 1-100" /><button onClick={check}>Проверить</button><div>{msg}</div></div>);
}