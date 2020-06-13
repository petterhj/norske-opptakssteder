<template>
  <header>
   <nav>
    <router-link to="/">Norske opptakssteder</router-link>
    <span class="accent">▪</span>
    <router-link :to="{ name: 'productions'}">Produksjoner</router-link> |
    <router-link to="/bar">Steder</router-link> |
    <router-link to="/bar">Folk</router-link> |
    <router-link to="/bar">Kart</router-link>
   </nav>
  </header>
</template>

<script>
export default {
  name: 'Caption',
  props: {
    // msg: String
  }
}
</script>

<style scoped>
  header {
    overflow: auto;
    padding: 20px 25px;
    background: #FFF;
    font-family: "Unica One", Helvetica, Arial, sans-serif;
    font-size: 1.4rem;
    text-align: left;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    color: #333;
  }
  nav {
    width: 100%;
  }
  nav a, nav span {
    text-decoration: none;
    color: #999;
  }
  nav a:first-of-type {
    font-weight: bold;
  }
  nav a:first-of-type + span {
    margin: 0 5px;
  }
  nav a:hover:not(.icon) {
    background-color: #DDD;
  }
  /* nav a.right {
    float: right;
    margin-left: 10px;
  }
  nav i.zmdi {
    color: #999;
  }
  nav i.zmdi:hover {
    color: #C31;
    cursor: pointer;
  } */
</style>
