<template>
 <div>
  <section id="cover">
   <img src="../../assets/error-page-bg.jpg" alt="error-background">
   <div class="heading">
    <h1>
     <template v-if="message">{{message}}</template>
     <template v-else>Heisann! Her manglet det noe</template> 
     <span class="code"> — {{status_code}}</span>
    </h1>
    <h2>Du venner deg til det.</h2>
   </div>
   <div class="caption">
    <h1><a href="https://www.imdb.com/title/tt0808185/">Den brysomme mannen</a> (2006)</h1>
    <h2>Nydalen stasjon, Nydalen, Oslo</h2>
   </div>
  </section>
 </div>
</template>

<script>
export default {
  components: {  },
  props: ['status_code', 'message'],
  data() {
    return {  }
  }
}
</script>

<style scoped>
 section#cover {
    position: relative;
    padding: 0 20px 20px 20px;
    background: #FFF;
    height: 100%;
 } 
 section#cover > img { 
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center center;
 }
 section#cover > div.heading {
   position: absolute;
   top: 20px;
   left: 40px;
 }
 section#cover > div.heading > h1 {
   margin: 0; font-size: 2.5rem;
 }
 section#cover > div.heading > h2 {
   margin-top: 10px;
   font-size: 1.5rem;
   color: rgba(255, 255, 255, 0.75);
 }

 section#cover > div.caption {
   position: absolute;
   bottom: 20px;
   left: 40px;
   width: auto;
   text-align: left;
   color: #FFF;
   opacity: 0.7;
 }
 section#cover > div.caption > h1 {
   margin: 0;
   font-size: 1.5rem;
 }
 section#cover > div.caption > h2 {
   margin: 5px 0 20px 0;
   font-size: 1rem;
 }
 
 span.code { opacity: 0.7; }
</style>