import { useState } from 'react';
export default function Calculator() {
	const [display, setDisplay] = useState('0');
	const [prev, setPrev] = useState(null);
	const [op, setOp] = useState(null);
	const handleNumber = n => setDisplay(display === '0' ? n : display + n);
	const handleOperation = o => { setPrev(parseFloat(display)); setOp(o); setDisplay('0'); };
	const calculate = () => { let result; const curr = parseFloat(display); switch(op) { case '+': result = prev + curr; break; case '-': result = prev - curr; break; case '*': result = prev * curr; break; case '/': result = curr !== 0 ? prev / curr : 'Error'; break; default: return; } setDisplay(result.toString()); setOp(null); setPrev(null); };
	const clear = () => { setDisplay('0'); setPrev(null); setOp(null); };
	return (<div><div>{display}</div><button onClick={clear}>C</button><button onClick={() => handleOperation('+')}>+</button><button onClick={() => handleOperation('-')}>-</button><button onClick={() => handleOperation('*')}>*</button><button onClick={() => handleOperation('/')}>/</button><button onClick={calculate}>=</button><button onClick={() => handleNumber('1')}>1</button><button onClick={() => handleNumber('2')}>2</button><button onClick={() => handleNumber('3')}>3</button><button onClick={() => handleNumber('4')}>4</button><button onClick={() => handleNumber('5')}>5</button><button onClick={() => handleNumber('6')}>6</button><button onClick={() => handleNumber('7')}>7</button><button onClick={() => handleNumber('8')}>8</button><button onClick={() => handleNumber('9')}>9</button><button onClick={() => handleNumber('0')}>0</button><button onClick={() => handleNumber('.')}>.</button></div>);
}