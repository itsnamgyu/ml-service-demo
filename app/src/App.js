import React from 'react';
import './App.css';
import Navbar from './Navbar';
import PostList from './PostList';
import PostCreate from './PostCreate';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      location: "postList",
    }
    this.navigateHome = this.navigateHome.bind(this)
    this.navigateToPostCreate= this.navigateToPostCreate.bind(this)
  }

  navigateHome() {
    this.setState({
      location: "postList"
    })
  }

  navigateToPostCreate() {
    this.setState({
      location: "postCreate"
    })
  }

  render() {
    return (
      <div className="App">
        <Navbar onNavigateHome={this.navigateHome}/>
        <div className="App-body container">
          <div className="row justify-content-center">
            <div className="col-12 col-md-8">
              {this.state.location === "postList"
                ? <PostList navigateToPostCreate={this.navigateToPostCreate}/>
                : <PostCreate navigateBack={this.navigateHome}/>
              }
            </div>
          </div>
        </div>

        <div className="py-5"/>
        <div className="py-5"/>
        <div className="py-5"/>
        <div className="py-5"/>

        <div className="text-center">
          <p className="App-copyright">Copyright 2022 © Namgyu Ho. All Rights Reserved. </p>
        </div>
      </div>
    );
  }
}

export default App;
