<template>
  <div>
    <img src="@/assets/homepage/Vector.svg" class="shade w-100 position-relative" alt="">
    <section>
      <div class="container text-center">
        <h1>Место, где точно есть рыба</h1>
        <h2 class="mt-1">
          Каспийское море - одно из лучших мест для рыбалки в мире -
          в нем водится множество видов рыб в огромном количестве!
        </h2>
        <div class="container d-flex flex-lg-row flex-column">
          <img src="@/assets/homepage/man.png" class="col-lg-5 col-12" alt="man">
          <div class="p-and-button col-lg-7 col-12">
            <div class="text-left">
              <p>
                У нас водятся сом, сазан, жерех и еще десятки других видов рыб
              </p>
              <p>
                Помимо рыбалки мы так же организуем охоту на водоплавающую дичь и подводную охоту
              </p>
              <p>
                Для начинающих рыбаков предлагаем обучение и практические советы по рыбной ловле
              </p>
              <p>
                Наши лодки и катера оборудованы двигателями различной мощности
              </p>
            </div>
            <router-link tag="div" class="to-book col-lg-8 col-12 text-center p-4 d-md-inline-block mb-lg-4 mb-5" to >Забронировать</router-link>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
export default {
  name: "PlaceWithFish"
}
</script>

<style scoped lang="scss">
.shade {
  z-index: -1;
}
section {
  background: #032560;
  border-radius: 0 0 50px 50px;
  margin-top: -2%;
  color: #fff;
  font-family: "Montserrat", sans-serif;
  h1 {
    font-weight: 600;
    font-size: 36px;
  }
  h2 {
    font-weight: 500;
    font-size: 24px;
  }
  p {
    font-style: normal;
    font-weight: 500;
    font-size: 20px;
  }
  .p-and-button {
    margin: auto 0;
  }
  .to-book {
    font-family: Montserrat, sans-serif;
    font-weight: 600;
    font-size: 30px;
    color: #fff;
    text-decoration: none;
    background: rgba(255, 67, 153, 1);
    border-radius: 40px;
    box-shadow: 0 0 24px rgba(255, 67, 153, 0.9);
  }
}
</style>
