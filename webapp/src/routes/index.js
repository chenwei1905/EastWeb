import React, { Component } from 'react';
import { BrowserRouter as Router, Link, Route } from 'react-router-dom';
import '../App.css';
import routeConfig from './routes'

/**
 * 图标列队
 */
import Svg from '../echarts/Svg';
import EchartsRadar from '../echarts/EchartsRadar';
import Dynamic from '../echarts/Dynamic';
import InventoryManage from '../echarts/InventoryManage'


export default  class RouteManagement extends Component {
  render() {
    return (
      <Router >
        <div className="App">
          {/* <Route path="/" exact component={InventoryManage}></Route> */}
          {routeConfig.map(({path, component}, index) => (
            <Route key={index}
             exact 
             path={path}
             component={component}
             />

          ))} 
           {/* <Route path="/echarts/Svg" exact component={Svg}></Route>
          <Route path="/echarts/EchartsRadar" exact component={EchartsRadar}></Route>
          <Route path="/echarts/Dynamic" exact component={Dynamic}></Route>
          <Route path="/echarts/InventoryManage" exact component={InventoryManage}></Route> */}
         
        </div>
      </Router>
    );
  }
}

