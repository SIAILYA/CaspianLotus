<template>
  <div class="booking-widget">
    <h3 class="font-weight-bold">Забронируйте номер!</h3>
    <div class="row justify-content-center mt-3">
      <div class="col-6 arrive col-md-3">
        <span>Заехать</span>
        <input ref="dateStart" :max="dateEnd" v-model="dateStart" type="date" class="form-control">
      </div>
      <div class="col-6 depart col-md-3">
        <span>Выехать</span>
        <input ref="dateEnd" :min="dateStart" v-model="dateEnd" type="date" class="form-control">
      </div>
      <div class="col-8 col-md-3 mt-3 mt-md-0">
        <span>Количество гостей</span>
        <b-form-select ref="count" v-model="count"
                       :options="['1 гость', '2 гостя', '3 гостя', '4 гостя', '5 гостей', '6 гостей', '7 гостей', '8 гостей', '9 гостей']"></b-form-select>
      </div>
      <div class="col-12 col-md-3 mt-3 mt-md-0 d-flex">
        <button @click="goToBooking" class="rose-button submit mt-auto mx-auto">Бронировать!</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "BookingWidget",
  data() {
    return {
      dateStart: this.getTomorrow(),
      dateEnd: null,
      count: "1 гость"
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
    goToBooking() {
      if (this.count) {
        if (this.dateStart) {
          if (this.dateEnd) {
            this.$router.push("/booking?st=" + this.dateStart + "&en=" + this.dateEnd + "&co=" + parseInt(this.count))
          } else {
            this.$refs.dateEnd.focus()
          }
        } else {
          this.$refs.dateStart.focus()
        }
      } else {
        this.$refs.count.focus()
      }
    }
  },
}
</script>

<style scoped lang="scss">
.booking-widget {
  background: white;
  box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);
  border-radius: 35px;
  padding: 20px;

  span {
    font-size: 18px;
    font-weight: 300;
  }
}

.submit {
  padding: 12px 20px;
  font-size: 20px;
  line-height: 1;
}

@media screen and (max-width: 768px) {
  .arrive {
    padding-right: .25rem;
  }

  .depart {
    padding-left: .25rem;
  }
}

@media screen and (max-width: 992px) and (min-width: 768px) {
  .booking-widget {
    span {
      font-size: 14px;
    }
  }
  .submit{
    font-size: 16px;
  }

}

h3 {
  color: var(--blue-main)
}
</style>