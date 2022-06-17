<template>
  <article id="entryContainer">
    <div class="phone">☏ {{ entry.no_assigned_phone }}</div>
    <div class="description">👤{{ entry.description }}</div>
    <div class="cost">💰{{ entry.cost }}€</div>
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
h2 {
  border-bottom: 2px solid black;
  padding: 0.5rem;
  margin: 1rem;
}
p {
  margin-left: 2rem;
}

#entryContainer {
  display: grid;
  grid-template-columns: auto auto auto;
  width: 50%;
}
#entryContainer.description {
  align-content: start;
}
#entryContainer.cost {
  align-content: start;
}
</style>
