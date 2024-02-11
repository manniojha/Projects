import Vue from "vue";

export default new Vue({
  methods: {
    run(arr) {
      let counter = 0;
      arr = [...arr];
      let n = arr.length - 1;
      for (let i = 0; i < n; i++) {
        for (let j = 0; j < n - i; j++) {
          if (arr[j] > arr[j + 1]) {
            counter++;
            let temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
            this.$emit("onItemSwap", {
              index: j + 1,
              arr: [...arr],
              counter,
            });
          }
        }
      }
    },
  },
});
