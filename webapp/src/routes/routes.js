import  {view as Login} from '../views/Login/index';
import Home from '../views/Home'



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