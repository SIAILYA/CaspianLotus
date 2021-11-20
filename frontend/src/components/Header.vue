<template>
  <header class="container">
    <div class="d-flex flex-row justify-content-between">
      <!-- logo -->
      <div class="logo d-flex" onclick="document.location.href = '/'">
        <img src="@/assets/Logo.svg">
        <p>Каспийский<br>Лотос</p>
      </div>
      <!-- contacts -->
      <div class="contacts d-flex flex-row">
        <img src="@/assets/header/Vk.svg" onclick="document.location.href = '#'">
        <img src="@/assets/header/Instagram.svg" onclick="document.location.href = '#'">
        <div class="text-center">
          <p>+7-912-345-67-89</p>
          <a href="#">Обратный звонок</a>
        </div>
      </div>
    </div>
    <!-- nav-menu -->
    <div class="nav-menu">
      <ul class="d-flex flex-row justify-content-around">
        <li>
          <a href="/">О нас</a>
        </li>
        <li>
          <a href="/booking">Бронирование</a>
        </li>
        <li>
          <a href="/contacts">Контакты</a>
        </li>
      </ul>
    </div>
  </header>
</template>

<script>
export default {
  name: "Header"
}
</script>

<style scoped lang="scss">
header {
  padding-top: 15px;
}

.logo {
  cursor: pointer;

  p {
    margin: auto 5px;
    font-family: "Montserrat", sans-serif;
    font-weight: 500;
    font-size: 26px;
    color: #0073A3;
    line-height: 1;
    letter-spacing: 2px;
  }
}

.contacts {
  padding: 20px 0;
  p {
    margin: 0;
    font-weight: 300;
    font-size: 20px;
  }
  a {
    font-weight: 200;
    font-size: 16px;
    text-decoration-line: underline;
    color: #0073A3;
    transition: 0.3s;
  }
  a:hover {
    color: inherit;
  }
  img {
    margin: 0 5px;
    cursor: pointer;
  }
}

.nav-menu {
  margin-top: 10px;
  ul {
    li {
      list-style: none;
      float: left;
      text-align: center;

      a {
        font-size: 22px;
        text-decoration: none;
        color: #272727;
        transition: 0.2s;
      }
      a:hover {
        color: #ff4399;
      }
    }
  }
}
</style>
