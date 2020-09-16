import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Planet from '../views/Planet.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/planet/:id',
    name: 'Planet',
    component:  Planet
  }
]

const router = new VueRouter({
  routes
})

export default router
