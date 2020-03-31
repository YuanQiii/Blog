<template>
  <div class="timeline">
    <div class="ull">
      <div v-for="(item, index) in archives" :key="index" class="lii">
        <h3>{{item.title}}</h3>
        <p>{{item.content}}</p>
        <time>{{timeFormat(item.createTime)}}</time>
      </div>
    </div>
  </div>
</template>

<script>
import { request } from "../network/request";
import {dateFormat} from '../utils/dateFormat'
export default {
  name: "Archives",
  data() {
    return {
      archives: {}
    };
  },
  created() {
    this;
    this.getArchives();
  },
  methods: {
    getArchives() {
      return request({
        url: "getarchives"
      }).then(response => {
        this.archives = response;
      });
    },
    timeFormat(time){
      return dateFormat(time)
    }
  }
};
</script>

<style lang="scss" scoped>


$gray: #dddddd;

.container {
  padding: 1em;
}

.timeline {
  position: relative;
  overflow: auto;
  
  &:before {
    content: '';
    position: absolute;
    height: 100%;
    width: 5px;
    background: #dfe6e9;
    left: 0;
  }
  
  .ull {
    list-style: none;
    padding: 0 0 0 1em;
    z-index: 1;
  }
  
  .lii {
    background: #dfe6e9;
    padding: 1em;
    margin-bottom: 1em;
    position: relative;
    
    &:before {
      content: '';
      width: 0;
      height: 0;
      border-top: 1em solid #dfe6e9;
      border-left: 1em solid transparent;
      position: absolute;
      left: -1em;
      top: 0;
    }
  }
  
  h3 {
    margin-top: 0;
  }
  
  time {
    font-style: italic;
  }
}

@media screen and (min-width: 40em) {
  .container {
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .timeline {
    &:before {
      left: 50%;
    }
    
    .ull {
      padding-left: 0;
      max-width: 700px;
      margin: 0 auto;
    }
    
    .lii {
      width: 42%;
    }
    
    .lii:nth-child(even) {
      float: right;
      margin-top: 2em;
    }
    
    .lii:nth-child(odd) {
      float: left;
      
      &:before {
        border-top: 1em solid #dfe6e9;
        border-right: 1em solid transparent;
        right: -1em;
        left: auto;
      }
    }
    
    .lii:nth-of-type(2n+1) {
      clear: both;
    }
  }
}
</style>