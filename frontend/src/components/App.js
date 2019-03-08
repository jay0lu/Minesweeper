import React from 'react'
import ReactDOM from "react-dom"
import axios from 'axios'
import WelcomePage from './WelcomePage'
import Game from './Game'
import Dialog from '@material-ui/core/Dialog'
import DialogActions from '@material-ui/core/DialogActions'
import DialogContent from '@material-ui/core/DialogContent'
import DialogContentText from '@material-ui/core/DialogContentText'
import DialogTitle from '@material-ui/core/DialogTitle'
import Button from '@material-ui/core/Button'

class App extends React.Component{
  constructor(props) {
    super(props)
    this.state = {
      uid: null,
      start: false,
      map: [],
      isMine: false
    }
  }

  handleNewGame = () => {
    axios.get('http://127.0.0.1:8000/newGame/')
      .then(response => {
        let data = response.data
        this.setState({
          start: true,
          uid: data.uid,
          map: data.map,
          isMine: false
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
        let data = response.data
        this.setState({
          start: true,
          uid: data.uid,
          map: data.map,
          isMine: false
        })
      }).catch(error => {
        console.log(error)
      })
  }

  updateMap = (obj) => {
    this.setState({
      map: obj.map,
      isMine: obj.isMine
    })
  }

  render() {
    let open = this.state.isMine === 'true'
    let endGame = (
      <Dialog
        open={open}
        disableBackdropClick={true}
        keepMounted
        onClose={this.handleNewGame}
      >
        <DialogTitle>
          {"Game Over"}
        </DialogTitle>
        <DialogContent>
          <DialogContentText>
            {"This is a mine!"}
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={this.handleNewGame} color="primary">
            {'New Game'}
          </Button>
        </DialogActions>
      </Dialog>
    )

    let renderedComponent = this.state.start ? (
      <div>
        <Game
          map={this.state.map}
          uid={this.state.uid}
          isMine={this.state.isMine}
          updateMap={this.updateMap}
        />
        {endGame}
      </div>
    ) : (
      <WelcomePage
        handleNewGame={this.handleNewGame}
        handleChangeId={this.handleChangeId}
        handleContinue={this.handleContinue}
      />
    )

    // let appComponent = open ? endGame : renderedComponent

    return renderedComponent
  }
}

ReactDOM.render(
  <App />,
  document.getElementById("app")
)