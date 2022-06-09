<template>
  <form>
    <section class="form-data">
      <label for="phone">Teléfono: </label>
      <input id="phoneNumber" v-model="phoneData" readonly />
      <label for="project">Proyecto: </label>
      <input type="text" id="projectName" v-model="projectData" />
      <label for="project">Descripción: </label>
      <input type="text" id="descriptionName" v-model="descriptionData" />
      <label for="subaccount"> Subcuenta: </label>
      <input type="text" id="subaccountName" v-model="subaccountData" />

      <section>
        <button class="button" @click="deletePhone">
          <span>Eliminar</span>
        </button>
        <button class="button-modify" @click="onModifyButton">
          <span>Modificar</span>
        </button>
      </section>
    </section>
  </form>
  {{}}
</template>

<script>
import config from "../../config";
export default {
  props: {
    phone: {
      type: String,
      required: true,
    },
    project: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
    subaccount: {
      type: String,
      required: true,
    },
  },

  data() {
    return {
      phoneData: this.phone,
      descriptionData: this.description,
      projectData: this.project,
      subaccountData: this.subaccount,
    };
  },

  methods: {
    async deletePhone() {
      const settings = {
        method: "DELETE",
        body: JSON.stringify({
          phone: this.phoneData,
          project: this.projectData,
          description: this.descriptionData,
          subaccount: this.subaccountData,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      };
      await fetch(`${config.config.API_PATH}/phones`, settings);

      location.reload();

      alert("Contacto eliminado exitosamente");
    },
    async onModifyButton() {
      let jsonPhone = JSON.stringify({
        phone: this.phoneData,
        project: this.projectData,
        description: this.descriptionData,
        subaccount: this.subaccountData,
      });
      const settings = {
        method: "PUT",
        body: jsonPhone,
        headers: {
          "Content-Type": "application/json",
        },
      };
      await fetch(`${config.config.API_PATH}/phones`, settings);

      console.log(settings);
      alert("Contacto guardado exitosamente");
    },
  },
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
}
.form-data {
  display: flex;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.4);
  border-radius: 4px;
  gap: 0.3em;
  margin: 1em 3em 1em 3em;
  padding: 2em 0 2em 1em;
}
@media (min-width: 320px) and (max-width: 1281px) {
  .form-data {
    display: grid;
    padding: 5px;
    padding-right: 1em;
    margin-right: 3%;
    margin-left: 1%;
  }
  .form-data form label[type="text"] {
    grid-template-columns: 1fr 1fr;
  }
  .button {
    display: grid;
    grid-template-rows: 1fr 1fr;
  }
}
form {
  margin-left: 1em;
}
button {
  margin-left: auto;
  margin-right: 2rem;
  border-radius: 50%;
  width: 4vw;
  font-size: 2rem;
  background: rgba(205, 81, 108, 0.755);
}
.button {
  display: inline-block;
  border-radius: 7px;
  border: none;
  background: #c55555b8;
  color: rgb(21, 11, 11);
  font-family: inherit;
  text-align: center;
  font-size: 13px;
  width: 10em;
  padding: 1em;
  transition: all 0.4s;
  cursor: pointer;
}

.button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.4s;
}

.button span:after {
  content: "X";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.7s;
}

.button:hover span {
  padding-right: 3.55em;
}

.button:hover span:after {
  opacity: 4;
  right: 0;
}
.button-modify {
  display: inline-block;
  border-radius: 7px;
  border: none;
  background: #7b2e2fb8;
  color: rgb(16, 9, 9);
  font-family: inherit;
  text-align: center;
  font-size: 13px;
  width: 10em;
  padding: 1em;
  transition: all 0.4s;
  cursor: pointer;
}
.button-modify span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.4s;
}

.button-modify span:after {
  content: "✓";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.7s;
}

.button-modify:hover span {
  padding-right: 3.55em;
}

.button-modify:hover span:after {
  opacity: 4;
  right: 0;
}

#phoneNumber {
  border: none;
}
input {
  border-radius: 5px;
  border: 1px solid rgba(204, 115, 51, 0.387);
  text-align: center;
}
</style>
