<template>
  <div>
    <input type="checkbox" id="menu" name="menu" class="menu-checkbox" />
    <div class="menu">
      <label class="menu-toggle" for="menu">
        <span>Toggle</span>
      </label>
      <ul>
        <p class="first">目录</p>
        <li v-for="(item, index) in logoArticle" :key="index" class="maintitle" style="list-style: none"> 
          <a class="title" @click="titleScroll(index)">{{item.title}}</a>
        </li>
        <li v-for="(item, index) in logoContent" :key="index" class="subtitle" style="list-style: none">
          <a @click="subTitleScroll(index)">{{item.sub_title}}</a>
        </li>
        <p @click="opinionScroll"  class="opinion">评论区</p>
      </ul>
    </div>
  </div>
</template>

<script>
import { request } from "../../network/request";
export default {
  name: "Catalog",
  props: {
    articleid: {
      type: String
    }
  },
  data() {
    return {
      logoArticle: [],
      logoContent: [],
      id: this.articleid
    };
  },
  created() {
    this.getArticle(this.id), this.getArticleContent(this.id);
  },
  methods: {
    getArticleContent(id) {
      return request({
        url: "content/" + id
      }).then(response => {
        this.logoContent = response;
        // this.$emit('sendArticleContent', this.contents)
      });
    },
    getArticle(id) {
      return request({
        url: "article/" + id
      }).then(response => {
        this.logoArticle = response;
        // this.$emit('sendArticle', this.article)
      });
    },
    titleScroll(index){
      document.getElementById('T'+index).scrollIntoView()
    },
    subTitleScroll(index){
      document.getElementById('S'+index).scrollIntoView()
    },
    opinionScroll(){
      document.getElementById('opinion').scrollIntoView()
    }
  }
};
</script>

<style lang="sass" scoped>

.first
  font-size: 2.2rem
  margin-left: 18px

.opinion
  font-size: 2.2rem
  margin-left: 18px

.opinion:hover 
  color: #2d3436
  background-color: #2d3436;
  color: #dfe6e9;
  transition: 0.4s;

.opinion 
  font-size: 2.2rem
  margin-left: 18px

label
  cursor: pointer
  &:focus
    outline: none
    
.menu
  position: fixed
  top: 0
  left: 0
  background: #dfe6e9
  width: 200px
  height: 100%
  transform: translate3d(-200px, 0, 0)
  transition: transform 0.35s
      
  label.menu-toggle  
    position: absolute    
    right: -60px
    width: 60px
    height: 75px
    line-height: 0px    
    display: block
    padding: 0
    text-indent: -9999px
    background: #2d3436 url(https://cdn1.iconfinder.com/data/icons/office-292/128/_Hamburger_menu_options_-512.png) 50% 50% / 25px 25px no-repeat
    
  
  ul
    li
      > label
        background: url(https://cdn4.iconfinder.com/data/icons/ionicons/512/icon-arrow-right-b-128.png) 95% 50% / 16px 16px no-repeat
      a, label
        display: block
        text-align: left
        padding: 0 20px
        line-height: 60px
        margin-right: 0px
        text-decoration: none
        color: #2d3436
        font-size: 1rem
        &:hover
          color: #2d3436
          background-color: #2d3436;
          color: #dfe6e9;
          transition: 0.4s;

/* hide inputs */          
.menu-checkbox
  display: none

/* hide navigation icon for sublabels */    
.menu .menu label.menu-toggle
  background: none
    
/* fade in checked menu */    
.menu-checkbox:checked + .menu
  transform: translate3d(0, 0, 0)
p
  margin-bottom: 15px
</style>