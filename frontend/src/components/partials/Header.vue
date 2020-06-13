<template>
  <section id="header">
   <slot></slot>
  </section>
</template>

<script>
export default {
  name: 'Header',
  props: {},
  mounted() {
      console.log('Header mounted!');
  }
}
</script>

<style scoped>
  section {
    width: 100%;
    padding: 5vw 25vw;
    background: #FFF;
    text-align: center;
    color: #666;
  }
  section > img { 
    margin: 30px 0 30px 0;
    border-radius: 4px;
  }
  section > h1 { font-size: 3rem; color: #C31; }
  section > h1 { font-size: 2.5rem; }
  section > p {
    margin-top: 30px;
    font-family: "Vollkorn", serif;
    font-size: 1.9rem;
    color: #666;
    text-align: justify;
    line-height: 3rem;
  }
</style>
