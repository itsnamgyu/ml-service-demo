import './PostList.css';
import React from 'react';
import CsrfToken from "./CsrfToken";
import axios from 'axios'

class PostCreate extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      file: null,
      error: "",
    };
    this.onFormSubmit = this.onFormSubmit.bind(this)
    this.onChange = this.onChange.bind(this)
    this.submitForm = this.submitForm.bind(this)
  }

  onChange(e) {
    this.setState({file: e.target.files[0]})
  }

  onFormSubmit(e) {
    e.preventDefault()
    this.submitForm()
  }

  submitForm() {
    if (this.state.file == null) {
      this.setState({error: "You must specify a file"})
      return
    }
    const url = '/api/posts/create/';
    const formData = new FormData();
    formData.append('image', this.state.file)
    axios.post(url, formData).then(response => {
      this.props.navigateBack()
    }).catch(error => {
      this.setState({error: error.message});
    });
  }

  render() {
    return <div>
      <h2 className="mb-4">New Post</h2>
      <form method="post" encType="multipart/form-data" onSubmit={this.onFormSubmit}>
        <CsrfToken/>
        <div className="mb-3">
          <label className="form-label" htmlFor="id_image">
            Image
          </label>
          <br/>
          <input type="file" name="image" accept="image/*" className="form-control" required
                 id="id_image" onChange={this.onChange}/>
        </div>
        <p className="text-danger">
          {this.state.error}
        </p>
        <div className="text-end">
          <button className="btn btn-secondary me-2" onClick={this.props.navigateBack}>Cancel</button>
          <button className="btn btn-primary me-2" type="submit">Save</button>
        </div>
      </form>
    </div>
  }
}

export default PostCreate