<template>
  <article>
    <h3>{{ phone }}</h3>
    <h3>{{ project }}</h3>
    <h3>{{ description }}</h3>
    <button @click="deletePhone" class="button" style="vertical-align: middle">
      <span>Eliminar</span>
    </button>
  </article>
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
  },

  data() {
    return {
      phoneData: this.phone,
      descriptionData: this.description,
      projectData: this.project,
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
        }),
        headers: {
          "Content-Type": "application/json",
        },
      };
      await fetch(`${config.config.API_PATH}/phones`, settings);
      location.reload();
    },
  },
};
</script>

<style scoped>
article {
  display: flex;
  box-shadow: 0px 0px 8px rgba(0, 0, 0, 0.4);
  gap: 1rem;
}
article h3 {
  margin-left: 4rem;
}
button {
  margin-left: auto;
  margin-right: 2rem;
  border-radius: 50%;
  width: 4vw;
  font-size: 2rem;
  background: rgba(255, 0, 0, 0.755);
}
.button {
  display: inline-block;
  border-radius: 7px;
  border: none;
  background: #ff2020b8;
  color: white;
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
</style>
