import { useState } from 'react'
function Calculator() {
 const [display, setDisplay] = useState('0')
 const handleNumber = (num) => {
    setDisplay(display === '0' ? num : display + num)
 }
 const [previousValue, setPreviousValue] = useState(null)
 const [operation, setOperation] = useState(null)
 const handleOperation = (op) => {
    setPreviousValue(parseFloat(display))
    setOperation(op)
 }
 const calculate = () => {
    const current = parseFloat(display)
    let result

    switch(operation) {
        case '+': result = previousValue + current; break
        case '-': result = previousValue - current; break
        case '*': result = previousValue * current; break
        case '/': result = previousValue / current; break
        default: return
    }

    setDisplay(result.toString())
    setOperation(null)
    setPreviousValue(null)
    }
  const clear = () => {
    setDisplay('0')
    setPreviousValue(null)
    setOperation(null)
  }
 return (
    <div className="calculator">
        <div className="display">{display}</div>
        <div className="buttons">
            <button onClick={clear}>C</button>
            <button onClick={() => handleOperation('/')}>/</button>
            <button onClick={() => handleOperation('*')}>*</button>
            <button onClick={() => handleOperation('-')}>-</button>

            <button onClick={() => handleNumber('7')}>7</button>
            <button onClick={() => handleNumber('8')}>8</button>
            <button onClick={() => handleNumber('9')}>9</button>
            <button onClick={() => handleOperation('+')}>+</button>

            <button onClick={() => handleNumber('4')}>4</button>
            <button onClick={() => handleNumber('5')}>5</button>
            <button onClick={() => handleNumber('6')}>6</button>
            <button onClick={calculate}>=</button>

            <button onClick={() => handleNumber('1')}>1</button>
            <button onClick={() => handleNumber('2')}>2</button>
            <button onClick={() => handleNumber('3')}>3</button>
            <button onClick={() => handleNumber('0')}>0</button>
        </div>
    </div>
 )
}
export default Calculator