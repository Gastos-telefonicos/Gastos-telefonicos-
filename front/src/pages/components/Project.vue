<template>
  <article>
    <p>
      {{ entry.phone }} --- {{entry.description}} ---{{ entry.cost }}€
    </p>
  </article>
</template>

<script>
export default {
  name: "Projects",
  data() {
    return {
      projectInBill: this.projects,
      totalPrice: 0,
    };
  },
  props: {
  
    entry: {
      type: Object,
      required: true,
    },
  },
  mounted() {
    this.loadProjectsData;
    this.projectInBill.totalPrice = this.getTotalProjectPrice;
  },
  methods: {
    loadProjectsData() {
      this.$emit("load", this.projectInBill);
    },
  },
  computed: {
    getTotalProjectPrice() {
      const prices = this.projectInBill.phones;
      let totalPrice = 0;
      for (const price in prices) {
        totalPrice = totalPrice + prices[price];
      }
      return totalPrice;
    },
  },
  emits: ["load"],
  watch: {
    project: {
      handler(newValue) {
        const projectAsJson = JSON.stringify(newValue);
        this.projectInBill = JSON.parse(projectAsJson);
      },
      inmediate: true,
    },
  },
};
</script>

<style scoped>
h2 {
  border-bottom: 2px solid black;
  padding: 0.5rem;
  margin: 1rem;
}
p {
  margin-left: 2rem;
}


</style>
