<template>
  <div class="px-4">
    <h1 class="logo text-center primary--text  mt-3 pa-3 mb-0">
      Meticulous Machines
    </h1>
    <v-layout class="px-12 py-2" align-center justify-center>
      <v-btn color="primary" @click="jsonDialog = true" depressed width="200">
        Show JSON
      </v-btn>

      <v-btn
        color="primary"
        @click="matrixDialog = true"
        depressed
        width="200"
        class="mx-3 "
      >
        Show Metrics
      </v-btn>
      <v-btn
        color="white"
        style="border: 1px solid #FF7373 !important;"
        @click="gameDialog = true"
        class="primary--text elevation-0"
        width="200"
      >
        Play Game
      </v-btn>
    </v-layout>
    <div class="pa-3 px-12"></div>
    <v-slide-group column align-center>
      <v-slide-item v-for="(crops, image) in result" :key="image">
        <v-card class="ma-2 elevation-4" outlined style="border-color: #F8ADBA">
          <v-card-text>
            <ImageView :crops="crops" :image="image"> </ImageView>
          </v-card-text>
        </v-card>
      </v-slide-item>
      <template v-slot:next>
        <v-btn color="primary" fab>
          <v-icon large>mdi-arrow-right-bold</v-icon>
        </v-btn>
      </template>
      <template v-slot:prev>
        <v-btn color="primary" fab>
          <v-icon large>mdi-arrow-left-bold</v-icon>
        </v-btn>
      </template>
    </v-slide-group>

    <v-dialog v-model="gameDialog" max-width="450px" scrollable="">
      <v-card outlined>
        <v-card-title>
          Game
        </v-card-title>
        <v-card-text>
          <game></game>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="matrixDialog" scrollable width="320">
      <v-card>
        <v-card-title>Metrics</v-card-title>
        <v-card-text>
          <v-layout justify-center column align-center="">
            <table class="table-border">
              <tr>
                <td class="primary darken-2 white--text">TP: 236</td>
                <td class="primary white--text lighten-2 ">FP: 0</td>
              </tr>
              <tr>
                <td class="primary white--text">FN: 32</td>
                <td class="primary lighten-1 white--text">TN: 16</td>
              </tr>
              <caption>
                Confusion Matrix
              </caption>
            </table>
          </v-layout>
          <v-divider class="my-3"></v-divider>
          <table>
            <tr>
              <th>Precision</th>
              <td>1</td>
            </tr>
            <tr>
              <th>Recall</th>
              <td>0.88</td>
            </tr>
            <tr>
              <th>F1</th>
              <td>0.94</td>
            </tr>
          </table>
        </v-card-text>
      </v-card>
    </v-dialog>
    <v-dialog v-model="jsonDialog" scrollable>
      <v-card>
        <v-card-title>JSON output</v-card-title>
        <v-card-text>
          <v-layout>
            <!-- <v-flex xs6>
              <pre>{{ result }}</pre>
            </v-flex> -->
            <v-flex xs6>
              <JsonViewer :value="result" :expand-depth="5"></JsonViewer>
            </v-flex>
          </v-layout>
        </v-card-text>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import ImageView from "@/components/ImageView.vue";
import Game from "@/components/Game.vue";
import JsonViewer from "vue-json-viewer";

export default {
  components: { ImageView, JsonViewer, Game },
  name: "Home",

  data: () => ({
    result: {},
    jsonDialog: false,
    gameDialog: false,
    matrixDialog: false
  }),

  mounted() {
    fetch("/result.json")
      .then(res => res.json())
      .then(res => (this.result = res))
      .catch(err => {
        console.error(err);
      });
  }
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Great+Vibes&display=swap");
.border {
  border: 0.124rem solid rgba($color: #000000, $alpha: 0.2);
}
.logo {
  font-family: "Great Vibes", cursive;
  font-size: 48pt;
  margin-bottom: 0 !important;
  text-shadow: 1px 2px 6px #ffffff8e;
}
table.table-border {
  th,
  td {
    border: 0.1125rem solid #0000008e;
  }
}
table {
  color: #000000c4;
}
td,
th {
  font-size: 14pt;
  padding: 0.25rem 1rem;
}
</style>
