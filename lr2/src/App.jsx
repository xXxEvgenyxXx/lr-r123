import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage/HomePage';
import Calculator from './pages/Calculator/Calculator';
import TodoList from './pages/TodoList/TodoList';
import Weather from './pages/Weather/Weather';
import Timer from './pages/Timer/Timer';
import Quiz from './pages/Quiz/Quiz';
import Notes from './pages/Notes/Notes';
import Gallery from './pages/Gallery/Gallery';
import Converter from './pages/Converter/Converter';
import Game from './pages/Game/Game';
import Portfolio from './pages/Portfolio/Portfolio';

function App() {

  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/calculator" element={<Calculator />}/>
          <Route path="/todolist" element={<TodoList />}/>
          <Route path="/weather" element={<Weather />}/>
          <Route path="/timer" element={<Timer />}/>
          <Route path="/quiz" element={<Quiz />}/>
          <Route path="/notes" element={<Notes />}/>
          <Route path="/gallery" element={<Gallery />}/>
          <Route path="/converter" element={<Converter />}/>
          <Route path="/game" element={<Game />}/>
          <Route path="/portfolio" element={<Portfolio />}/>
        </Routes>
      </div>
    </Router>
  )
}

export default App
