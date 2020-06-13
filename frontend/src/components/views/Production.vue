<template>
 <div>
  <Header v-if="production.data">
   <img src="../../assets/oslo-31-august.jpg" class="poster" alt="poster">
   <h1>{{production.data.title}}</h1>
   <h2>{{production.data.year}}</h2>
   <h3>
    <a href="/person/joachim-trier/" title="Regi">Joachim Trier</a>
   </h3>
   <p>Oslo, 31. august er et portrett av Oslo i dag - inspirert av kultromanen «Le feu follet». Anders er i Oslo for å søke jobb og møte gamle venner. Han er rusfri etter seks år som narkoman og vandrer rundt i byen. Nå er det tid for å starte på nytt. Et visuelt og emosjonelt drama om en mann drevet til sitt eksistensielle nullpunkt. </p>
  </Header>
  <Grid v-if="production.data">
   Hallo
   <router-link :to="{ name: 'production', params: { slug: 'asdasd' }}">NESTE</router-link>
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
        // slug: this.$router.params.slug,
    }
  },
  chimera: {
    production () {
      return {
        url: '/productions/' + this.$route.params.slug,
        keepData: false,
        on: {
          error(e, d) {
            // console.log(e.error.status_code)
            // console.log(e.error.message)
            this.$router.replace({name: 'error', props: {
              status_code: e.error.status_code,
              message: e.error.message
            }});
          }
        }
      }
    }
  },
  created() {}
}
</script>

<style scoped>
  #header > img {
    width: 180px;
    height: 267px;
  }
</style>