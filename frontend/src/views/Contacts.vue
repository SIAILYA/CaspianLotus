<template>
  <div class="container header-pt">
    <h1 class="text-center">Контакты</h1>
    <div class="d-flex flex-md-row flex-column">
      <div class="col-md-6 col-12">
        <h2 class="mt-3">Звоните</h2>
        <h3>+7-912-345-67-89</h3>
        <h4>в любой день с 9 до 12</h4>
        <h2 class="mt-4">Пишите</h2>
        <h3>mail@caspianlotus.ru</h3>
        <h4>когда угодно</h4>
        <h2 class="mt-4">Наши соцсети</h2>
        <div class="mb-2">
          <img src="@/assets/contacts/vk.svg" alt="vk">
          <a href="#">@caspianlotus</a>
        </div>
        <div class="mb-5">
          <img src="@/assets/contacts/Instagram.svg" alt="Instagram">
          <a href="#">@caspianlotusru</a>
        </div>
      </div>
      <div class="map col-md-6 col-12 text-center">
        <h3>Каспийский Лотос на карте</h3>
        <div style="position:relative;overflow:hidden;"><a href="https://yandex.ru/maps/org/gostevoy_dom_lotos/233165853468/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:0;">Гостевой дом Лотос</a><a href="https://yandex.ru/maps/10946/astrakhan-oblast/category/resort/184106400/?utm_medium=mapframe&utm_source=maps" style="color:#eee;font-size:12px;position:absolute;top:14px;">Дом отдыха в Астраханской области</a><iframe src="https://yandex.ru/map-widget/v1/-/CCUuBTwwOD" width="560" height="400" style="position:relative;"></iframe></div>
      </div>
    </div>
    <h1 class="text-center mt-5">Обратная связь</h1>
    <h3 class="text-center">Заполните форму ниже и мы свяжемся с Вами в ближайшее время!</h3>
    <form class="text-center">
      <div class="d-flex flex-md-row flex-column justify-content-between text-left">
        <div class="col-md-3 col-sm-6 col-12">
          <h5 class="mt-2">Как к Вам обращаться</h5>
          <input type="text" class="w-100">
        </div>
        <div class="col-md-3 col-sm-6 col-12">
          <h5 class="mt-2">Телефон или почта</h5>
          <input type="text" class="w-100">
        </div>
        <div class="col-md-3 col-sm-6 col-12">
          <h5 class="mt-2">Когда с Вами связаться</h5>
          <input type="text" class="w-100" placeholder="Как можно скорее">
        </div>
      </div>
      <div class="d-flex text-left">
        <div class="col-12 mb-3">
          <h5 class="mt-2">Что вы хотите узнать?</h5>
          <input type="text" class="w-100" placeholder="Например: можно ли приехать с домашним животным (да, можно!)">
        </div>
      </div>
      <input type="submit" class="p-3 mx-auto mb-3 rose-button">
    </form>
  </div>
</template>

<script>
export default {
  name: "Contacts"
}
</script>

<style scoped lang="scss">
h1 {
  color: var(--blue-main);
}
h2 {
  color: var(--accent-rose);
  font-weight: 500;
  font-size: 20px;
}
h3 {
  font-size: 24px;
  font-weight: 500;
}
h4 {
  font-weight: 300;
  font-size: 16px;
}
h5 {
  font-weight: 500;
  font-size: 14px;
}
a {
  color: var(--blue-main);
  text-decoration-line: underline;
  font-weight: 500;
  font-size: 22px;
  line-height: 32px;
  margin-left: 10px;
}
iframe {
  border: none;
}
.map div {
  padding: 0;
  border-radius: 30px;
  box-shadow: 0 0 6px rgba(0, 0, 0, 0.7);
}
input[type="text"] {
  border: none;
  border-bottom: 1px solid #000000;
}
input[type="text"]:focus {
  outline:none;
  border: none;
  border-bottom: 1px solid #000000;
}
input[type="submit"] {
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
</style>
