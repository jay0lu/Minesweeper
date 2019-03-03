import React from 'react'
import ReactDOM from "react-dom"
import axios from 'axios'
import WelcomePage from './WelcomePage'
import Game from './Game'

class App extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      uid: null,
      start: false
    }
  }

  handleNewGame = () => {
    axios.get('http://127.0.0.1:8000/newGame/')
      .then(response => {
        console.log('---',response.data)
        let data = response.data
        this.setState({
          start: true,
          uid: data.uid,
          map: data.uid,
          isMine: data.isMine
        })
      }).catch(error => {
        console.log(error)
      })
  }

  handleChangeId = (e) => {
    this.setState({ uid: e.target.value })
  }

  handleContinue = () => {
    let uid = this.state.uid
    axios.get('http://127.0.0.1:8000/game/' + uid + '/')
      .then(response => {
        this.setState({ start: true })
      }).catch(error => {
        console.log(error)
      })
  }

  render() {
    let renderedComponent = this.state.start ? (
      <Game
        map={this.state.map}
        uid={this.state.uid}
        isMine={this.state.isMine}
      />
    ) : (
      <WelcomePage
        handleNewGame={this.handleNewGame}
        handleChangeId={this.handleChangeId}
        handleContinue={this.handleContinue}
      />
    )
    return renderedComponent
  }
}

ReactDOM.render(
  <App />,
  document.getElementById("app")
)