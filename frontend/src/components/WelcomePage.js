import React from "react"
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'
import AppBar from '@material-ui/core/AppBar'

class WelcomePage extends React.Component {
  state = {
    uid: null,
    startGame: false
  }

  handleNewGame = () => {
    this.setState({ startGame: true })
  }

  handleChangeId = (e) => {
    this.setState({ uid: e.target.value })
  }

  handleContinue = (event, value) => {
    this.setState({ startGame: true })
  }

  render() {
    return(
      <div>
        <Grid container spacing={24}>
          <Grid item xs={12}>Minesweeper</Grid>
          <Grid item xs={12}></Grid>
          <Grid item xs={12}></Grid>
          <Grid item xs={12}>
            <Button
              variant="contained"
              color="primary"
              onClick={this.handleNewGame}
            >
              Start New Game
            </Button>
          </Grid>
          <Grid item xs={12}>
            {' or '}
          </Grid>
          <Grid item xs={6}>
            <TextField
              label="Enter id"
              variant="outlined"
              name="id"
              onChange={this.handleChangeId}
            />
          </Grid>
          <Grid item xs={6}>
            <Button
              onClick={this.handleContinue}
              variant="contained"
            >
              Continue
            </Button>
          </Grid>
        </Grid>
      </div>
    )
  }
}

export default WelcomePage;
