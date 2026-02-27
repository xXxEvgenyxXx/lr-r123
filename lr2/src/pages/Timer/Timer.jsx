import { useState, useEffect } from 'react';
export default function Timer() {
	const [time, setTime] = useState(0);
	const [isRunning, setIsRunning] = useState(false);
	useEffect(() => { let interval = null; if (isRunning) { interval = setInterval(() => setTime(t => t + 1), 1000); } return () => clearInterval(interval); }, [isRunning]);
	return (<div><div>{time}s</div><button onClick={() => setIsRunning(!isRunning)}>{isRunning ? 'Стоп' : 'Старт'}</button><button onClick={() => { setTime(0); setIsRunning(false); }}>Сброс</button></div>);
}