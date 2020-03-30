import { view as Login } from "../views/Login/index";
import HomeBack from "../views/HomeBack";
import Home from "../views/Home";
import Home1 from "../views/Home1";
import Grid from "../views/Grid";
import CardView from "../views/CardView"

import Knight from "../views/Knight";
import Board from "../views/Board";
import BoardView from "../views/BoardView";

import View from "../components/echarts/index";
import Game from "../views/Game";

import DustBinView from "../views/DustBinView"

const routeConfig = [
    { path: "/", component: View },

    { path: "/Login", component: Login },

    { path: "/Home", component: Home1 },
    { path: "/Grid", component: Grid  },
    { path: "/CardView", component: CardView  },
    { path: "/Knight", component: Knight  },
    { path: "/Board", component: Board  },
    { path: "/BoardView", component: BoardView  },
    { path: "/Game", component: Game  },

    { path: "/DustBin", component: DustBinView },


];

export default routeConfig;
