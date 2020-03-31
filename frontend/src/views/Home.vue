<template>
  <div>
    <!-- <welcome></welcome> -->
    <div class="wel">
      <welcome1/>
    </div>
     <div>
        <title-list />
      </div>
  </div>
</template>

<script>
import TitleList from "../components/TitleList";
import Welcome from '../components/Welcome'
import Welcome1 from '../components/guide/Welcome1'
export default {
  name: "Home",
  components: {
    TitleList,
    Welcome,
    Welcome1
  }
};
</script>

<style scoped>

/* .welcome {
  color: #333;
  font-family: Helvetica;
  margin: 0;
  padding: 0;
  font-size: 8rem;
  letter-spacing: -0.3rem;
  position: relative;

}

.welcome::after {
  content: "Welcome YuanQiii's Blog";
  color: yellow;
  position: absolute;
  top: 0;
  left: 0;
  -webkit-clip-path: ellipse(100px, 100px, at 50% 50%);
  clip-path: ellipse(100px, 100px, at 0% 50%);


}

.wel {
  background-color: #222;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
} */
</style>