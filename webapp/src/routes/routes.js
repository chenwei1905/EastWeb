import { view as Login } from "../views/Login/index";
import HomeBack from "../views/HomeBack";
import Home from "../views/Home";
import Home1 from "../views/Home1";
import Grid from "../views/Grid";
import CardView from "../views/CardView"

import View from "../components/echarts/index";

const routeConfig = [
    { path: "/", component: View },

    { path: "/Login", component: Login },

    { path: "/Home", component: Home1 },
    { path: "/Grid", component: Grid  },
    { path: "/CardView", component: CardView  }

];

export default routeConfig;
