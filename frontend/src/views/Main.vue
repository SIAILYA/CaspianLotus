<template>
  <div>
    <TitleSection/>
    <SeaUnderLegs/>
    <PlaceWithFish/>
    <LeisureForAll/>
    <Reviews/>
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

export default {
  name: "Main",
  components: {TitleSection, SeaUnderLegs, PlaceWithFish, LeisureForAll, Reviews, Planing, Gallery}
}
</script>

<style scoped>

</style>
