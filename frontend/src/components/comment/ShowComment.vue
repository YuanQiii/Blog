<template>
  <div >
    <div v-for="(item, index) in showComments" :key="index" class="show">
      <div class="name">{{item.name}}</div>
      <div class="comment">{{item.comment}}</div>
      <div class="createTime">{{timeFormat(item.createTime)}}</div>
    </div>
  </div>
</template>

<script>
import {dateFormat} from '../../utils/dateFormat'
export default {
  name: "ShowComment",
  props: {
    sendComments: {
      type: Array
    }     
  },
  data() {
    return {
      showComments: this.sendComments 
    };
  },
  methods: {
    timeFormat(time){
      return dateFormat(time)
    }
  }
};
</script>

<style scoped>
.show {
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