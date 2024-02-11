<template>
  <div id="navbar">
    <div>
      <button @click="clickEvent(true)" :disabled="sortingState">
        Generate New Data
      </button>
      <span>
        <label for="speed" :class="{ disabled: sortingState }">Speed</label>
        <input
          type="range"
          min="5"
          max="50"
          name="speed"
          v-model="speed"
          :disabled="sortingState"
        />
      </span>
    </div>
    <div id="algorithmButtons">
      <button @click="clickEvent(false, 'bubble')" :disabled="sortingState">
        Bubble Sort
      </button>
      <button @click="clickEvent(false, 'selection')" :disabled="sortingState">
        Selection Sort
      </button>
      <button @click="clickEvent(false, 'quick')" :disabled="sortingState">
        Quick Sort
      </button>
      <button @click="clickEvent(false, 'heap')" :disabled="sortingState">
        Heap Sort
      </button>
      <button @click="clickEvent(false, 'merge')" :disabled="sortingState">
        Merge Sort
      </button>
    </div>
  </div>
</template>
<script>
export default {
  name: "Navbar",
  data() {
    return {
      speed: 10,
    };
  },
  props: ["sortingState"],
  watch: {
    speed(value) {
      this.$emit("speed", value);
    },
  },
  methods: {
    clickEvent(resetGrid = false, activeAlgorithm = "") {
      let emitObject = {
        resetGrid: resetGrid,
        activeAlgorithm: activeAlgorithm,
      };
      this.$emit("clickEventObject", emitObject);
    },
  },
};
</script>
<style scoped>
#navbar {
  width: 78%;
  display: flex;
  position: relative;
  margin: 3rem auto;
  padding-top: 2rem;
  border-top: 3px solid #1f3b97;
}
#navbar div:nth-child(1) * {
  margin: 0 10px;
}
#algorithmButtons {
  position: absolute;
  right: 0;
}
button {
  padding: 15px;
  margin: 0 5px;
  color: #1f3b97;
  font-size: 15px;
  font-weight: bold;
  border: 1px solid;
  background: #fff;
  border-radius: 15px;
}
button:hover {
  background: #1f3b97;
  color: #fff;
}
button:disabled,
button[disabled],
input:disabled {
  background-color: #cccccc;
  color: #666666;
}
.disabled {
  color: #666666;
}
</style>
