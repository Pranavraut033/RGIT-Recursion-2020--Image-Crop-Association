<template>
  <v-stepper v-model="step" class="elevation-0 pa-0">
    <v-stepper-content :step="1" class="pa-0">
      <p>
        A Image will be shown for 1s.
      </p>
      <v-btn color="primary" block @click="start()" @>Continue</v-btn>
    </v-stepper-content>
    <v-stepper-content :step="2" v-if="image.crop" class="pa-0">
      <p>You have {{ time }}s to remember</p>
      <v-img :src="'dataset/crops/' + image.crop.name"></v-img>
    </v-stepper-content>
    <v-stepper-content :step="3" v-if="image.crop" class="pa-0">
      <div style="position: relative">
        <p v-if="notFound">
          <span class="error--text">
            Failed to find the matching piece
          </span>
          <v-btn small color="primary" depressed @click="init">
            Play again
          </v-btn>
        </p>
        <p v-else>You have {{ time }}s to find the matching location</p>
        <v-img :src="'dataset/images/' + image.name"></v-img>
        <img
          @click="found = true"
          :src="'dataset/crops/' + image.crop.name"
          :style="{
            border: '2px solid red',
            opacity: notFound ? 1 : 0,
            position: 'absolute',
            top: image.crop.loc[1] + 'px !important',
            left: image.crop.loc[0] + 'px !important',
            height: image.crop.loc[3] - image.crop.loc[1] + 'px !important',
            width: image.crop.loc[2] - image.crop.loc[0] + 'px !important',
            transition: ' all 300ms cubic-bezier(0.075, 0.82, 0.165, 1)'
          }"
        />
      </div>
      <v-dialog v-model="found" max-width="390px">
        <v-card>
          <v-card-title>Piece Found!</v-card-title>
          <v-card-text>
            <v-img
              v-if="image.crop"
              :src="'dataset/crops/' + image.crop.name"
              height="68"
              contain
            ></v-img>
            <p class="mt-3 ma-0">
              Congratulation! You found the matching piece.
            </p>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" depressed @click="init">Play again</v-btn>
            <v-spacer></v-spacer>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-stepper-content>
  </v-stepper>
</template>

<script>
export default {
  data: () => ({
    time: "",
    timerId: 0,
    step: 1,
    images: "",
    image: {
      name: "",
      crop: null
    },
    found: false
  }),
  methods: {
    init() {
      this.step = 1;
      this.found = false;
      this.notFound = false;
      clearInterval(this.timerId);

      if (!this.images) return;

      var index = this.getRandomArbitrary(0, this.images.length - 1);

      this.image = {
        name: this.images[index].name,
        crop: this.images[index].crops[
          this.getRandomArbitrary(0, this.images[index].crops.length - 1)
        ]
      };
    },
    start() {
      this.step = 2;
      this.time = 1;

      this.timerId = setInterval(() => {
        this.time--;
        if (this.time == 0) {
          clearInterval(this.timerId);
          this.showGame();
        }
      }, 1000);
    },
    showGame() {
      this.step = 3;
      this.time = 30;

      this.timerId = setInterval(() => {
        this.time--;
        if (this.time == 0) {
          clearInterval(this.timerId);
          this.notFound = true;
        }
      }, 1000);
    },
    getRandomArbitrary(min, max) {
      return Math.ceil(Math.random() * (max - min) + min);
    }
  },
  mounted() {
    this.init();
    fetch("/result.json")
      .then(res => res.json())
      .then(res => {
        let a = [];
        for (const image in res) {
          const details = res[image];
          a.push({
            name: image,
            crops: details.map(ev => ({ name: ev[0], loc: ev[1] }))
          });
        }
        this.images = a;
        this.init();
      })
      .catch(err => {
        console.error(err);
      });
  }
};
</script>

<style></style>
