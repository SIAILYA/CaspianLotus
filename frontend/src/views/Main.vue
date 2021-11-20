<template>
  <div>
    <TitleSection/>
    <SeaUnderLegs/>
    <PlaceWithFish/>
    <LeisureForAll/>
  </div>
</template>

<script>
import TitleSection from "@/components/homepage/TitleSection.vue";
import SeaUnderLegs from "@/components/homepage/SeaUnderLegs.vue";
import PlaceWithFish from "@/components/homepage/PlaceWithFish.vue";
import LeisureForAll from "@/components/homepage/LeisureForAll.vue";
export default {
  name: "Main",
  components: {TitleSection, SeaUnderLegs, PlaceWithFish, LeisureForAll}
}
</script>

<style scoped>

</style>
