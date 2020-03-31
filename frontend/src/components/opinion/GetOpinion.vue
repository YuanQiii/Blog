<template>
  <div>
    <div v-for="(item, index) in opinions" :key="index" class="get">
      <div class="name" >{{item.name}}</div>
      <div class="comment">{{item.content}}</div>
      <hr>
      <div class="createTime">{{timeFormat(item.createTime)}}</div>
    </div>
  </div>
</template>

<script>
import { request } from "../../network/request";
import {dateFormat} from '../../utils/dateFormat'
export default {
  name: "GetOpinions",
  props: {
    articleid2: {
      type: String
    }
  },
  data() {
    return {
      opinions: {},
      id: this.articleid2
    };
  },
  created() {
    this.getOpinions(this.id);
  },
  methods: {
    getOpinions(id) {
      return request({
        url: "opinion/" + id
      }).then(response => {
        this.opinions = response;
        console.log(this.opinions);
      });
    },
    timeFormat(time){
      return dateFormat(time)
    }
  }
};
</script>

<style scoped>
.get {
  margin: 0 auto;
  max-width: 860px;
  margin-bottom: 50px;
  background-color: #dfe6e9;
  text-align: left;
  border-radius: 10px;
  padding: 50px;
}

.name {
  font-size: 2.5rem;
}

.comment {
    margin-top: 30px;
  font-size: 1.5rem;
}

.createTime {
   text-align: right;
}

</style>