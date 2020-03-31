<template>
  <div class="stack">
    <div class="title">
      <p>技术栈</p>
    </div>
    <div class="article">
      <p>
        前端：
        <a href="https://developer.mozilla.org/zh-CN/">HTML/CSS/JavaScript</a> --
        <a href="https://cn.vuejs.org/">Vue</a> --
        <a href="https://www.webpackjs.com/">webpack</a>
      </p>
      <p>
        后端：
        <a href="https://www.python.org/">Python</a> --
        <a href="https://www.django-rest-framework.org/">Django REST framework</a> --
        <a href="https://www.mysql.com/">MySQL</a>
      </p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Stack"
};
</script>

<style scoped>
.stack {
  margin: 0 auto;
  max-width: 860px;
  margin-bottom: 50px;
  background-color: #dfe6e9;
  text-align: left;
  border-radius: 10px;
  padding: 50px;
  padding-top: 30px;
}

.title {
  font-size: 2.5rem;
}
.article {
  font-size: 1.5rem;
}

a {
  transition: 0.4s;
  color: #2d3436;
  text-decoration: none;
}

a:hover {
  background-color: #2d3436;
  color: #dfe6e9;
  padding: 0.7rem;
}
</style>