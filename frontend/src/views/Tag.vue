<template>
  <div>
    <h3>标签</h3>
    <div v-for="(item, index) in article" :key="index">
      <p @click="jump(item)">{{item.tag}}</p>
    </div>
  </div>
</template>

<script>
import { request } from "../network/request";
export default {
  name: "Tag",
  data() {
    return {
      article: "",
      id: ''
    };
  },
  created() {
    this.getTags();
  },
  methods: {
    getTags() {
      return request({
        url: "article"
      }).then(response => {
        this.article = response;
      });
    },
    jump(item) {
      var id = item.id.toString();
      var articlePath = "article/" + id;
      this.$router.push(articlePath);
    }
  }
};
</script>