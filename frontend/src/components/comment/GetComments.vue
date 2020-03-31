<template>
  <div>
    <div v-for="(item, index) in comments" :key="index" class="get">
      <div class="name" >{{item.name}}</div>
      <div class="comment">{{item.comment}}</div>
      <hr>
      <div class="createTime">{{timeFormat(item.createTime)}}</div>
    </div>
  </div>
</template>

<script>
import { request } from "../../network/request";
import {dateFormat} from '../../utils/dateFormat'
export default {
  name: "GetComments",
  data() {
    return {
      comments: {},
    };
  },
  created() {
    this.getComments();
  },
  methods: {
    getComments() {
      return request({
        url: "getcomments"
      }).then(response => {
        this.comments = response;
        console.log(this.comments);
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