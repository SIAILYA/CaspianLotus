<template>
  <section>
    <div class="container text-center p-4 d-md-flex flex-md-row flex-column">
      <div class="col-md-4 col-12 row text-md-left text-center mb-md-0 mb-3 ">
        <img class="col-5" src="@/assets/footer/logo.svg" alt="logo">
        <h1 class="col-7 my-auto">Каспийский Лотос</h1>
      </div>
      <div class="col-md-4 col-12 text-md-left text-center my-auto">
        <ul>
          <li>
            <router-link class="footer-link" to>О базе отдыха</router-link>
          </li>
          <li>
            <router-link class="footer-link" to>Досуг</router-link>
          </li>
          <li>
            <router-link class="footer-link" to>Рыбалка</router-link>
          </li>
          <li>
            <router-link class="footer-link" to>Отзывы</router-link>
          </li>
          <li>
            <router-link class="footer-link" to>Фотогалерея</router-link>
          </li>
        </ul>
      </div>
      <div class="col-md-4 col-12 text-md-left text-center mt-md-0 mt-4">
        <img class="pr-2" src="@/assets/footer/Vk.svg" alt="Vk">
        <img src="@/assets/footer/Instagram.svg" alt="Instagram">
        <h2 class="mt-2">
          +7-912-345-67-89
        </h2>
        <h3>
          По будням с 9 до 20
        </h3>
        <h2 class="mt-3">
          mail@caspainlotus.ru
        </h2>
        <h3>
          В любое время
        </h3>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: "Footer"
}
</script>

<style scoped lang="scss">
section {
  background: #032560;
  border-radius: 35px 35px 0 0;
  color: #fff;
  h1 {
    font-weight: 600;
    font-size: 24px;
  }
  h2 {
    font-weight: 600;
    font-size: 20px;
  }
  h3 {
    font-size: 14px;
  }
  ul {
    padding: 0;
    li {
    list-style: none;
  }
  }
  .footer-link {
    color: inherit;
    font-weight: 600;
    font-size: 18px;
  }
  .footer-link:hover {
    text-decoration: none;
  }
}
</style>
