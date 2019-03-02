import React from 'react'
import par from 'par'
import axios from 'axios'

export default function Game (props) {
  let map = props.map
  let handleClick = (num) => {
    axios.post('http://127.0.0.1:8000/moves', {
      position: num
    }).then(
      // updateMap
    )
  }

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
      bordRow.push(<Square onClick={par(props.onClick, num)} />);
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
  let showNum = props.mapNum
  showNum = -1
  let renderSquare = showNum === -1 ? (
    <button
			className="square"
			onClick={props.onClick}
		/>
  ) : (
    <button
      disabled
      className="square"
    >
      {showNum}
    </button>
  )

  return renderSquare
}