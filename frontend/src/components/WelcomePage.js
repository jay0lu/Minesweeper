import React from 'react'
import Grid from '@material-ui/core/Grid';
import Button from '@material-ui/core/Button'
import TextField from '@material-ui/core/TextField'

function WelcomePage(props) {
  return(
    <div align="center">
      <Grid container spacing={24}>
        <Grid item xs={12}>
          <h1>Minesweeper</h1>
        </Grid>
        <Grid item xs={12}></Grid>
        <Grid item xs={12}></Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={props.handleNewGame}
          >
            Start New Game
          </Button>
        </Grid>
        <Grid item xs={12}>
          {' or '}
        </Grid>
        <Grid item xs={3}></Grid>
        <Grid item xs={3}>
          <TextField
            label="Enter id"
            variant="outlined"
            name="id"
            onChange={props.handleChangeId}
          />
        </Grid>
        <Grid item xs={3}>
          <Button
            onClick={props.handleContinue}
            variant="contained"
          >
            Continue
          </Button>
        <Grid item xs={3}></Grid>
        </Grid>
      </Grid>
    </div>
  )
}

export default WelcomePage;
