import Vue from 'vue'
import VueRouter from 'vue-router'
import Leisure from "@/views/Leisure";
import About from "@/views/About";
import PhotoReports from "@/views/PhotoReports";
import Fishing from "@/views/Fishing";
import Roadmap from "@/views/Roadmap";
import Contacts from "@/views/Contacts";
import Reviews from "@/views/Reviews";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'About',
    component: About
  },
  {
    path: '/photo_reports',
    name: 'PhotoReports',
    component: PhotoReports
  },
  {
    path: '/leisure',
    name: 'Leisure',
    component: Leisure
  },
  {
    path: '/fishing',
    name: 'Fishing',
    component: Fishing
  },
  {
    path: '/reviews',
    name: 'Reviews',
    component: Reviews
  },
  {
    path: '/roadmap',
    name: 'Roadmap',
    component: Roadmap
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
