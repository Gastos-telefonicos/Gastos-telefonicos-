<template>
  <main class="home">
    <ul class="background">
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
      <li></li>
    </ul>
    <div class="container">
      <input @change="previewFiles" type="file" id="myFile" class="btn" />
      <br />
      <router-link to="/bill"> <button>Ejecutar</button></router-link>
    </div>
  </main>
</template>

<script>
import config from "../../config";
export default {
  name: "Home",
  data() {
    return {
      file: "",
    };
  },
  mounted() {},
  methods: {
    async previewFiles(event) {
      const settings = {
        method: "POST",
        headers: {
          "Content-Type": "application/pdf",
        },
        body: event.target.files[0],
      };
      console.log(event.target.files[0]);
      await fetch(`${config.config.API_PATH}/docs`, settings);
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=Roboto:wght@500&display=swap");
h1 {
  font-style: italic;
}
.container {
  display: grid;
  place-content: center;
  border: 5px dotted green;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.2);
  width: 50vw;
  height: 40vh;
  z-index: 2;
}
@media screen and (max-width: 600px) {
  .container {
    width: 90vw;
    height: 40vh;
  }
}

.btn {
  padding: 1.1em 2em;
  background: none;
  font-family: Roboto;
  border: 2px solid #fff;
  font-size: 3vh;
  color: #131313;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: all 0.3s;
  border-radius: 12px;
  background-color: #a5ec48;
  font-weight: bolder;
  box-shadow: 0 2px 0 2px #000;
}

.btn:before {
  content: "";
  position: absolute;
  width: 100px;
  height: 120%;
  background-color: #00ff4c;
  top: 50%;
  transform: skewX(30deg) translate(-150%, -50%);
  transition: all 0.5s;
}

.btn:hover {
  background-color: #4cf065;
  color: #fff;
  box-shadow: 0 2px 0 2px #0d3b66;
}

.btn:hover::before {
  transform: skewX(30deg) translate(150%, -50%);
  transition-delay: 0.1s;
}

.btn:active {
  transform: scale(0.9);
}
@keyframes animate {
  0% {
    transform: translateY(0) rotate(0deg);
    opacity: 1;
    border-radius: 0;
  }
  100% {
    transform: translateY(-1000px) rotate(720deg);
    opacity: 0;
    border-radius: 50%;
  }
}
main {
  display: grid;
  place-content: center;
  height: 96vh;
}
@keyframes cube {
  from {
    transform: scale(0) rotate(0deg) translate(-50%, -50%);
    opacity: 1;
  }
  to {
    transform: scale(20) rotate(960deg) translate(-50%, -50%);
    opacity: 0;
  }
}

.background {
  position: fixed;
  width: 100vw;
  height: 100vh;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  background: #38b602;
  overflow: hidden;
}
.background li {
  position: absolute;
  top: 80vh;
  left: 45vw;
  width: 10px;
  height: 10px;
  border: solid 1px #32a301;
  color: transparent;
  transform-origin: top left;
  transform: scale(0) rotate(0deg) translate(-50%, -50%);
  animation: cube 16s ease-in forwards infinite;
}
undefined .background li:nth-child(0) {
  animation-delay: 0s;
  left: 44vw;
  top: 96vh;
}

.background li:nth-child(1) {
  animation-delay: 2s;
  left: 52vw;
  top: 85vh;
}

.background li:nth-child(2) {
  animation-delay: 4s;
  left: 1vw;
  top: 76vh;
}

.background li:nth-child(3) {
  animation-delay: 6s;
  left: 62vw;
  top: 59vh;
  border-color: #3dc802;
}

.background li:nth-child(4) {
  animation-delay: 8s;
  left: 91vw;
  top: 43vh;
  border-color: #3dc802;
}

.background li:nth-child(5) {
  animation-delay: 10s;
  left: 22vw;
  top: 32vh;
}

.background li:nth-child(6) {
  animation-delay: 12s;
  left: 16vw;
  top: 50vh;
  border-color: #3dc802;
}

.background li:nth-child(7) {
  animation-delay: 14s;
  left: 99vw;
  top: 62vh;
  border-color: #3dc802;
}

.background li:nth-child(8) {
  animation-delay: 16s;
  left: 38vw;
  top: 70vh;
}

.background li:nth-child(9) {
  animation-delay: 18s;
  left: 8vw;
  top: 92vh;
}

.background li:nth-child(10) {
  animation-delay: 20s;
  left: 59vw;
  top: 7vh;
}

.background li:nth-child(11) {
  animation-delay: 22s;
  left: 71vw;
  top: 39vh;
  border-color: #3dc802;
}

.background li:nth-child(12) {
  animation-delay: 24s;
  left: 82vw;
  top: 20vh;
}

.background li:nth-child(13) {
  animation-delay: 26s;
  left: 74vw;
  top: 18vh;
  border-color: #3dc802;
}

.background li:nth-child(14) {
  animation-delay: 28s;
  left: 31vw;
  top: 4vh;
}
</style>
