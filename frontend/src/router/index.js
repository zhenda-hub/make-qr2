import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import QRGeneratorView from '../views/QRGeneratorView.vue'
import PageManagerView from '../views/PageManagerView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/qr-generator',
      name: 'qr-generator',
      component: QRGeneratorView
    },
    {
      path: '/page-manager',
      name: 'page-manager',
      component: PageManagerView
    }
  ]
})

export default router
