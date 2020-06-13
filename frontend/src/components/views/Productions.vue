<template>
 <div>
  <Grid>
   <h1 v-for="prod in productions.data" :key="prod.title">
    <router-link :to="{ name: 'production', params: { slug: prod.slug }}">
     {{prod.title}} ({{prod.year}}) ({{prod.slug}})
    </router-link>
   </h1>
  </Grid>
 </div>
</template>

<script>
import Grid from '../partials/Grid.vue'

export default {
  components: { Grid },
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

</style>