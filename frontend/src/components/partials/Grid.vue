<template>
  <section id="content">
   <slot></slot>
  </section>
</template>

<script>
export default {
  name: 'Base',
  props: {},
  mounted() {
      console.log('Grid mounted!');
  }
}
</script>

<style scoped>
  section {
      margin: 5vw 10vw;
  }
</style>
