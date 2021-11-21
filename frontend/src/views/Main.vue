<template>
  <div>
    <TitleSection/>
    <SeaUnderLegs/>
    <PlaceWithFish/>
    <LeisureForAll/>
    <Reviews/>
    <div class="container mb-5">
      <section class="mt-5 houses-info">
        <h2 class="text-center">Информация о домиках</h2>
        <b-row class="justify-content-center mt-5">
          <div class="col-12 col-ld-10">
            <b-row>
              <div class="col-12 col-md-5 d-flex">
                <img alt="" class="houses-photo-1 w-100" src="@/assets/houses-1.jpeg">
              </div>
              <div class="col-12 d-flex col-md-7 houses-text text-center text-md-left">
              <span class="my-md-auto my-4">
                В нашем распоряжении 24 уютных домика, в каждом из которых может с комфортом поместиться 2 человека. Во всех домиках есть всё для длительного пребывания - санузел, сплит-система и небольшая кухня
              </span>
              </div>
            </b-row>
            <b-row>
              <div class="col-12 d-flex col-md-7 houses-text text-center text-md-left">
              <span class="my-md-auto my-4">
                Рядом с домиками есть пространство на свежем воздухе, где установлены беседки и мангалы для приготовления шашлыка и рыбы
              </span>
              </div>
              <div class="col-12 col-md-5 d-flex">
                <img alt="" class="houses-photo-2 w-100" src="@/assets/houses-2.jpeg">
              </div>
            </b-row>
          </div>
        </b-row>
      </section>
    </div>
    <div class="container">
      <booking-widget class="mb-4"></booking-widget>
    </div>
    <Planing/>
    <Gallery/>
  </div>
</template>

<script>
import TitleSection from "@/components/homepage/TitleSection.vue";
import SeaUnderLegs from "@/components/homepage/SeaUnderLegs.vue";
import PlaceWithFish from "@/components/homepage/PlaceWithFish.vue";
import LeisureForAll from "@/components/homepage/LeisureForAll.vue";
import Reviews from "@/components/homepage/Reviews";
import Planing from "@/components/homepage/Planing";
import Gallery from "@/components/homepage/Gallery";
import BookingWidget from "../components/BookingWidget";

export default {
  name: "Main",
  components: {BookingWidget, TitleSection, SeaUnderLegs, PlaceWithFish, LeisureForAll, Reviews, Planing, Gallery}
}
</script>

<style scoped lang="scss">
.houses-info {
  img {
    border-radius: 35px;
    box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);
  }

  .houses-photo-1 {
    transform: rotate(8deg);
    transition: all .3s ease;
  }

  .houses-photo-1:hover {
    transform: rotate(5deg) scale(1.01);
  }

  .houses-photo-2 {
    transform: rotate(-5deg);
    transition: all .3s ease;
  }

  .houses-photo-2:hover {
    transform: rotate(2deg) scale(1.01);
  }

  .houses-text {
    font-size: 24px;
  }
}

@media screen and (max-width: 768px) {
  .houses-photo-1{
    width: 75% !important;
    margin-left: auto;
    margin-right: auto;
  }
  .houses-photo-2{
    width: 75% !important;
    margin-left: auto;
    margin-right: auto;
  }
}
</style>
