
/**
 * 添加组件页面
 */
import Login from '../views/Login'
import App from '../App'
const routeConfig = [
    { path: '/',
      
      component: App,
      childRoutes: [
        // { path: 'about', component: About },
        // { path: 'inbox',
        //   component: Inbox,
        //   childRoutes: [
        //     { path: '/messages/:id', component: Message },
        //     { path: 'messages/:id',
        //       onEnter: function (nextState, replaceState) {
        //         replaceState(null, '/messages/' + nextState.params.id)
        //       }
        //     }
        //   ]
        // }
      ]
    }
  ]
  
 

  export default routeConfig;