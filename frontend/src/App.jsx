import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Home from './pages/Home'
import Result from './pages/Result'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import './App.css'
import './assets/styles.css'

function App() {
  return (
    <BrowserRouter>
      <div className="app-shell">
        <Navbar />
        <main className="page-content">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/result" element={<Result />} />
          </Routes>
        </main>
        <Footer />
      </div>
    </BrowserRouter>
  )
}

export default App
