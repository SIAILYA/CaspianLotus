<template>
  <div class="container text-center mt-5">
    <b-modal id="modal-viewer" size="xl" title="Фотография" ok-only>
      <img :src="activePhoto" class="w-100 rounded-sm" alt="">
      <a class="d-flex mt-3" :href="activePhoto" target="_blank">
        <span class="material-icons-outlined my-auto mr-2">link</span>
        <span class="my-auto">Открыть в новом окне</span>
      </a>
    </b-modal>
    <h1 id="photos">
      Фотогалерея
    </h1>
    <h3>
      Лучше один раз увидеть, чем сто раз услышать! Смотрите<br>свежие фотографии с нашей базы
    </h3>
    <div class="images d-flex flex-wrap flex-md-row flex-column mt-5" v-if="!photosLoading">
      <div class="col-md-3 col-12 px-1" v-for="(ph, index) in photos" :key="ph">
        <img :src="BACKEND + ph" :alt="'photogallery_' + (index + 1)" @click="openViewer(BACKEND + ph)">
      </div>
    </div>
    <div v-else class="text-center my-3">
      <b-spinner type="grow"></b-spinner>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import {BACKEND} from "../../backend.config";

export default {
  name: "Gallery",
  data() {
    return {
      photos: [],
      photosLoading: true,
      BACKEND: BACKEND,
      activePhoto: ""
    }
  },
  methods: {
    openViewer(aph) {
      this.$bvModal.show("modal-viewer")
      this.activePhoto = aph
    }
  },
  mounted() {
    this.photosLoading = true
    axios.get(BACKEND + "/api/get_photos").then(r => {
      this.photos = r.data
      this.photosLoading = false
    })
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

.images {
  img {
    width: 100%;
    border-radius: 20px;
    box-shadow: 0px 0px 14px rgba(0, 0, 0, 0.25);
  }
}
</style>
