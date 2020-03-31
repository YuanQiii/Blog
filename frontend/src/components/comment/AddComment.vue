<template>
  <div id="AddComment">
    <div class="container">
      <div class="group">
        <input type="text" v-model="name" />
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>留下你的大名吧...</label>
      </div>
      <div class="group">
        <input type="text" v-model="comment" />
        <span class="highlight"></span>
        <span class="bar"></span>
        <label>留下你的足迹吧...</label>
      </div>
    </div>
    <div class="svg">
      <a class="button">
        <svg>
          <rect height="40" width="130" fill="transparent" />
        </svg>
        <span class="spot" @click="submit">留言</span>
      </a>
    </div>
  </div>
</template>

<script>
import { request } from "../../network/request";
import axios from "axios";
export default {
  name: "AddComment",
  data() {
    return {
      name: "",
      comment: ""
    };
  },
  methods: {
    submit() {
      if (this.name === "") {
        alert("昵称不能为空");
      } else if (this.comment === "") {
        alert("留言内容不能为空");
      } else {
        var obj = {};
        obj.name = this.name;
        obj.comment = this.comment;
        obj.createTime = Date.now();
        this.$emit("submit", obj);
        axios({
          method: "post",
          url: "http://127.0.0.1:8000/app01/api/comment",
          data: {
            name: this.name,
            comment: this.comment,
            createTime: Date.now()
          }
        });
        alert("感谢留言o(*￣▽￣*)o");
      }
    }
  }
};
</script>

<style scoped>
#AddComment {
  text-align: center;
}

/* * {
  box-sizing: border-box;
} */

.container {
  font-family: "Roboto";
  width: 320px;
  margin: 30px auto 0;
  display: block;
  background: transparent;
  margin: auto;
  padding: 50px 50px 20px;

}

/* form starting stylings ------------------------------- */
.group {
  position: relative;
  margin-bottom: 45px;
}
input {
  font-size: 18px;
  padding: 10px 10px 10px 5px;
  display: block;
  width: 300px;
  border: none;
  border-bottom: 1px solid #757575;
}
input:focus {
  outline: none;
}

/* LABEL ======================================= */
label {
  color: #999;
  font-size: 18px;
  font-weight: normal;
  position: absolute;
  pointer-events: none;
  left: 5px;
  top: 10px;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}

/* active state */
input:focus ~ label,
input:valid ~ label {
  top: -20px;
  font-size: 14px;
  color: #dfe6e9;
}

/* BOTTOM BARS ================================= */
.bar {
  position: relative;
  display: block;
  width: 300px;
}
.bar:before,
.bar:after {
  content: "";
  height: 2px;
  width: 0;
  bottom: 1px;
  position: absolute;
  background: #5264ae;
  transition: 0.2s ease all;
  -moz-transition: 0.2s ease all;
  -webkit-transition: 0.2s ease all;
}
.bar:before {
  left: 50%;
}
.bar:after {
  right: 50%;
}

/* active state */
input:focus ~ .bar:before,
input:focus ~ .bar:after {
  width: 50%;
}

/* HIGHLIGHTER ================================== */
.highlight {
  position: absolute;
  height: 60%;
  width: 100px;
  top: 25%;
  left: 0;
  pointer-events: none;
  opacity: 0.5;
}

/* active state */
input:focus ~ .highlight {
  -webkit-animation: inputHighlighter 0.3s ease;
  -moz-animation: inputHighlighter 0.3s ease;
  animation: inputHighlighter 0.3s ease;
}

/* ANIMATIONS ================ */
@-webkit-keyframes inputHighlighter {
  from {
    background: #2d3436;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@-moz-keyframes inputHighlighter {
  from {
    background: #2d3436;
  }
  to {
    width: 0;
    background: transparent;
  }
}
@keyframes inputHighlighter {
  from {
    background: #2d3436;
  }
  to {
    width: 0;
    background: transparent;
  }
}


/* ------------------------------------------ */


p {
    color: #ddd;
    font-family: Helvetica;
    font-size: 20px;
    margin: 20px 0 0 0;
}

a {
    color: #000;
    text-decoration: none;
    text-transform: uppercase;
    font-family: Helvetica;
}

a,
span {
    font-size: 20px;
}

svg {
    width: 130px;
    height: 40px;
}





/* THE SVG HOVER EFFECTS */
.svg .button {
    text-decoration: none;
    color: #dfe6e9;
    position: relative;
    display: inline-block;
    width: 130px;
    height: 40px;
    margin: 20px;
    overflow: hidden;
    margin-bottom: 140px;
}

.svg .button rect {
    position: absolute;
    top: 0;
    left: 0;
    stroke-width: 4px;
    stroke-dashoffset: 400px;
    stroke: #dfe6e9;
}

.svg .button span {
    color: #dfe6e9;
    width: 130px;
    height: 40px;
    display: inline-block;
    text-align: center;
    position: absolute;
    left: 0;
    top: 0;
    line-height: 40px;
    transition: all .2s linear;
}

.svg .button span:hover {
    color: #2d3436;
    background: #dfe6e9;
    transition: all 1s cubic-bezier(1.25s 0, 1.15, 1, 1);
    transition-delay: .5s;
}

.svg .button:nth-child(1):hover rect {
    animation: draw1 .75s linear forwards;
}

@keyframes draw1 {
    0% {
        stroke-dasharray: 300;
        stroke-dashoffset: 700;
        stroke-width: 4px;
    }
    75% {
        stroke-dasharray: 900;
        stroke-width: 1px;
    }
    100% {
        stroke-dasharray: 900;
        stroke-width: 1px;
    }
}

</style>
