<template>
  <header>
    <h1>Lista de teléfonos</h1>
    <button class="return-button" @click="onButtonBack()">↩</button>
  </header>
  <main>
    <form action="" v-bind:class="{ actived: isActive, unactived: !isActive }">
      <button class="delete" @click.prevent="setUnactived">X</button>
      <label for="Número de telefono">Teléfono</label>
      <input type="text" v-model="newPhone.phone" />
      <label for="Descripción">Descripción</label>
      <input type="text" v-model="newPhone.description" />
      <label for="Proyecto">Proyecto</label>
      <input type="text" v-model="newPhone.project" />
      <button class="green-button" @click="addNewTelephone">Añadir</button>
    </form>
    <div v-if="isLoading" class="loading">
      <h2>Procesando factura</h2>
      <p>Loading&#8230;</p>
    </div>
    <div class="filter">
      <input
        type="text"
        placeholder="Filtrar por proyectos..."
        v-model="search"
      />
    </div>
    <div class="main-selection">
      <button class="add-button" @click="setActive">Añadir teléfono</button>
    </div>
    <section>
      <table>
        <thead class="table-head">
          <th>Teléfono</th>
          <th>Proyecto</th>
          <th>Descripción</th>
          <th>Subcuenta</th>
        </thead>
        <tbody>
          <div>
            <Telephone
              v-for="phone in filteredPhones"
              :key="phone"
              :description="phone.description"
              :project="phone.project"
              :phone="phone.phone"
              :subaccount="phone.subaccount"
            />
          </div>
        </tbody>
      </table>
    </section>
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
      searchProject: "",
      isLoading: false,
      search: "",
      newPhone: {
        description: "",
        project: "",
        phone: "",
        subaccount: "",
      },
      isActive: false,
    };
  },
  mounted() {
    this.loadData();
  },
  methods: {
    async loadData() {
      this.isLoading = true;
      const settings = {
        method: "GET",
      };
      const response = await fetch(
        `${config.config.API_PATH}/phones`,
        settings
      );
      this.phones = await response.json();
      this.isLoading = false;
    },
    async addNewTelephone() {
      const settings = {
        method: "POST",
        body: JSON.stringify(this.newPhone),
        headers: {
          "Content-Type": "application/json",
        },
      };
      const response = await fetch(
        `${config.config.API_PATH}/phones`,
        settings
      );
      this.phones = await response.json();
      this.isActive = false;
    },
    setActive() {
      this.isActive = true;
    },
    setUnactived() {
      this.isActive = false;
    },
    onButtonBack() {
      this.$router.push("/bill");
    },
  },

  computed: {
    filteredPhones() {
      return this.phones.filter((phone) => {
        if (
          phone.project.toLowerCase().includes(this.search.toLowerCase()) ||
          phone.description.toUpperCase().includes(this.search.toUpperCase()) ||
          phone.phone.toLowerCase().includes(this.search.toLowerCase())
        ) {
          return true;
        } else {
          return false;
        }
      });
    },
  },
};
</script>
<style scoped>
* {
  padding: 0;
  margin: 0;
}
header {
  width: 100%;
  padding-top: 1em;
  background: #7b2e2fb8;
  color: rgb(16, 9, 9);
  font-size: 1em;
  text-align: center;
}

form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  border-radius: 5px;
  background: white;
  box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.5);
  border: 2px solid #cb8565a5;
  height: 40vh;
  width: 20vw;
  gap: 0.4rem;
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
  padding: 2rem;
}
form input {
  border: 2px solid rgba(0, 0, 0, 0.432);
  border-radius: 4px;
  max-width: 100%;
}
.green-button {
  border: 2px solid rgba(0, 0, 0, 0.432);
  border-radius: 4px;
  background: #cb8565a5;
  color: black;
  font-size: 1em;
  font-family: "Raleway";
  font-weight: bold;
  cursor: pointer;
}
.unactived {
  visibility: hidden;
}
.actived {
  visibility: visible;
}
.delete {
  border: 2px solid rgba(0, 0, 0, 0.432);
  border-radius: 4px;
  background: rgb(255, 90, 90);
  color: black;
  font-size: 1em;
  font-family: "Raleway";
  font-weight: bold;
  cursor: pointer;
}

@media (min-width: 320px) and (max-width: 1281px) {
  .add-button {
    padding: 0;
    margin: 6px;
    margin-left: 80%;
  }
}
thead {
  display: flex;
  justify-content: space-evenly;
  margin-left: 9em;
  gap: 8em;
  width: 49%;
}
tbody {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding: 1em;
}
.filter {
  display: flex;
  justify-content: center;
  margin-top: 1em;
}
.main-selection {
  display: flex;
  justify-content: flex-end;
  width: 83%;
  margin-top: 1em;
}

.add-button {
  border: none;
  background: #cb8565a5;
  color: rgb(35, 29, 29);
  font-size: 12px;
  font-family: "Raleway";
  cursor: pointer;
  padding: 1em;
  border-radius: 7px;
}

.unactived {
  visibility: hidden;
}
.actived {
  visibility: visible;
  position: absolute;
  left: 0;
  right: 0;
}

.delete {
  border: 2px solid rgba(0, 0, 0, 0.432);
  border-radius: 4px;
  background: rgb(255, 90, 90);
  color: black;
  font-size: 1em;
  font-family: "Raleway";
  font-weight: bold;
  cursor: pointer;
}
.return-button {
  display: flex;
  flex-direction: row;
  padding: 1px 10px;
  margin-left: 1em;
  border: none;
  border-radius: 4px;
  background: rgba(224, 190, 156, 0.705);
  font-size: 1em;
  font-family: "Raleway";
  font-weight: bold;
  cursor: pointer;
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
