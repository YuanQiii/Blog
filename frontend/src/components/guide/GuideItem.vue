<template>
  <div class="guide-item" @click="itemClick">
    <slot name="item-text" />
  </div>
</template>

<script>
export default {
  name: "GuideItem",
  props: {
    path: String
  },
  methods: {
    itemClick() {
      this.$router.push(this.path);
    }
  }
};
</script>

<style scoped>
.guide-item {
  display: inline-block
}
</style>