<template>
  <div>
    <img src="@/assets/homepage/Vector.svg" class="shade w-100 position-relative" alt="">
    <section>
      <div class="container text-center">
        <h1>Планируете заранее?</h1>
        <h2 class="mt-1">
          Каспийский Лотос постоянно растет и расширяется! Если планируете поездку на следующий сезон - посмотрите, что мы уже сейчас готовим для Вас и бронируйте места на нужное время!
        </h2>
        <div class="container">
          <div class="d-flex flex-row mt-5">
            <div class="col-2 text-center">
              <div class="circle mx-auto"></div>
              <h4 class="mt-2 mx-auto text-center">лето 2022</h4>
              <div class="vertical-shade mt-4 mx-auto"></div>
            </div>
            <div class="col-md-5 col-10 my-auto text-left">
              <p class="">
                Построим детскую площадку и орагнизуем инфраструктуру для сап-туров в Каспийском море
              </p>
            </div>
            <img class="col-5 my-auto d-md-block d-none" src="@/assets/homepage/surfing.png" alt="surfing">
          </div>
          <div class="d-flex flex-row mt-5">
            <div class="col-2 text-center">
              <div class="circle mx-auto"></div>
              <h4 class="mt-2">осень 2022</h4>
              <div class="vertical-shade mt-4 mx-auto"></div>
            </div>
            <div class="col-md-5 col-10 my-auto text-left">
              <p class="">
                Оборудуем небольшую столовую на 20 человек. В разгар сезона в столовой будут подаваться блюда из свежей рыбы и дичи
              </p>
            </div>
            <img class="col-5 my-auto d-md-block d-none" src="@/assets/homepage/food.png" alt="food">
          </div>
        </div>
        <router-link tag="div" class="to-book col-md-7 col-sm-10 text-center d-md-inline-block mx-auto p-4 mt-4 mb-4" to >Забронировать нужные даты</router-link>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "Planing"
}
</script>

<style scoped lang="scss">
.shade {
  z-index: -1;
}
section {
  background: var(--blue-main);
  border-radius: 0 0 50px 50px;
  margin-top: -2%;
  color: #fff;
  font-family: "Montserrat", sans-serif;
  padding-bottom: 5px;
h1 {
  font-weight: 600;
  font-size: 36px;
  line-height: 54px;
}
h2 {
  font-weight: 500;
  font-size: 24px;
  line-height: 34px;
}
p {
  font-style: normal;
  font-weight: 500;
  font-size: 20px;
  line-height: 32px;
}
.p-and-button {
  margin: auto 0;
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
.circle {
  height: 40px;
  width: 40px;
  border-radius: 20px;
  background: var(--accent-rose);
}
.vertical-shade {
  width: 2px;
  height: 250px;
  background: #fff;
}
h4 {
  font-size: 14px;
  line-height: 24px;
}
</style>
