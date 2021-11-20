<template>
  <div class="container text-center mt-5">
    <h1>
      Фотогалерея
    </h1>
    <h3>
      Лучше один раз увидеть, чем сто раз услышать! Смотрите<br>свежие фотографии с нашей базы
    </h3>
    <div class="images d-flex flex-md-row flex-column mt-5">
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/bathhouse1.png" alt="bathhouse1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/houses1.png" alt="houses1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/plane1.png" alt="plane1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/houses2.png" alt="houses2">
      </div>
    </div>
    <div class="images d-flex flex-md-row flex-column mb-5">
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/bathhouse1.png" alt="bathhouse1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/houses1.png" alt="houses1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/plane1.png" alt="plane1">
      </div>
      <div class="col-md-3 col-12">
        <img src="@/assets/homepage/houses2.png" alt="houses2">
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Gallery"
}
</script>

<style scoped lang="scss">
div {
  font-family: Montserrat, sans-serif;
  color: #151515;
  font-weight: 500;
  h1 {
    font-weight: 600;
    font-size: 40px;
    line-height: 54px;
    color: #032560;
  }
  h3 {
    font-size: 24px;
    line-height: 34px;
  }
  h2 {
    font-weight: 600;
    font-size: 24px;
  }
  p {
    font-size: 22px;
  }
}
.images {
  img {
    width: 100%;
  }
}
</style>
