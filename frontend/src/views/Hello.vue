<template>
  <div>
    <p>{{fullName}}</p>
  </div>
</template>

<script lang="ts">
import { request } from "../network/request";
export default {
  name: "Hello",
  data() {
    return {
      fullName: ""
    };
  },
  created() {
    this.getHello();
  },
  methods: {
    getHello() {
      return request({
        url: "hello"
      }).then(response => {
        this.fullName = response;
      });
    }
  }
};
</script> 