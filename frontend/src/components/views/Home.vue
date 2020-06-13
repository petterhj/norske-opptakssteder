<template>
 <div>
  <Header>
    <h1>Norske opptakssteder</h1>
  </Header>
  <Grid>
    <h1 v-for="prod in productions.data" :key="prod.title">{{prod.title}} ({{prod.year}})</h1>
  </Grid>
 </div>
</template>

<script>
import Header from '../partials/Header.vue'
import Grid from '../partials/Grid.vue'

export default {
  components: { Header, Grid },
  data() {
    return {
    }
  },
  chimera: {
    productions () {
      return {
        url: '/productions'
      }
    }
  }
}
</script>

<style scoped>
  #header {
    background-image: url(../.././assets/landing-header.jpg);
    background-repeat: no-repeat;
    background-position: 0 80%;
    background-size: cover;
    padding: 1vw 5vw;
  }
  #header > h1 {
    width: 150px;
    font-size: 5rem;
    color: #FFF;
    border-bottom: 2px solid #FFF;
  }
</style>