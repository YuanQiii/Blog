import Vue from 'vue'
import VueRouter from 'vue-router'
const Hello = () => import('../views/Hello.vue')
const Home = () => import('../views/Home.vue')
const Article = () => import('../views/Article.vue')
const About = () => import('../views/About.vue')
const Archives = () => import('../views/Archives.vue')
const Tag = () => import('../views/Tag.vue')
const Comment = () => import('../views/Comment.vue')

Vue.use(VueRouter)

const routes = [{
    path: '',
    redirect: '/home',
  },
  {
    path: '/home',
    component: Home
  },
  {
    path: '/content/:id',
    component: Article,
  },
  {
    path: '/about',
    component: About
  },
  {
    path: '/archives',
    component: Archives
  },
  {
    path: '/tag',
    component: Tag
  },{
    path: '/comment',
    component: Comment
  },
  {
    path: '/hello',
    name: 'hello',
    component: Hello
  }
]

const scrollBehavior = function(to, from, savePosition) {
  if(to.hash){
    return {
      selector: to.hash
    }
  }
}

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
  scrollBehavior
})

export default router