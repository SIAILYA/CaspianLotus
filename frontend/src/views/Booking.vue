<template>
  <b-container class="header-pt text-center">
    <h1>
      Бронирование домиков
    </h1>
    <b-row class="justify-content-center">
      <div class="col-12 col-md-10 col-xl-8">
        <div class="mt-4 booking-card">
          <h4>Бронируйте заранее и получайте скидку!</h4>
          <b-row class="mt-4">
            <div class="col-12 col-md-6 d-flex">
              <span class="text-nowrap mr-2 my-auto">Количество домиков</span>
              <input v-model="count" class="form-control w-50 mx-md-auto ml-auto my-auto" type="number"
                     @input="onChangeInfo">
            </div>
            <div class="col-12 col-md-6 d-flex flex-column mt-3 mt-md-0">
              <div class="d-flex">
                <span class="text-nowrap mr-2 my-auto">Дата заезда</span>
                <input v-model="dateStart" class="form-control w-50 ml-auto ml-0 my-auto" type="date"
                       @input="onChangeInfo">
              </div>
              <div class="d-flex mt-3">
                <span class="text-nowrap mr-2 my-auto">Дата выезда</span>
                <input v-model="dateEnd" :min="dateStart" class="form-control w-50 ml-auto ml-0 my-auto"
                       type="date" @input="onChangeInfo">
              </div>
            </div>
          </b-row>

          <div :class="price ? 'show-price' : ''" class="result mt-3" style="height: 0">
            Стоимость бронирования: {{}}
          </div>
        </div>

      </div>
    </b-row>
    <button class="rose-button mt-4">Перейти к оплате</button>
    <section class="mt-5 houses-info">
      <h2>Информация о домиках</h2>
      <b-row class="justify-content-center">
        <div class="col-12 col-ld-10">
          <b-row>
            <div class="col-12 col-md-5">
              <img alt="" class="w-100" src="@/assets/houses-1.jpeg">
            </div>
            <div class="col-12 col-md-7">

            </div>
          </b-row>
        </div>
      </b-row>
    </section>
  </b-container>
</template>

<script>
export default {
  name: "Booking",
  data() {
    return {
      count: 1,
      dateStart: this.getTomorrow(),
      dateEnd: null,
      price: null
    }
  },
  methods: {
    getTomorrow() {
      var currentDate = new Date(new Date().getTime() + 24 * 60 * 60 * 1000);
      var day = currentDate.getDate()
      var month = currentDate.getMonth() + 1
      var year = currentDate.getFullYear()

      return `${year}-${month}-${day}`
    },
    onChangeInfo() {
      if (this.count && this.dateStart && this.dateEnd) {
        // get price
      }
    }
  },
}
</script>

<style scoped>

.booking-card {
  background: white;
  box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);
  border-radius: 35px;
  padding: 16px 24px;
}

.result {
  font-size: 24px;
  font-weight: 500;
  overflow: hidden;
  transition: all .3s ease;
}

.show-price {
  height: 32px !important;
}

h1, h2, h4 {
  color: var(--blue-main)
}
</style>
