import  {view as Login} from '../views/Login/index';
import HomeBack from '../views/HomeBack'
import Home from '../views/Home';
import Home1 from '../views/Home1';



const routeConfig = [
  { path: '/',
    component: Login,
  },

  { path: '/Login',
    component: Login,
  },

  { path: '/Home',
    component: Home,
  },

]

export default routeConfig; 