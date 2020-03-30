import React from 'react'
import ReactDOM from 'react-dom'
import Board from './Board'
import { observe } from './observe'

const root = document.getElementById('root')

const Game = observe(knightPosition =>
  ReactDOM.render(<Board knightPosition={knightPosition} />, root),
)
export default Game;