<template>
  <section class="title-section pt-5 pb-3">
    <div class="container text-center mt-5">
      <img class="col-lg-4 col-sm-7 col-10" src="@/assets/homepage/logo.svg" alt="logo">
      <h1 class="col-lg-0 mt-5">Каспийский Лотос</h1>
    </div>
    <div class="container mt-3 mt-md-5 text-center">
      <vue-typed-js
          :strings="['за новыми впечатлениями', 'на рыбалку!', 'за хорошим уловом!', 'для души', 'для настоящего отдыха']"
          :backSpeed="50"
          :shuffle="true"
          :showCursor="false"
          :loop="true"
          :backDelay="1000"
      >
        <h2 class="col-12 mb-5 text-center">Приезжайте к нам<br><span
            class="pink-text typing" style="min-height: 50px; display: block">за новыми впечатлениями</span></h2>
      </vue-typed-js>
      <booking-widget>
      </booking-widget>
<!--      <router-link tag="div" class="to-book col-lg-4 col-12 p-3 p-md-4 d-md-inline-block rose-button" to="/booking">-->
<!--        Забронировать-->
<!--      </router-link>-->
    </div>
  </section>
</template>

<script>
import BookingWidget from "../BookingWidget";
export default {
  name: "TitleSection",
  components: {BookingWidget}
}
</script>

<style scoped lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@200;300;400;500;600;700;800&display=swap');

.title-section {
  background: url("../../assets/homepage/background.png");
  background-size: cover;
  min-height: 100vh;
  border-radius: 0 0 50px 50px;
  box-shadow: 0 0 10px rgba(0, 0, 0, .8);

  h1 {
    mix-blend-mode: screen;
    font-family: "Montserrat", sans-serif;
    font-weight: 700;
    font-size: 64px;
    text-shadow: 0 0 44px #00B4FF;
    opacity: 80%;

    background: radial-gradient(rgba(0, 131, 186, 1), rgba(0, 180, 255, 1));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }

  img {
    mix-blend-mode: screen;
  }

  h2 {
    font-family: Montserrat, sans-serif;
    font-weight: 600;
    font-size: 38px;
    text-align: center;
    color: rgba(255, 255, 255, .8);
    mix-blend-mode: screen;

    .pink-text {
      color: rgba(255, 67, 153, .8);
    }
  }

  .to-book {
    font-family: Montserrat, sans-serif;
    font-weight: 600;
    font-size: 30px;
    color: #fff;
    line-height: 37px;
    text-decoration: none;
    background: rgba(255, 67, 153, 1);
    border-radius: 40px;
    box-shadow: 0 0 24px rgba(255, 67, 153, 0.9);
  }
}

@media screen and (max-width: 993px) {
  .title-section {
    h1 {
      font-size: 32px;
    }

    h2 {
      font-size: 28px;
    }

    .to-book{
      font-size: 26px;
    }

    p {
      font-size: 36px;
    }
  }
}
</style>
