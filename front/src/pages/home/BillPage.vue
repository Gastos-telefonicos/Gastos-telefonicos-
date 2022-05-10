<template>
  <header>
    <h1>Factura #312</h1>
  </header>
  <main>
    <h1 class="title">Proyectos</h1>
    <section class="proyectos">
      <button class="asign">Asignar proyectos</button>
      <Project
        :projects="project"
        v-for="project in projects"
        :key="project"
      ></Project>
    </section>
    <button class="downloadButton" @click="exportDataToExcel">
      Descargar factura
    </button>
    <h2 class="totalPrice">
      Precio total ...................................................
      {{ totalPrice }}€
    </h2>
  </main>
</template>

<script>
import Project from "../components/Project.vue";
import exportFromJSON from "export-from-json";
import "xlsx";
export default {
  components: {
    Project,
  },

  data() {
    return {
      totalPrice: 0,
      projects: [
        {
          project: "Sin asignar",
          totalPrice: 0,
          phones: {
            691722323: 22,
            612232212: 15,
            791123321: 20,
          },
          class: "no-assigned",
        },
        {
          project: "GEN222442",
          totalPrice: 0,
          phones: {
            691722323: 10,
            612232212: 8,
            791123321: 91,
          },
          class: "project",
        },
        {
          project: "GEN22242442",
          totalPrice: 0,
          phones: {
            691722323: 15,
            612232212: 81,
            791123321: 28,
          },
          class: "project",
        },
      ],
    };
  },
  mounted() {
    this.totalPrice = this.getTotalPrice;
  },
  methods: {
    exportDataToExcel() {
      const data = this.projects;
      const fileName = "download";
      const exportType = "xls";
      exportFromJSON({ data, fileName, exportType });
      // for (let object of data) {
      //   for (let key of Object.values(object)) {
      //     //if key is an object
      //     if (typeof key === "object") {
      //       for (let phone of Object.keys(key)) {
      //         console.log(phone);
      //       }
      //     }
      //   }
      // }
    },
  },
  computed: {
    getTotalPrice() {
      const projects = this.projects;
      let totalPrice = 0;
      for (const project of projects) {
        totalPrice = project.totalPrice + totalPrice;
      }
      return totalPrice;
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Raleway:wght@600&display=swap");

body,
html {
  margin: 0;
  padding: 0;
}
header {
  width: 100%;
  background: rgb(5, 210, 5);
  font-family: "Raleway";
  padding: 1rem 0;
  font-size: 1em;
  text-align: center;
}
main .title {
  border-bottom: 2px solid black;
  padding: 0.5rem;
}
.totalPrice {
  margin-left: 1rem;
}
.proyectos {
  height: 55vh;
  overflow-y: scroll;
}
.asign {
  float: right;
  margin-right: 2rem;
  padding: 15px 25px;
  border: unset;
  border-radius: 15px;
  color: #212121;
  z-index: 1;
  background: #ffb2b2;
  position: relative;
  font-weight: 1000;
  font-size: 17px;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
  overflow: hidden;
}

button::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 0;
  border-radius: 15px;
  background-color: #212121;
  z-index: -1;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
}

button:hover {
  color: #e8e8e8;
  cursor: pointer;
}

button:hover::before {
  width: 100%;
}
.downloadButton {
  margin-top: 1rem;
  float: right;
  margin-right: 3rem;
  padding: 15px 25px;
  border: unset;
  border-radius: 15px;
  color: #212121;
  z-index: 1;
  background: #bbbbbb;
  position: relative;
  font-weight: 1000;
  font-size: 17px;
  -webkit-box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  box-shadow: 4px 8px 19px -3px rgba(0, 0, 0, 0.27);
  transition: all 250ms;
  overflow: hidden;
}
</style>