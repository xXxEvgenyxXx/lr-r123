import { useState } from 'react';
const questions = [ { q: '2+2?', a: ['3','4','5'], correct: 1 }, { q: 'React — это?', a: ['БД','Фреймворк','Библиотека'], correct: 2 }, { q: 'JSX — это?', a: ['CSS','HTML','JS'], correct: 1 }, { q: 'useState — это?', a: ['Хук','Компонент','Сервис'], correct: 0 }, { q: 'Где хранить глобальное состояние?', a: ['Redux','HTML','CSS'], correct: 0 } ];
export default function Quiz() {
	const [step, setStep] = useState(0);
	const [score, setScore] = useState(0);
	const answer = idx => { if (idx === questions[step].correct) setScore(score+1); setStep(step+1); };
	return step < questions.length ? (<div><div>{questions[step].q}</div>{questions[step].a.map((a,i) => <button key={i} onClick={() => answer(i)}>{a}</button>)}</div>) : (<div>Ваш результат: {score}/{questions.length}</div>);
}