<template>
  <header>
    <h1>Factura</h1>
  </header>
  <main>
    <div v-if="isLoading" class="loading">
      <h2>Procesando factura</h2>
      <p>Loading&#8230;</p>
    </div>
    <h1 class="title">Proyectos</h1>
    <section class="proyectos">
      <button @click="sendToRoute('/projects')" class="asign">Proyectos</button>
      <article class="projects">
        <div v-for="entries of projectEntries" :key="entries">
          <h3 class="project" v-if="entries[0] != ''">{{ entries[0] }}</h3>
          <h3 class="no-assigned" v-else>Sin asignar</h3>
          <hr />
          <div v-for="entry of entries[1]" :key="entry">
            <Project :entry="entry"></Project>
          </div>
        </div>
      </article>
    </section>
    <button class="downloadButton" @click="exportDataToExcel">
      Descargar factura
    </button>
  </main>
</template>

<script>
import Project from "../components/Project.vue";
import config from "@/config";
import exportFromJSON from "export-from-json";
import { goTo } from "@/helpers/index";
export default {
  components: {
    Project,
  },

  data() {
    return {
      phones: [],
      totalPrice: 0,
      projects: [],
      projectEntries: {},
      excelData: [],
      isLoading: false,
    };
  },
  mounted() {
    this.totalPrice = this.getTotalPrice;
    this.getFullData();
  },

  methods: {
    sendToRoute(route) {
      goTo(route, this.$router);
    },
    getObjectEntries() {
      let projectEntries = Object.entries(this.projects);
      this.projectEntries = projectEntries;
      for (let entry of projectEntries) {
        this.excelData.push(entry);
      }
    },
    setNewObject() {
      let result = this.phones.reduce(function (projects, phone) {
        console.log("R ES", projects);
        console.log("A ES", phone);
        projects[phone.project] = projects[phone.project] || [];
        projects[phone.project].push(phone);
        return projects;
      }, Object.create(null));
      this.projects = result;
      this.getObjectEntries();
    },
    async getFullData() {
      this.isLoading = true;
      await new Promise((resolve) => setTimeout(resolve, 2000));
      const response = await fetch(
        `${config.config.API_PATH}/phones/full-data`
      );
      const data = await response.json();
      this.phones = data;
      this.setNewObject();
      this.isLoading = false;
    },
    exportDataToExcel() {
      const data = this.phones.map((project) => {
        return {
          Descripcion: project.description,
          Teléfono: project.phone,
          Proyecto: project.project,
        };
      });

      const fileName = "download";
      const exportType = "xls";
      exportFromJSON({ data, fileName, exportType });
    },
  },
  computed: {},
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
  font-family: "Raleway";
  background: #7b2e2fb8;
  color: rgb(16, 9, 9);
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
  margin-right: 1rem;
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
.no-assigned {
  color: #7b2e2fb8;
}
.project {
  color: rgba(201, 136, 111, 0.856);
  margin-left: 1em;
}
.loading {
  position: fixed;
  z-index: 999;
  height: 2em;
  width: 2em;
  overflow: visible;
  margin: auto;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

/* Transparent Overlay */
.loading:before {
  content: "";
  display: block;
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.3);
}

.loading:not(:required) {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}

.loading:not(:required):after {
  content: "";
  display: block;
  font-size: 10px;
  width: 1em;
  height: 1em;
  margin-top: -0.5em;
  -webkit-animation: spinner 1500ms infinite linear;
  -moz-animation: spinner 1500ms infinite linear;
  -ms-animation: spinner 1500ms infinite linear;
  -o-animation: spinner 1500ms infinite linear;
  animation: spinner 1500ms infinite linear;
  border-radius: 0.5em;
  -webkit-box-shadow: rgba(0, 0, 0, 0.75) 1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) 1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) 0 1.5em 0 0,
    rgba(0, 0, 0, 0.75) -1.1em 1.1em 0 0, rgba(0, 0, 0, 0.5) -1.5em 0 0 0,
    rgba(0, 0, 0, 0.5) -1.1em -1.1em 0 0, rgba(0, 0, 0, 0.75) 0 -1.5em 0 0,
    rgba(0, 0, 0, 0.75) 1.1em -1.1em 0 0;
  box-shadow: rgba(0, 0, 0, 0.75) 1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) 1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) 0 1.5em 0 0,
    rgba(0, 0, 0, 0.75) -1.1em 1.1em 0 0, rgba(0, 0, 0, 0.75) -1.5em 0 0 0,
    rgba(0, 0, 0, 0.75) -1.1em -1.1em 0 0, rgba(0, 0, 0, 0.75) 0 -1.5em 0 0,
    rgba(0, 0, 0, 0.75) 1.1em -1.1em 0 0;
}

/* Animation */

@-webkit-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-moz-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@-o-keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
@keyframes spinner {
  0% {
    -webkit-transform: rotate(0deg);
    -moz-transform: rotate(0deg);
    -ms-transform: rotate(0deg);
    -o-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(360deg);
    -moz-transform: rotate(360deg);
    -ms-transform: rotate(360deg);
    -o-transform: rotate(360deg);
    transform: rotate(360deg);
  }
}
</style>
