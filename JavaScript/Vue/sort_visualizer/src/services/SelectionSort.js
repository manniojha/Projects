import Vue from "vue";

export default new Vue({
  methods: {
    run(arr) {
      let counter = 0;
      let index = 0;
      arr = [...arr];
      while (index != arr.length) {
        let minValue = arr[index];
        let innerTempIndex = index;
        for (let i = index; i < arr.length; i++) {
          if (arr[i] < minValue) {
            minValue = arr[i];
            innerTempIndex = i;
          }
        }
        if (innerTempIndex != index) {
          let temp = arr[index];
          arr[index] = minValue;
          arr[innerTempIndex] = temp;

          this.$emit("onItemSwap", {
            left: {
              index: index,
              value: arr[index],
            },
            right: {
              index: innerTempIndex,
              value: arr[innerTempIndex],
            },
            counter: counter++,
          });
        }
        index++;
      }
    },
  },
});
