import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import MainView from '../views/MainView.vue'
import DetailView from '../views/DetailView.vue'
// import ReadView from '../views/ReadView.vue'
import ReviewView from '../views/ReviewView.vue'
import ProfileView from '../views/ProfileView.vue'
import NotFound404 from '../views/NotFound404.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/main',
    name: 'main',
    component: MainView,
  },
  {
    path: '/movies/',
    name: 'movie_list',
    component: () => import('../views/ReadView.vue')
  },
  {
    path: '/movies/:movie_id',
    name: 'movie_detail',
    component: DetailView,
  },
  {
    path: '/reviews/:review_id',
    name: 'review_detail',
    component: ReviewView,
  },
  {
    path: '/:userName',
    name: 'profile',
    component: ProfileView,
  },
  {
    path: '/not-found-404',
    name: 'NotFound404',
    component: NotFound404,
  },
  {
    path: '*',
    redirect: '/not-found-404'
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
