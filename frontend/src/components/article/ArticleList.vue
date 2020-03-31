<template>
  <div>
    <span>
      <div class="article" v-for="(item, index) in article" :key="index">
        <h1 :id="'T'+index" class="title">{{item.title}}</h1>
        <p class="tag">
          <img src="../../assets/img/tag.svg" alt />
          {{item.tag}}
        </p>

        <div class="info">
          <span class="time">最后编辑于：{{timeFormat(item.createTime)}}</span><p></p>    
          <span class="count">阅读量：{{AticleCount}}</span>
        </div>
      </div>

      <div class="article" v-for="(item, index) in contents" :key="index">
        <h2 :id="'S'+index" class="subtitle">{{item.sub_title}}</h2>
        <div class="content">{{item.content}}</div>
      </div>
    </span>

    <div id="opinion">
      <main-opinion :articleid1="id" />
    </div>

    <div id='button'>
      <img src="../../assets/img/backtotop.svg" alt="">
    </div>
  </div>
</template>

<script>
import { request } from "../../network/request";
import { dateFormat } from "../../utils/dateFormat";
import MainOpinion from "../opinion/MainOpinion";
import axios from "axios";
export default {
  name: "ArticleList",
  components: {
    MainOpinion
  },
  props: {
    articleid: {
      type: String
    }
  },
  data() {
    return {
      contents: {},
      article: {},
      AticleCount: 0,
      id: this.articleid
    };
  },
  created() {
    this.getArticleContent(this.id);
    this.getArticle(this.id);
  },
  mounted() {
    this.backTop();
  },
  beforeDestroy() {
    this.postCount(this.id);
  },
  methods: {
    getArticleContent(id) {
      return request({
        url: "content/" + id
      }).then(response => {
        this.contents = response;
      });
    },
    getArticle(id) {
      return request({
        url: "article/" + id
      }).then(response => {
        this.article = response;
        this.AticleCount = response[0].count + 1;
      });
    },
    postCount(id) {
      axios({
        method: "put",
        url: "http://127.0.0.1:8000/app01/api/count/" + id,
        data: {
          count: this.AticleCount
        }
      });
    },
    timeFormat(time) {
      return dateFormat(time);
    },
    backTop() {
      var btn = $("#button");

      $(window).scroll(function() {
        if ($(window).scrollTop() > 300) {
          btn.addClass("show");
        } else {
          btn.removeClass("show");
        }
      });

      btn.on("click", function(e) {
        e.preventDefault();
        $("html, body").animate({ scrollTop: 0 }, "300");
      });
    }
  }
};
</script>

<style scoped>
.tag img {
  width: 22px;
}

.tag {
  font-size: 1.3rem;
}

.article {
  margin: 0 auto;
  max-width: 860px;
  margin-bottom: 50px;
  background-color: #dfe6e9;
  text-align: left;
  border-radius: 10px;
  padding: 50px;
}

.info {
  display: table;
}

.count .time {
  display: table-cell;
}

.title {
  font-size: 2.5rem;
}

.subtitle {
  font-size: 2rem;
}

.article {
  font-size: 1.5rem;
}

.time {
  font-size: 1.3rem;
  text-align: right;
}

.count {
  font-size: 1.3rem;
}

#button {
  position: fixed;
  bottom: 30px;
  right: 30px;
  transition: background-color 0.3s, opacity 0.5s, visibility 0.5s;
  opacity: 0;
  visibility: hidden;
  z-index: 1000;
}
#button.show {
  opacity: 1;
  visibility: visible;
}
</style>