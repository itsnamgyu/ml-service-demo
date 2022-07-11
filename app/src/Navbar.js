import './Navbar.css';
import React from 'react';
import {FontAwesomeIcon} from '@fortawesome/react-fontawesome'
import {faGithub, faReact} from '@fortawesome/free-brands-svg-icons'

class Navbar extends React.Component {
  render() {
    return <nav className="navbar navbar-mobile fixed-top bg-white navbar-expand-lg navbar-light px-3 py-3 border-bottom">
      <button className="navbar-brand btn px-0" onClick={this.props.onNavigateHome}>
        <p className="fw-bold m-0">
          <FontAwesomeIcon icon={faReact} className="me-2"/>
          ML Service Demo (React)
        </p>
      </button>
      <a className="navbar-brand ms-auto d-flex align-items-center" href="https://github.com/itsnamgyu/ml-service-demo">
        <FontAwesomeIcon icon={faGithub} className="me-2"/>
        <div className="m-0">View on GitHub</div>
      </a>
    </nav>
  }
}

export default Navbar