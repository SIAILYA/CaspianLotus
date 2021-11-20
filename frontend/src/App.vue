<template>
  <div id="app">
    <div id="nav" :class="navBack ? 'nav-background' : ''" class="navigation">
      <b-container class="d-flex justify-content-center">
        <div class="links d-flex">
          <router-link active-class="current-link" class="navigation-link mt-auto mb-auto" exact to="/">О нас
          </router-link>
          <router-link active-class="current-link" class="navigation-link mt-auto mb-auto" exact to="/booking">
            Забронировать
          </router-link>
          <router-link active-class="current-link" class="navigation-link mt-auto mb-auto" exact to="/#attraction">Досуг
          </router-link>
          <router-link active-class="current-link" class="navigation-link mt-auto mb-auto" exact to="/#photos">
            Фотографии
          </router-link>
          <router-link active-class="current-link" class="navigation-link mt-auto mb-auto mr-0" exact to="/contacts">
            Контакты
          </router-link>
        </div>
        <div :class="showPhone ? 'phone-show'  : 'phone-hide'"
             class="text-nowrap ml-0 ml-xl-5 d-none d-xl-block overflow-hidden">
          <a class="d-none phone-number text-white d-xl-block" href="tel:89535823354">
            +7-912-345-67-89
          </a>
          <span class="decor-underline text-white">
              Обратный звонок
            </span>
        </div>
        <button v-b-toggle.sidebar-1 class="mobile-sidebar-open d-block d-sm-none"><span class="material-icons-round">menu</span>
        </button>
      </b-container>
    </div>
    <router-view/>
  </div>
</template>


<script>

export default {
  data() {
    return {
      scrollTop: 0
    }
  },
  computed: {
    navBack() {
      return this.$route.path !== "/" || this.scrollTop > 0
    },
    showPhone() {
      return this.scrollTop > 0
    }
  },
  methods: {
    scroll() {
      this.scrollTop = window.pageYOffset || document.documentElement.scrollTop
    },
  },
  mounted() {
    window.addEventListener("scroll", this.scroll)
  }
}
</script>

<style lang="scss">
@import "main";

.navigation {
  position: fixed;
  width: 100%;
  padding-top: 20px;
  padding-bottom: 20px;
  z-index: 5;
  transition: all .3s ease-in-out;

  div {
    max-height: 50px;
    overflow-y: hidden;
  }
}

.navigation-link {
  margin-right: 16px;
  color: white;
  font-size: 24px;
  text-shadow: 0 0 5px rgba(0, 0, 0, 0.08);
  transition: all .3s ease-in-out;
}

.navigation-link:hover {
  text-decoration: none;
  transform: translateY(5px);
  color: var(--blue-secondary);
}

@media screen and (max-width: 1000px) {
  .navigation-link {
    font-size: 20px;
    white-space: nowrap;
  }
}

@media screen and (max-width: 635px) {
  .links {
    overflow-x: auto;
  }

  .navigation-link {
    font-size: 16px;
    white-space: nowrap;
  }
}

.current-link {
  color: var(--accent-rose);
  //text-shadow: 0 0 5px rgba(255, 255, 255, 0.5);
}

.mobile-sidebar-open {
  background: none;
  border: none;
  margin-top: 8px;
  padding: 0 0 0 10px;

  span {
    font-size: 32px;
    color: white;
  }
}

.nav-background {
  border-radius: 0 0 15px 15px;
  background: rgba(3, 37, 96, 0.8);
  box-shadow: 0 8px 32px 0 rgba(31, 55, 160, 0.25);
  //backdrop-filter: blur( 5px );
  //-webkit-backdrop-filter: blur( 5px );
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-top: none;
}

.phone-show {
  width: 200px;
  height: 45px;
  transition: all .3s ease;
}

.phone-hide {
  width: 0;
  height: 0;
  transition: all .3s ease;
}

.phone-number {
  font-size: 22px;
  line-height: 1;
}
</style>
