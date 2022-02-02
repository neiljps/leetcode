import React from 'react';
import './App.css';

class Solution extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      //nums: [1, 1, 2],
      nums: [0, 0, 0, 1, 1, 2, 3, 3],
      k: 0
    }
  }

  removeDuplicates(){
    const res = [...this.state.nums]
    for (let i = 0; i < res.length; i++){
      if((i + 1) < res.length){
        while( ((i + 1) < res.length) &&
          (res[i] === res[i + 1])) {
            res.splice(i, 1)
        }
      }
    }

    this.setState({
      nums: res,
      k: res.length
    })
  }

  componentDidMount(){
    this.removeDuplicates()
  }

  render(){
    return (
        <div>
          {this.state.nums.map((num) => (
            <span>{num} </span>
          ))}
        </div>
    );
  }
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Solution/>
      </header>
    </div>
  );
}

export default App;
