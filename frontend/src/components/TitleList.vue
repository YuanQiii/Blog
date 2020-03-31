<template>
  <div>
    <div class="list"></div>
    <div class="TitleList" v-for="(item, index) in article" :key="index">
      <div class="title" @click="jump(item)">{{item.title}}</div>
      <div class="desc">{{item.description}}</div>
      <hr />
      <div class="info">
              <span class="tag">
        <img src="../assets/img/tag.svg" alt />
        {{item.tag}}
      </span>
      <span class="time">
        <img src="../assets/img/calendar.svg" alt />
        {{timeFormat(item.createTime)}}
      </span>
      </div>

    </div>
  </div>
</template>

<script>
import { request } from "../network/request";
import { dateFormat } from "../utils/dateFormat";
export default {
  name: "TitleList",
  data() {
    return {
      article: {}
    };
  },

  created() {
    this.getArtciles();
  },
  methods: {
    getArtciles() {
      return request({
        url: "article"
      }).then(response => {
        this.article = response;
      });
    },
    jump(item) {
      var id = item.id.toString();
      var articlePath = "content/" + id;
      this.$router.push(articlePath);
    },
    timeFormat(time) {
      return dateFormat(time);
    }
  }
};
</script>

<style scoped>

.list {
  margin: 0 auto;
  margin-bottom: 50px;
  background-color: transparent;
  padding: 50px;
}
.TitleList {
  margin: 0 auto;
  max-width: 860px;
  margin-bottom: 50px;
  background-color: #dfe6e9;
  text-align: left;
  border-radius: 10px;
  padding: 50px;
}

span img {
  width: 15px;
}

.time {
  margin-left: 20px;
}

.info {
  text-align: right;
}

.title {
  font-size: 2.5rem;
  transition: 0.4s;
  color: #2d3436;
  /* font-size: 20px; */
  text-decoration: none;
  /* padding: 0 10px;
  margin: 0 10px; */
}

.title:hover {
  background-color: #2d3436;
  color: #dfe6e9;
  padding: 0.7rem;
}

.desc {
  margin-top: 30px;
  font-size: 1.5rem;
}
</style>