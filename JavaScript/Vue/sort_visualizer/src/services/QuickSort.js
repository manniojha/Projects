import Vue from "vue";

export default new Vue({
  data() {
    return {
      counter: 0,
    };
  },
  methods: {
    run(arr) {
      this.counter = 0;
      this.quickSort(arr, 0, arr.length - 1);
    },
    quickSort(arr, left, right) {
      if (left >= right) {
        return false;
      }
      let pivot = arr[Math.floor((left + right) / 2)];
      let index = this.partition(arr, left, right, pivot);

      this.quickSort(arr, left, index - 1);
      this.quickSort(arr, index, right);
    },
    partition(arr, left, right, pivot) {
      while (left <= right) {
        while (arr[left] < pivot) {
          left++;
        }
        while (pivot < arr[right]) {
          right--;
        }
        if (left <= right) {
          let temp = arr[left];
          arr[left] = arr[right];
          arr[right] = temp;
          left++;
          right--;

          this.counter++;
          this.$emit("onItemSwap", {
            arr: [...arr],
            left,
            right,
            counter: this.counter,
          });
        }
      }
      return left;
    },
  },
});
