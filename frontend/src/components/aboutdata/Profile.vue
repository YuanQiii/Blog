<template>
  <div class="mine">
    <div class="title">
      <p>关于我</p>
    </div>
    <div class="article">
      <p>姓名：袁湫</p>
      <p>职业：某大学大四学生</p>
      <p>住址：成都</p>
      <p>GitHub：<a href='https://github.com/YuanQiii'>https://github.com/YuanQiii</a></p>
      <p>QQ：934024048</p>
      <p>微信：18908077873</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "Profile"
};
</script>

<style scoped>
.mine {
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