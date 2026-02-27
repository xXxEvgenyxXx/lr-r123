import { Link } from "react-router-dom";

const HomePage = () => {
    
    return (
        <div>
            <h1>Главная страница</h1>
            <Link target="_blank" to="/calculator">Калькулятор</Link>
            <Link target="_blank" to="/todolist">TodoList</Link>
            <Link target="_blank" to="/weather">Погода</Link>
            <Link target="_blank" to="/timer">Таймер</Link>
            <Link target="_blank" to="/quiz">Quiz</Link>
            <Link target="_blank" to="/notes">Notes</Link>
            <Link target="_blank" to="/gallery">Галерея</Link>
            <Link target="_blank" to="/converter">Конвертер</Link>
            <Link target="_blank" to="/game">Игра</Link>
            <Link target="_blank" to="/portfolio">Портфолио</Link>
        </div>
    );
};
export default HomePage;