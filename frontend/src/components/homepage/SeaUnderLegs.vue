<template>
  <div class="container text-center" id="sea_under_legs">
    <h1 class="mt-5">Море под ногами</h1>
    <h2 class="text-center">
      База расположена на самом берегу Каспийского моря недалеко от города Астрахань и готова предложить своим посетителям уникальный отдых!
    </h2>
    <div class="container d-lg-flex d-block flex-lg-row flex-column-reverse">
      <div class="picture-set col-lg-5 col-12 position-relative">
        <img class="w-100" id="pic_1" src="@/assets/homepage/boards.png" alt="">
        <img class="w-100" id="pic_2" src="@/assets/homepage/sea.png" alt="">
        <img class="w-100" id="pic_3" src="@/assets/homepage/lotus.png" alt="">
      </div>
      <div class="p-series col-lg-7 col-12 text-left my-lg-auto my-0 mt-sm-0 mt-5">
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
    color: #032560;
  }

  h2 {
    font-size: 24px;
  }

  .p-series {
    margin: 15% 0;
    p {
      font-size: 22px;
    }
  }

  .picture-set {
    aspect-ratio: .91;
    img {
      position: absolute;
      left: 0;
    }
    #pic_1 {
      transform: rotate(3deg);
      transition: all .3s ease;
    }
    #pic_1:hover {
      transform: rotate(-7deg) scale(1.05);
    }
    #pic_2 {
      transform: rotate(15deg);
      transition: all .3s ease;
      top: 70px;
    }
    #pic_2:hover {
      transform: rotate(-7deg) scale(1.05);
    }
    #pic_3 {
      transform: rotate(3deg);
      transition: all .3s ease;
      top: 140px;
    }
    #pic_3:hover {
      transform: rotate(10deg) scale(1.05);
    }
  }
}

.houses-photo-2 {
}

.houses-photo-2:hover {
}

@media screen and (max-width: 993px) {
  .p-series {
    margin: 0;
  }
  .picture-set {
  }
}
@media screen and (max-width: 768px) {
  .picture-set {
    aspect-ratio: 0.95 !important;
  }
}
@media screen and (max-width: 380px) {
  .picture-set {
    aspect-ratio: 1.5;
  }
}
</style>
