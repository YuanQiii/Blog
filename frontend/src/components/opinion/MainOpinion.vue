<template>
  <div>
    <add-opinion :articleid2='id' @submit='sub'/>
    <get-opinion :articleid2='id'/>
    <show-opinion :sendOpinions='opinions'/>
  </div>
</template>

<script>
import GetOpinion from '../opinion/GetOpinion'
import AddOpinion from '../opinion/AddOpinion'
import ShowOpinion from '../opinion/Showopinion'
export default {
  name: 'MainOpinion',
  props: {
    articleid1: {
      type: String
    }
  },
  data(){
    return {
      id: this.articleid1,
      opinions: []
    }
  },
  components: {
    GetOpinion,
    AddOpinion,
    ShowOpinion
  },
  methods: {
    sub(obj){
      this.opinions.push(obj)
    }
  }
}
</script>