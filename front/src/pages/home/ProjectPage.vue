<template>
  <header>
    <h1>Proyectos</h1>
    <button class="return-button" @click="$router.go(-1)">↩</button>
  </header>
  <main>
    <button class="add-button" @click="setActive">Añadir teléfono</button>
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
      newPhone: {
        description: "",
        project: "",
        phone: "",
      },
      isActive: false,
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
      console.log(this.isActive);
    },
    setUnactived() {
      this.isActive = false;
    },
  },
};
</script>
<style scoped>
header {
  width: 100%;
  background: rgba(255, 148, 248, 0.63);
  font-family: "Raleway";
  color: rgb(120, 112, 112);
  padding: 1rem 0;
  font-size: 1em;
  text-align: center;
}
.add-button {
  padding: 0;
  margin: 6px;
  margin-left: 80%;
}
main {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  overflow-y: scroll;
  max-height: 78vh;
}
form {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  border-radius: 5px;
  background: white;
  box-shadow: 0px 0px 2px rgba(0, 0, 0, 0.5);
  border: 2px solid rgb(5, 210, 5);
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
.add-button {
  border: 2px solid rgba(0, 0, 0, 0.432);
  border-radius: 4px;
  background: rgba(200, 74, 204, 0.36);
  color: rgb(120, 112, 112);
  font-size: 1em;
  font-family: "Raleway";
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
.return-button {
  display: flex;
  flex-direction: row;
  padding: 1px 10px;
  margin-left: 1em;
  border: none;
  border-radius: 4px;
  background: rgba(96, 50, 84, 0.705);
  font-size: 1em;
  font-family: "Raleway";
  font-weight: bold;
  cursor: pointer;
}
</style>
