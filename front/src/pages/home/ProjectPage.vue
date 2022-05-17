<template>
  <header>
    <h1>Teléfonos</h1>
  </header>
  <main>
    <Telephone
      v-for="phone in telephones"
      :key="phone.key"
      :owner="phone.owner"
      :price="phone.price"
      :project="phone.project"
      :telephone="phone.telephone"
    />
  </main>
</template>


<script>
import Telephone from "../components/Telephone.vue";
export default {
  name: "Projects",
  components: {
    Telephone,
  },
  data() {
    return {
      telephones: [
        {
          id: "1",
          project: "GEN222321",
          price: "22.12",
          owner: "Josu",
          telephone: "612432234",
        },
        {
          id: "2",
          project: "GEN214221",
          price: "11.75",
          owner: "Joseba",
          telephone: "661358944",
        },
        {
          id: "3",
          project: "GEN122444",
          price: "96.12",
          owner: "Rocio",
          telephone: "612832534",
        },
      ],
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {},
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