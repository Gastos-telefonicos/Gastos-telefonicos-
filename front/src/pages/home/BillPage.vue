<template>
  <header>
    <h1>Factura #312</h1>
  </header>
  <main>
    <h1 class="title">Proyectos</h1>
    <section class="proyectos">
      <button class="asign">Asignar proyectos</button>
      <article class="projects">
        <div v-for="entries of projectEntries" :key="entries">
          <h3 class="project" v-if="entries[0] != ''">{{entries[0]}}</h3>
          <h3 class="no-assigned" v-else>Sin asignar</h3>    
          <hr>
          <div v-for="entry of entries[1]" :key="entry">
            <Project :entry=entry></Project>
            </div>
        </div>
      </article>
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
import config from "@/config";
import exportFromJSON from "export-from-json";
export default {
  components: {
    Project
  },

  data() {
    return {
      phones: [],
      totalPrice: 0,
      projects: [],
      projectEntries:{}
    };
  },
  mounted() {
    this.totalPrice = this.getTotalPrice;
    this.getFullData();
  },
 
  methods: {
    getObjectEntries(){
      let projectEntries = Object.entries(this.projects)
      this.projectEntries = projectEntries

    },
    setNewObject() {
      //Es de google,no lo entiendo mucho xD.
      let result = this.phones.reduce(function (r, a) {
        r[a.project] = r[a.project] || [];
        r[a.project].push(a);
        return r;
      }, Object.create(null));
      this.projects = result;
      this.getObjectEntries();
    },
    async getFullData() {
      const response = await fetch(
        `${config.config.API_PATH}/phones/full-data`
      );
      const data = await response.json();
      this.phones = data;
      this.setNewObject();
    },
    exportDataToExcel() {
      const data = this.projects.map((project) => {
        return {
          Proyecto: project.project,
          Haber: 0,
          Debe: project.totalPrice,
        };
      });
      const fileName = "download";
      const exportType = "xls";
      exportFromJSON({ data, fileName, exportType });
    },
  },
  computed: {
    
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
.no-assigned {
  color: #ff0000;
} 
.project {
  color: green;
} 
</style>