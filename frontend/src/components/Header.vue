<template>
  <b-container>
    <b-navbar toggleable="lg" type="light" variant="light" class="header">
      <b-navbar-brand href="#" class="header-logo">
        <div class="d-flex flex-row">
          <b-img src="@/assets/lotos_logo.svg" />
          Каспийский<br>Лотос
        </div>
      </b-navbar-brand>
      <b-navbar-nav>
        <b-nav-item href="#" class="nav-item">О нас</b-nav-item>
        <b-nav-item href="#" class="nav-item">Фотоотчёты</b-nav-item>
        <b-nav-item href="#" class="nav-item">Досуг</b-nav-item>
        <b-nav-item href="#" class="nav-item">Рыбалка</b-nav-item>
        <b-nav-item href="#" class="nav-item">Отзывы</b-nav-item>
        <b-nav-item href="#" class="nav-item">Карта развития</b-nav-item>
        <b-nav-item href="#" class="nav-item">Контакты</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
  </b-container>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped lang="scss">
.header {
  background-color: inherit;

  .header-logo {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 500;
    font-size: 24px;
    line-height: 1.5;
    color: #0073A3;
  }

  .nav-item {
    font-family: Montserrat, sans-serif;
    font-style: normal;
    font-weight: 300;
    font-size: 18px;
    line-height: 22px;
    color: #272727;
  }
}
</style>
