<template>
  <section id="table-projects">
    <table class="table">
      <tr class="table-body">
        <td><input id="phoneNumber" v-model="phoneData" readonly /></td>

        <td><input type="text" id="projectName" v-model="projectData" /></td>

        <td>
          <input type="text" id="descriptionName" v-model="descriptionData" />
        </td>
        <td>
          <input type="text" id="subaccountName" v-model="subaccountData" />
        </td>
        <button class="button" @click="deletePhone">
          <span>Eliminar</span>
        </button>
        <button class="button-modify" @click="onModifyButton">
          <span>Modificar</span>
        </button>
      </tr>
    </table>
  </section>
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

      alert("Teléfono eliminado exitosamente");
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
      alert("Cambios guardados exitosamente");
    },
  },
};
</script>

<style scoped>
* {
  padding: 0;
  margin: 0;
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
  margin-top: 0.5em;
  border-radius: 7px;
  border: none;
  background: #c55555b8;
  color: rgb(21, 11, 11);
  text-align: center;
  font-size: 12px;
  width: 10em;
  padding: 0.5em;
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
  text-align: center;
  font-size: 12px;
  width: 10em;
  padding: 0.5em;
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
  margin: 1em;
}
</style>
