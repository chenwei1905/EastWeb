import React from "react";
import ReactDOM from "react-dom";
import { createStore } from "redux";
import Counter from "./Counter";
import reducer from "./reducer";
const store = createStore(reducer)
const rootEl = document.getElementById('root')

const render = () => ReactDOM.render(
  <Counter
    value={store.getState()}
    onIncrement={() => store.dispatch({ type: 'INCREMENT' })}
    onDecrement={() => store.dispatch({ type: 'DECREMENT' })}
  />,
  rootEl
)

store.subscribe(render)

export {render} ;
