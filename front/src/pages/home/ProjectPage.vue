<template>
  <header>
    <h1>Teléfonos</h1>
  </header>
  <main>
    <Telephone
      v-for="phone in phones"
      :key="phone.key"
      :description="phone.description"
      :project="phone.project"
      :phone="phone.phone"
    />
  </main>
</template>

<script>
import config from "../../config";
import Telephone from "../components/Telephone.vue";
export default {
  name: "Projects",
  components: {
    Telephone,
  },
  data() {
    return {
      phones: [],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      const settings = {
        method: "GET",
      };
      const response = await fetch(
        `${config.config.API_PATH}/phones`,
        settings
      );
      this.phones = await response.json();
    },
  },
};
</script>
<style scoped>
header {
  width: 100%;
  background: rgb(5, 210, 5);
  font-family: "Raleway";
  padding: 1rem 0;
  font-size: 1em;
  text-align: center;
}
main {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
</style>
