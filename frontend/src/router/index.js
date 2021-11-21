import Vue from 'vue'
import VueRouter from 'vue-router'
import Main from "@/views/Main";
import Contacts from "@/views/Contacts";
import Booking from "@/views/Booking";
import Vr from "../views/Vr";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'About',
    component: Main
  },
  {
    path: '/booking',
    name: 'Booking',
    component: Booking
  },
  {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  },
  {
    path: '/vr',
    name: 'Vr',
    component: Vr
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
