<template>
  <section class="entryContainer">
    <div class="phone">☏ {{ entry.no_assigned_phone }}</div>
    <div class="description">👤 {{ entry.description }}</div>
    <div class="cost">💰 {{ entry.cost }}€</div>
  </section>
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
  },
  methods: {
    loadProjectsData() {
      this.$emit("load", this.projectInBill);
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
.entryContainer {
  display: flex;
  gap: 14em;
  margin-bottom: 0.5em;
  justify-content: flex-start;
  margin-left: 1em;
}
.description,
.cost {
  width: 20em;
  text-align: initial;
}
</style>
