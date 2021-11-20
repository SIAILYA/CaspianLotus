<template>
  <div class="container text-center mt-5">
    <h1>
      Досуг на любой вкус
    </h1>
    <h3>
      Главное, за чем приезжают на нашу базу - это рыбалка.<br>Но помимо этого у нас множество других активностей!
    </h3>
    <div class="d-flex flex-row row mt-2">
      <img class="col-6" src="@/assets/homepage/lotuses.png" alt="lotuses">
      <div class="col-6 text-left">
        <h2>
          Экскурсии на лотосовые поля
        </h2>
        <p>
          Это одно из самых потрясающих зрелищ, которое стоит увидеть зотя бы раз в жизни. Период цветения длится всего полтора месяца и именно в это время на лотосовых полях царит нереальная красота и гармония!
        </p>
      </div>
    </div>
    <div class="d-flex flex-row-reverse row mt-2">
      <img class="col-6" src="@/assets/homepage/bathhouse.png" alt="lotuses">
      <div class="col-6 text-left">
        <h2>
          Настоящая русская баня
        </h2>
        <p>
          Когда в последний раз Вы были в русской бане? На территории базы оборудована русская баня, в которой можно попариться на дровах и насладиться приятной атмосферой        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LeisureForAll"
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
  .row div {
    margin: auto 0;
  }
}
</style>
