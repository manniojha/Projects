<template>
  <div>
    <div class="gridContainer">
      <div v-for="(bar, index) in barArray" :key="index" :id="`bar-${index}`">
        {{ bar }}
        <div class="bar" :style="{ height: `${bar * 3.5}px` }"></div>
      </div>
    </div>
  </div>
</template>

<script>
import BubbleSort from "../services/BubbleSort";
import QuickSort from "../services/QuickSort";
import SelectionSort from "../services/SelectionSort";
// import MergeSort from "../services/MergeSort";
import HeapSort from "../services/HeapSort";

const MAIN_BG_COLOR = "red";
const SECONDARY_BG_COLOR = "yellow";

export default {
  name: "Body",
  data() {
    return {
      bar: null,
      barArray: [],
      speed: this.sortingSpeed,
    };
  },
  props: ["clickEventObj", "sortingSpeed"],
  watch: {
    clickEventObj(value) {
      if (value.resetGrid) {
        this.createGrid();
      } else if (value.activeAlgorithm) {
        switch (value.activeAlgorithm) {
          case "bubble":
            this.bubbleSort();
            break;
          case "quick":
            this.quickSort();
            break;
          case "selection":
            this.selectionSort();
            break;
          case "merge":
            this.mergeSort();
            break;
          case "heap":
            this.heapSort();
            break;
          default:
            console.log(value.activeAlgorithm);
        }
      }
    },
  },
  methods: {
    createGrid() {
      this.barArray = [];
      for (let i = 0; i < 53; i++) {
        this.barArray.push(Math.floor(Math.random() * 100) + 5);
      }
      this.resetBackgroundColors(MAIN_BG_COLOR);
    },
    changeBarColor(index, color) {
      let element = document.querySelector(`#bar-${index} .bar`);
      if (element) {
        element.style.backgroundColor = color;
      }
    },
    resetBackgroundColors(color) {
      if (document.querySelector(".gridContainer")) {
        Array.from(document.querySelector(".gridContainer").children).forEach(
          (child) => {
            child.querySelector(".bar").style.backgroundColor = color;
          }
        );
      }
    },
    bubbleSort() {
      this.$emit("isSorting", true);
      let counter = 0;
      BubbleSort.$on("onItemSwap", (data) => {
        counter++;
        this.speed += 15;
        setTimeout(() => {
          this.resetBackgroundColors(MAIN_BG_COLOR);
          this.changeBarColor(data.index, SECONDARY_BG_COLOR);
          this.barArray = [...data.arr];
          if (data.counter == counter) {
            this.resetBackgroundColors(SECONDARY_BG_COLOR);
            this.$emit("isSorting", false);
          }
        }, this.speed);
      });

      BubbleSort.run(this.barArray);
      BubbleSort.$off();
    },
    quickSort() {
      this.$emit("isSorting", true);
      let counter = 0;
      QuickSort.$on("onItemSwap", (data) => {
        counter++;
        this.speed += 70;
        setTimeout(() => {
          this.resetBackgroundColors(MAIN_BG_COLOR);
          this.changeBarColor(data.left, SECONDARY_BG_COLOR);
          this.changeBarColor(data.right, SECONDARY_BG_COLOR);
          this.barArray = [...data.arr];
          if (data.counter == counter) {
            this.resetBackgroundColors(SECONDARY_BG_COLOR);
            this.$emit("isSorting", false);
          }
        }, this.speed);
      });
      QuickSort.run(this.barArray);
      QuickSort.$off();
    },
    selectionSort() {
      this.$emit("isSorting", true);
      let counter = 0;
      SelectionSort.$on("onItemSwap", (data) => {
        counter = counter + 1;
        this.speed += 100;
        setTimeout(() => {
          this.resetBackgroundColors(MAIN_BG_COLOR);
          this.barArray[data.left.index] = data.left.value;
          this.changeBarColor(data.left.index, SECONDARY_BG_COLOR);
          this.barArray[data.right.index] = data.right.value;
          this.changeBarColor(data.right.index, SECONDARY_BG_COLOR);
          this.barArray = [...this.barArray];
          if (counter == data.counter + 1) {
            this.resetBackgroundColors(SECONDARY_BG_COLOR);
            this.$emit("isSorting", false);
          }
        }, this.speed);
      });
      SelectionSort.run(this.barArray);
      SelectionSort.$off();
    },
    heapSort() {
      this.$emit("isSorting", true);
      HeapSort.$on("onItemSwap", (data) => {
        this.speed += 120;
        setTimeout(() => {
          this.resetBackgroundColors(MAIN_BG_COLOR);
          this.changeBarColor(data.left, SECONDARY_BG_COLOR);
          this.changeBarColor(data.right, SECONDARY_BG_COLOR);
          this.barArray = [...data.arr];
          if (data.isLast) {
            this.resetBackgroundColors(MAIN_BG_COLOR);
            this.$emit("isSorting", false);
          }
        }, this.speed);
      });
      HeapSort.run(this.barArray);
      HeapSort.$off();
    },
    // mergeSort() {
    //   MergeSort.run(this.barArray);
    // },
  },
  created() {
    this.createGrid();
  },
};
</script>

<style scoped>
.gridContainer {
  display: flex;
  justify-content: center;
  align-items: flex-end;
  gap: 8px;
}
.gridContainer div {
  font-weight: bold;
  font-size: 11px;
}
.bar {
  background: red;
  width: 18px;
}
</style>
