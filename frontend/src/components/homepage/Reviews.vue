<template>
  <div class="container text-center mt-5" id="reviews">
    <h1>
      Отзывы
    </h1>
    <h3>
      Наши гости рассказывают почему любят Каспийский Лотос и делятся своими впечатлениями
    </h3>
    <div v-if="!loading" class="d-flex flex-lg-row flex-column mt-4 justify-content-between">
      <div class="col-lg-4 col-12 mb-3" v-for="review in reviews" :key="review._id">
        <div class="review-card">
          <div class="d-flex">
            <img :src="'https://icotar.com/initials/' + review.name + '?fg=e53b89&bg=ffffff'" width="55" height="55" alt="reviewer">
            <div class="user-data my-auto flex-column text-left ml-2">
              <h4>
                {{ review.name }}
              </h4>
              <h5>
                {{ review.date || 'Октябрь 2021' }}
              </h5>
            </div>
          </div>
          <p class="row text-left pt-3 pl-3 pr-3">
            {{
              review.review
            }}
          </p>
          <div class="text-right" v-if="review.source_name">
            <h6>
              <a :href="review.source_link">
                Отзыв с {{review.source_name}}
              </a>
            </h6>
          </div>
        </div>
      </div>
    </div>
    <div v-else class="text-center my-3">
      <b-spinner type="grow"></b-spinner>
    </div>
    <router-link tag="div" class="more-reviews mt-4" to="/">
      Больше отзывов
    </router-link>
    <div class="d-flex flex-md-row flex-column-reverse">
      <div class="p-4 mt-4 col-md-7 col-12 text-center">
        <div class="share my-auto p-3">
          <h1>
            Поделитесь своей поездкой!
          </h1>
          <p>
            Уже были в Каспийском Лотосе?<br>Расскажите другим, как провели время и поделитесь фотографиями, а мы
            подарим Вам скидку на следующее бронирование!
          </p>
          <div class="to-book col-md-8 col-12 text-center p-3 d-inline-block rose-button">Рассказать</div>
        </div>
      </div>
      <div class="images col-md-5 col-12 position-relative p-2 my-auto">
        <img class="w-100" id="pic_1" src="@/assets/homepage/plane.png" alt="">
        <img class="w-100" id="pic_2" src="@/assets/homepage/houses.png" alt="">
      </div>
    </div>
  </div>
</template>

<script>
import {BACKEND} from "../../backend.config";
import axios from "axios";

export default {
  name: "Reviews",
  data() {
    return {
      reviews: [],
      loading: false
    }
  },
  methods: {
    loadReviews() {
      this.loading = true
      axios.get(BACKEND + "/api/getreviews").then(r => {
        this.loading = false
        console.log(r.data)
        this.reviews = r.data
      })
    }
  },
  mounted() {
    this.loadReviews()
  }
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

.review-card {
  padding: 20px;
  border-radius: 25px;
  box-shadow: 0 0 10px rgba(0, 0, 0, .3);

  h4 {
    font-size: 20px;
    line-height: 24px;
  }

  h5 {
    font-weight: 300;
    font-size: 20px;
    line-height: 24px;
  }

  p {
    font-weight: 300;
    font-size: 18px;
    line-height: 22px;
  }

  h6 {
    font-weight: 300;
    font-size: 20px;
    line-height: 24px;
  }
}

.more-reviews {
  font-size: 18px;
  text-decoration-line: underline;
  color: #032560;
}

.to-book {
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

.share {
  border-radius: 30px;
  box-shadow: 0 0 10px rgba(0, 0, 0, .3);
}

.images {
  aspect-ratio: .9;

  img {
    position: absolute;
    left: 0;
    transform: rotate(0);
    transition: all .3s ease;
  }

  #pic_1:hover {
    transform: rotate(-7deg) scale(1.01);
  }

  #pic_2:hover {
    transform: rotate(2deg) scale(1.01);
  }

  #pic_2 {
    top: 160px;
  }
}
</style>
