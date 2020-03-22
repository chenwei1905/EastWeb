import  {view as Login} from '../views/Login/index';
import HomeBack from '../views/HomeBack'
import Home from '../views/Home';
import Home1 from '../views/Home1';


import View from '../components/echarts/index'



const routeConfig = [
  { path: '/',
    component: View,
  },

  { path: '/Login',
    component: Login,
  },

  { path: '/Home',
    component: Home1,
  },

]

export default routeConfig; 