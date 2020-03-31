<template>
  <div class="nav">
    <slot />
  </div>
</template>

<script>
export default {
  name: "Guide"
};
</script>

<style scoped>

.nav {
  margin-top: 0px;
  padding: 24px;
  text-align: center;
  font-family: Arial, Helvetica, sans-serif;
  /* box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.5); */
  background: #2d3436;
}
</style>