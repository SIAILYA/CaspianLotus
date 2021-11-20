<template>
  <div class="container text-center">
    <h1 class="mt-5">Море под ногами</h1>
    <h2 class="text-center">
      База расположена на самом берегу Каспийского моря недалеко от города Астрахань и готова предложить своим посетителям уникальный отдых!
    </h2>
    <div class="container d-flex flex-row">
      <div class="picture-set col-5 position-relative">
        <img class="w-100" id="pic_1" src="@/assets/homepage/boards.png" alt="">
        <img class="w-100" id="pic_2" src="@/assets/homepage/sea.png" alt="">
        <img class="w-100" id="pic_3" src="@/assets/homepage/lotus.png" alt="">
      </div>
      <div class="p-series col-7 text-left">
        <p>
          Собственный выход к воде прямо на базе - не нужно далеко идти
        </p>
        <p>
          Аренда лодок и катеров разной можности - от прогулки до ловли рыбы в открытом море
        </p>
        <p>
          Природа, тишина и чистый воздух вокруг базы
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "SeaUnderLegs"
}
</script>

<style scoped lang="scss">
div {
  font-family: Montserrat, sans-serif;
  font-weight: 500;
  color: #151515;
  line-height: 1.1;
  h1 {
    font-weight: 600;
    font-size: 40px;
    line-height: 54px;
    color: #032560;
  }

  h2 {
    font-size: 24px;
  }

  .p-series {
    margin: 160px 0;
    p {
      font-size: 22px;
    }
  }

  .picture-set {
    img {
      position: absolute;
      left: 0;
    }
    #pic_1 {
    }
    #pic_2 {
      top: 70px;
    }
    #pic_3 {
      top: 140px;
    }
  }
}
</style>
