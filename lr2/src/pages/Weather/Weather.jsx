import { useState } from 'react';
export default function Weather() {
	const [city, setCity] = useState('');
	const [weather, setWeather] = useState(null);
	const fetchWeather = () => { if (!city.trim()) return; setWeather({ city, temperature: Math.round(Math.random() * 30 - 5), description: ['Солнечно', 'Облачно', 'Дождь', 'Снег'][Math.floor(Math.random() * 4)] }); };
	return (<div><input value={city} onChange={e => setCity(e.target.value)} placeholder="Введите город" /><button onClick={fetchWeather}>Найти</button>{weather && (<div><h3>{weather.city}</h3><div>{weather.temperature}°C</div><div>{weather.description}</div></div>)}</div>);
}