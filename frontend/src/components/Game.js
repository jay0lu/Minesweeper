import React from 'react'
import axios from 'axios'

export default function Game (props) {
  let map = props.map
  let handleClick
  return(
    <Board
      map={map}
      onClick={handleClick}
    />
  )
}

function Board(props) {
  const map = props.map
  let grid = []

  for(let i = 0; i < 10; i++) {
    let bordRow = [];
    for(let j = 0; j < 10; j++) {
      let num = i * 10 + j;
      bordRow.push(<Square value={num} onClick={props.handleClick} />);
    }
    let row = (
      <div className="board-row">
        {bordRow}
      </div>
    );
    grid.push(row);
  }

  return(
    <div>{grid}</div>
  )
}

function Square(props) {
  const bold = {
    color: 'red'
  }
  let buttonStyle = bold
  return(
    <button
			style={buttonStyle}
			className="square"
			onClick={props.handleClick}
		>
    </button>
  )
}