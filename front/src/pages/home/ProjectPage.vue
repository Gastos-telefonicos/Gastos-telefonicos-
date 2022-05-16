<template>
  <h1></h1>

  <Projects :project="projects" @load="loadProjectsData" />
  {{ $data }}
</template>

<script>
import Projects from "@/pages/components/Project.vue";
export default {
  name: "Projects",
  components: {
    Projects,
  },
  data() {
    return {
      project: {
        id: "",
        projects: "",
        price: "",
      },
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
 