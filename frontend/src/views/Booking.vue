<template>
  <b-container class="header-pt booking text-center">
    <b-modal id="modal-1" title="Спасибо!" no-close-on-esc no-close-on-backdrop hide-header-close ok-only>
      <p class="my-2 text-center">
        //После редиректа на платежную систему и обратно//
        <br>
        <br>
        Ваша бронь записана! В скором времени мы с Вами свяжемся для уточнения деталей!
      </p>
      <template #modal-footer="{ }">
        <b-button size="md" variant="primary" @click="$router.push('/')">
          OK
        </b-button>
      </template>
    </b-modal>
    <b-modal id="modal-2" title="Ошибка!" no-close-on-esc no-close-on-backdrop hide-header-close ok-only>
      <p class="my-4">
        Во время обработки запроса произошла ошибка :(
        <br>
        <br>
        Информация об ошибке автоматически отправлена, мы уже занимаемся решением проблемы! Извините за неудобства...
      </p>
      <template #modal-footer="{ }">
        <b-button size="md" variant="primary" @click="$router.push('/')">
          OK
        </b-button>
      </template>
    </b-modal>
    <h1>
      Бронирование домиков
    </h1>
    <b-row class="justify-content-center">
      <div class="col-12 col-md-10 col-xl-8">
        <div class="mt-4 booking-card mb-4">
          <h4>Бронируйте заранее и получайте скидку!</h4>
          <b-row class="mt-4">
            <div class="col-12 col-md-6 d-flex">
              <span class="text-nowrap mr-2 my-auto">Количество гостей</span>
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
        </div>
      </div>
      <div class="col-12">
        <b-spinner v-if="loadVariants" type="grow" class="mt-3"></b-spinner>
      </div>
      <div class="col-12 col-md-10 col-xl-8">
        <div v-if="!loadVariants && variantsInfo" class="variants">
          <div class="row">
            <div class="col-12 col-md-5 mb-3 mb-md-0">
              <h4>Стандарт</h4>
              <span>Номер с двумя спальными кроватями в домике из двух номеров</span>
            </div>
            <div v-if="variantsInfo.standard > 0" class="col-6 col-md-3">
              <h5>Доступно</h5>
              <span class="available">{{ variantsInfo.standard }}</span>
            </div>
            <div v-if="variantsInfo.standard > 0" class="col-6 col-md-4">
              <h5>Количество бронирования</h5>
              <input @input.prevent="inputBookCount"
                     data-type="standard"
                     type="number"
                     class="form-control"
                     :max="variantsInfo.standard"
                     :value="toBookStandard"
              >
            </div>
            <div v-else class="col-12 col-md-7 d-flex">
              <h4 class="m-auto">К сожалению, на выбранные даты нет свободных номеров</h4>
            </div>
          </div>
          <hr>
          <div class="row">
            <div class="col-12 col-md-5 mb-3 mb-md-0">
              <h4>Люкс</h4>
              <span>Целый домик в Вашем распоряжении! Два спальных места в одном домике</span>
            </div>
            <div v-if="variantsInfo.lux > 0" class="col-6 col-md-3">
              <h5>Доступно</h5>
              <span class="available">{{ variantsInfo.lux }}</span>
            </div>
            <div v-if="variantsInfo.lux > 0" class="col-6 col-md-4">
              <h5>Количество бронирования</h5>
              <input @input.prevent="inputBookCount"
                     data-type="lux"
                     type="number"
                     class="form-control"
                     :max="variantsInfo.lux"
                     :value="toBookLux"
              >
            </div>
            <div v-else class="col-12 col-md-7 d-flex">
              <h4 class="m-auto">К сожалению, на выбранные даты нет свободных номеров</h4>
            </div>
          </div>
        </div>
      </div>
    </b-row>
    <button class="rose-button mt-4" v-if="!loadVariants && variantsInfo"
            :disabled="(toBookLux === '0' && toBookStandard === '0') || sending" @click="confirmBooking">
      Дальше
    </button>
    <br>
    <b-spinner v-if="sending" type="grow" class="mt-3"></b-spinner>
    <div class="mt-3" v-if="(toBookLux === '0' && toBookStandard === '0') && variantsInfo && !loadVariants ">Выберете
      количество номеров для бронирования!
    </div>
  </b-container>
</template>

<script>
import {BACKEND} from "../backend.config";
import axios from "axios";

export default {
  name: "Booking",
  data() {
    return {
      count: 1,
      dateStart: this.getTomorrow(),
      dateEnd: null,
      priceStandard: null,
      loadVariants: null,
      variantsInfo: null,
      toBookLux: "0",
      toBookStandard: "0",
      sending: false
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
      console.log(this.count, this.dateStart, this.dateEnd)

      if (this.count && this.dateStart && this.dateEnd) {
        this.loadVariants = true

        axios.get(BACKEND + "/api/get_prices")
            .then(r => {
              this.priceStandard = r.data[0].count
              return axios.post(BACKEND + "/api/check_booking", {
                count: this.count,
                dateStart: this.dateStart,
                dateEnd: this.dateEnd
              })
            })
            .then(r => {
              this.loadVariants = false
              this.variantsInfo = r.data
            }).
            catch(() => {
              this.$bvModal.show("modal-2")
        })
      }
    },
    inputBookCount(e) {
      const val = parseInt(e.target.value)
      const max = parseInt(e.target.max)
      console.log(val, max)
      console.log(this.toBookLux, this.toBookStandard)
      if (e.target.dataset.type === "standard") {
        this.toBookStandard = (isNaN(val) ? 0 : val < 0 ? 0 : val > max ? max : val) + ""
        e.target.value = this.toBookStandard
      } else {
        this.toBookLux = (isNaN(val) ? 0 : val < 0 ? 0 : val > max ? max : val) + ""
        e.target.value = this.toBookLux
      }
      console.log(this.toBookLux, this.toBookStandard)
    },
    confirmBooking() {
      this.sending = true

      axios.post(BACKEND + "/api/confirm_booking", {
        "count": this.count,
        "dateStart": this.dateStart,
        "dateEnd": this.dateEnd,
        "lux": this.toBookLux,
        "standard": this.toBookStandard
      }).then(() => {
        this.$bvModal.show("modal-1")
        this.sending = false
      }).catch(() => {
        this.$bvModal.show("modal-2")
        this.sending = false
      })
    }
  },
  mounted() {
    if (Object.keys(this.$route.query).length > 1) {
      this.count = this.$route.query.co || null
      this.dateEnd = this.$route.query.en || null
      this.dateStart = this.$route.query.st || this.getTomorrow()
      this.onChangeInfo()
    }
  }
}
</script>

<style lang="scss" scoped>

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

h1, h2, h4, h3, h5 {
  color: var(--blue-main)
}

.show-variants {
  height: auto !important;
}

.variants {
  background: white;
  box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);
  border-radius: 35px;
  padding: 16px 24px;
}

.available {
  font-size: 24px;
}

.booking{
  min-height: 100vh;
}
</style>
