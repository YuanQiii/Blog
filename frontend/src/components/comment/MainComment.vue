<template>
  <div id="article">
    <div class="content">
      <h3 class="title">留言板</h3>
      <div>
        <add-comment @submit="sub"/>
        <get-comments />
        <show-comment :sendComments="comments" />
      </div>
    </div>
  </div>
</template>

<script>
import AddComment from "./AddComment";
import ShowComment from "./ShowComment";
import GetComments from "./GetComments";
export default {
  name: "MainComment",
  components: {
    AddComment,
    ShowComment,
    GetComments
  },
  data() {
    return {
      comments: [],
    };
  },
  methods: {
    sub(obj) {
      this.comments.push(obj);
    }
  }
};
</script>

<style scoped>
.title {
  text-align: center;
  font-size: 3rem;
  color: #dfe6e9;
}
</style>