<template>
  <div>
    <div id="wrapper">
      <article-list :articleid="id" />
      <catalog :articleid="id" class="side"/>
    </div>
  </div>
</template>

<script>
import ArticleList from "../components/article/ArticleList";
import Catalog from "../components/article/Catalog";
export default {
  name: "Article",
  components: {
    ArticleList,
    Catalog
  },
  data() {
    return {
      id: null
    };
  },
  created() {
    this.id = this.$route.params.id;
    console.log(this.id);
  },
  methods: {}
};
</script>

<style scoped>

</style>