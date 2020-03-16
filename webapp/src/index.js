import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import * as serviceWorker from './serviceWorker';
import Login from './views/Login';
import EchartsRadar from './echarts/EchartsRadar';
import Svg from './echarts/Svg'
import Dynamic from './echarts/Dynamic';
import RouterConfig from './routes/index'


ReactDOM.render(<RouterConfig />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
