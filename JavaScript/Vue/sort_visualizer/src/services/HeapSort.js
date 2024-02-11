import Vue from "vue";

export default new Vue({
  methods: {
    run(arr) {
      arr = [...arr];
      let n = arr.length;
      // Build Max Heap
      for (let i = Math.floor(n / 2) - 1; i >= 0; i--) {
        this.heapify(arr, n, i);
      }
      // One by one extract an element from heap
      for (let i = n - 1; i >= 0; i--) {
        this.$emit("onItemSwap", {
          arr: [...arr],
          left: 0,
          right: i,
          isLast: i == 0,
        });
        this.swap(arr, 0, i);
        this.heapify(arr, i, 0);
      }
    },
    heapify(arr, n, i) {
      let largest = i,
        left = 2 * i + 1,
        right = 2 * i + 2;

      if (left < n && arr[left] > arr[largest]) largest = left;
      if (right < n && arr[right] > arr[largest]) largest = right;
      if (largest != i) {
        this.swap(arr, i, largest);
        this.heapify(arr, n, largest);
      }
    },
    swap(arr, l, r) {
      let swap = arr[l];
      arr[l] = arr[r];
      arr[r] = swap;
    },
  },
});
