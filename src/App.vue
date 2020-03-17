<template>
  <v-app class="bg">
    <router-view></router-view>
  </v-app>
</template>

<script>
export default {
  name: "App"
};
</script>

<style lang="scss">
.theme--light.v-application,
body {
  background: url("/bg.jpg") !important;
}
</style>
