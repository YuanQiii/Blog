<template>
  <div id="nav">
    <guide>
      <guide-item path="/home">
        <a slot="item-text">主页</a>
      </guide-item>
      <guide-item path="/archives">
        <a slot="item-text">归档</a>
      </guide-item>
      <!-- <guide-item path="/tag">
        <a slot="item-text">标签</a>
      </guide-item> -->
      <guide-item path="/about">
        <a slot="item-text">关于</a>
      </guide-item>
      <guide-item path="/comment">
        <a slot="item-text">留言</a>
      </guide-item>
      <!-- <guide-item path="/chain">
        <a slot="item-text">友链</a>
      </guide-item> -->
    </guide>
  </div>
</template>

<script>
import Guide from "./Guide";
import GuideItem from "./GuideItem";
export default {
  name: "MainGuide",
  components: {
    Guide,
    GuideItem
  },
  data() {
    return {};
  }
};
</script>

<style scoped>
a {
  transition: 0.4s;
  color: #dfe6e9;
  font-size: 20px;
  text-decoration: none;
  padding: 0 10px;
  margin: 0 10px;
}

a:hover {
  background-color: #dfe6e9;
  color: #2d3436;
  padding: 24px 10px;
}

</style>
