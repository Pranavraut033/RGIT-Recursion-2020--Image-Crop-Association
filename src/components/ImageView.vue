<template>
  <div class="img-container" v-if="image != 'NA'">
    <img
      :src="'/dataset/images/' + image"
      style=" border-bottom: 1px solid grey;"
    />
    <v-hover
      v-if="previewImage"
      :style="{
        top: previewImage[1][1] + 'px !important',
        left: previewImage[1][0] + 'px !important',
        height: previewImage[1][3] - previewImage[1][1] + 'px !important',
        width: previewImage[1][2] - previewImage[1][0] + 'px !important'
      }"
      v-slot:default="{ hover }"
    >
      <img
        :src="'/dataset/crops/' + previewImage[0]"
        class="preview-image elevation-2"
        :style="{
          opacity: hover ? 0.3 : 1,
          height: previewImage[1][2] - previewImage[1][0] + 'px !important',
          width: previewImage[1][3] - previewImage[1][1] + 'px !important'
        }"
      />
    </v-hover>

    <v-slide-group v-model="model" show-arrows class="w-100" mandatory>
      <v-slide-item
        v-for="(cropDetails, i) in crops"
        :key="i"
        :value="i"
        v-slot:default="{ active, toggle }"
      >
        <div>
          <v-img
            @click="toggle"
            class="ma-4 border"
            :src="'/dataset/crops/' + cropDetails[0]"
            width="68"
            height="68"
            :title="cropDetails[1]"
          ></v-img>
        </div>
      </v-slide-item>
    </v-slide-group>
  </div>
  <v-layout
    wrap
    fill-height
    v-else
    class="img-container"
    style="overflow:auto;height:600px"
  >
    <v-flex xs4 :key="i" v-for="(cropDetails, i) in crops">
      <div>
        <v-img
          class="ma-4 border"
          :src="'/dataset/crops/' + cropDetails[0]"
          width="68"
          height="68"
          contain
          :title="cropDetails[1]"
        ></v-img>
      </div>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  props: { image: String, crops: Array },
  data: () => ({
    model: -1
  }),
  computed: {
    previewImage() {
      return this.model == -1 ? null : this.crops[this.model];
    }
  }
};
</script>

<style lang="scss">
.img-container {
  // width: 400px;
  position: relative;

  .preview-image {
    border: 2px solid white;
    position: absolute;
    transition: all 300ms cubic-bezier(0.075, 0.82, 0.165, 1);
  }
}
</style>
