import React from 'react'
import par from 'par'
import axios from 'axios'


export default function Game(props) {
  let map = props.map
  let uid = props.uid

  const config = {
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded'
    }
  }

  let handleClick = (num) => {
    let data = {
      position: num
    }

    axios.defaults.xsrfCookieName = 'csrftoken'
    axios.defaults.xsrfHeaderName = 'X-CSRFToken'
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/moves/' + num,
      data: JSON.stringify(data)
    })
  }

  let updateMap = (currentMap) => {
    map = currentMap
  }

  return(
    <div>
      <h1>Uid: {uid}</h1>
      <Board
        map={map}
        onClick={handleClick}
      />
    </div>
  )
}

function Board(props) {
  const map = props.map
  let grid = []

  for(let i = 0; i < 10; i++) {
    let bordRow = [];
    for(let j = 0; j < 10; j++) {
      let index = i * 10 + j;
      bordRow.push(<Square onClick={par(props.onClick, index)} map={map} index={index} />);
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
  let map = props.map
  let index = props.index
  let showNum = map[index]

  let renderSquare = showNum === -1 ? (
    <button
      key={index}
			className="square"
			onClick={props.onClick}
		/>
  ) : (
    <button
    key={index}
      disabled
      className="square"
    >
      {showNum}
    </button>
  )

  return renderSquare
}