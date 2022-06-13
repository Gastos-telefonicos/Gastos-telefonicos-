<template>
  <TopHeader />
  <router-view />
</template>

<script>
import TopHeader from "./pages/components/TopHeader.vue";
export default {
  name: "Projects",
  components: {
    TopHeader,
  },
};
</script>
<style>
* {
  box-sizing: border-box;
}
body,
html {
  margin: 0;
  padding: 0;
  min-height: 100vh;
}
</style>
