import { Link } from 'react-router-dom'

function Navbar() {
  return (
    <header className="navbar glass-card">
      <Link className="brand" to="/">
        <span className="brand-mark">R</span>
        <span>Resume Extractor</span>
      </Link>
      <nav className="nav-links" aria-label="Primary navigation">
        <Link to="/">Home</Link>
        <Link to="/result">Results</Link>
      </nav>
    </header>
  )
}

export default Navbar
