import { useState } from 'react';
export default function Converter() {
	const [value, setValue] = useState('');
	const [result, setResult] = useState(null);
	const convert = () => setResult(Number(value) * 2);
	return (<div><input value={value} onChange={e => setValue(e.target.value)} placeholder="Введите число" /><button onClick={convert}>Удвоить</button>{result !== null && <div>Результат: {result}</div>}</div>);
}