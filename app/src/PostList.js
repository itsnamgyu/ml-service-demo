import './PostList.css';
import React from 'react';
import axios from 'axios';

class Post extends React.Component {
  render() {
    return <div className="col-6 mb-4">
      <div className="Post">
        <h4 className="Post-prediction">{this.props.post.prediction}</h4>
        <img className="Post-image w-100" src={this.props.post.image_url}/>
      </div>
    </div>
  }
}

class PostList extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      posts: [],
    };
    this.getPosts = this.getPosts.bind(this);
  }

  componentDidMount() {
    this.getPosts()
  }

  getPosts() {
    axios.get("/api/posts").then(response => {
      this.setState({
        "posts": response.data
      });
    })
  }

  render() {
    return <div>
      <h2 className="mb-4">Post List</h2>
      <div className="row">
        {
          this.state.posts.map((post) => <Post post={post} key={post.id}/>)
        }
      </div>
      <div className="text-end">
        <button onClick={this.props.navigateToPostCreate} className="btn btn-primary">Add Post</button>
      </div>
    </div>
  }
}

export default PostList