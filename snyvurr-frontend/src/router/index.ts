import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import axios from 'axios'
import { ref } from 'vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/profile',
      name: 'profile',
      component: () => import('../views/ProfileView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/social',
      name: 'social',
      component: () => import('../views/ConnectView.vue'),
      // meta: { requiresAuth: true },
    },
    {
      path: '/functions',
      name: 'utilities',
      component: () => import('../views/UtilsView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/functions/studytools',
      name: 'studytools',
      component: () => import('../views/functions/StudytoolsView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/functions/studytools/quiz',
      name: 'studyquiz',
      component: () => import('../views/functions/StudyQuizView.vue'),
      meta: { requiresAuth: true },
    },
    {
      path: '/privacy-policy',
      name: 'privacy-policy',
      component: () => import('../views/PrivacyPolicyView.vue'),
    },
    {
      path: '/logout',
      name: 'logout',
      component: () => import('../views/LogoutView.vue'),
      meta: { requiresAuth: true },
    }
  ]
})

// const apiURL = import.meta.env.VITE_API_URL
// const apiKey = import.meta.env.VITE_API_KEY
const apiKey = 'boobies';
const apiURL = 'http://127.0.0.1:5000';
const authenticated= ref(false);

router.beforeEach(async (to,from, next) => {
  if (to.matched.some((record) => record.meta.requiresAuth)) {
    try {
      const resp  = await axios.get(`${apiURL}/checkAuth`, {
        headers: {
          "X-API-KEY": apiKey,
        },
        withCredentials: true,
      })
      if (resp.data.authenticated) {
        console.log('authenticated')
        authenticated.value = true
        next()
      } else {
        authenticated.value = false
        next({ name: 'home' })
      }
    } catch (error) {
      console.error(error)
      next({ name: 'home' })
    }
  } else {
    next()
  }
})

export {router, authenticated}
