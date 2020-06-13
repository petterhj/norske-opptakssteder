<template>
  <div id="app">
    <Caption />
    <router-view></router-view>
  </div>
</template>

<script>
import Caption from './components/partials/Caption.vue'

export default {
  name: 'app',
  components: { Caption },
  mounted () {
    //
  }
}
</script>

<style>
  @font-face {
    font-family: 'Monda';
    font-style: normal;
    font-weight: normal;
    src:
      local('Monda Regular'),
      local('Monda-Regular'),
      /* from https://fonts.gstatic.com/s/monda/v8/TK3tWkYFABsmjsphPho.woff2 */
      url('./assets/fonts/Monda.woff2') format('woff2'),
      /* from https://fonts.gstatic.com/s/monda/v8/TK3tWkYFABsmjsphPhw.woff */
      url('./assets/fonts/Monda.woff') format('woff'),
      /* from https://fonts.gstatic.com/s/monda/v8/TK3tWkYFABsmjsphPh4.eot */
      url('./assets/fonts/Monda.eot?#iefix') format('embedded-opentype'),
      /* from https://fonts.gstatic.com/l/font?kit=TK3tWkYFABsmjsphPh0&skey=12b74b97e719c11d&v=v8#Monda */
      url('./assets/fonts/Monda.svg#Monda') format('svg'),
      /* from https://fonts.gstatic.com/s/monda/v8/TK3tWkYFABsmjsphPh8.ttf */
      url('./assets/fonts/Monda.ttf') format('truetype');
  }
  @font-face {
    font-family: 'Unica One';
    font-style: normal;
    font-weight: normal;
    src:
      local('Unica One'),
      local('UnicaOne-Regular'),
      /* from https://fonts.gstatic.com/s/unicaone/v6/DPEuYwWHyAYGVTSmalsRcd3e.woff2 */
      url('./assets/fonts/Unica_One.woff2') format('woff2'),
      /* from https://fonts.gstatic.com/s/unicaone/v6/DPEuYwWHyAYGVTSmalsRcd3Y.woff */
      url('./assets/fonts/Unica_One.woff') format('woff'),
      /* from https://fonts.gstatic.com/s/unicaone/v6/DPEuYwWHyAYGVTSmalsRcd3a.eot */
      url('./assets/fonts/Unica_One.eot?#iefix') format('embedded-opentype'),
      /* from https://fonts.gstatic.com/l/font?kit=DPEuYwWHyAYGVTSmalsRcd3Z&skey=95c90eaca39f67c7&v=v6#UnicaOne */
      url('./assets/fonts/Unica_One.svg#UnicaOne') format('svg'),
      /* from https://fonts.gstatic.com/s/unicaone/v6/DPEuYwWHyAYGVTSmalsRcd3b.ttf */
      url('./assets/fonts/Unica_One.ttf') format('truetype');
  }
  @font-face {
    font-family: 'Noto Serif';
    font-style: normal;
    font-weight: normal;
    src:
      local('Noto Serif'),
      local('NotoSerif'),
      /* from https://fonts.gstatic.com/s/notoserif/v6/ga6Iaw1J5X9T9RW6j9bNfFcWaA.woff2 */
      url('./assets/fonts/Noto_Serif.woff2') format('woff2'),
      /* from https://fonts.gstatic.com/s/notoserif/v6/ga6Iaw1J5X9T9RW6j9bNfFcWbg.woff */
      url('./assets/fonts/Noto_Serif.woff') format('woff'),
      /* from https://fonts.gstatic.com/s/notoserif/v6/ga6Iaw1J5X9T9RW6j9bNfFcWbA.eot */
      url('./assets/fonts/Noto_Serif.eot?#iefix') format('embedded-opentype'),
      /* from https://fonts.gstatic.com/l/font?kit=ga6Iaw1J5X9T9RW6j9bNfFcWbw&skey=ff3f102bd67fc93c&v=v6#NotoSerif */
      url('./assets/fonts/Noto_Serif.svg#NotoSerif') format('svg'),
      /* from https://fonts.gstatic.com/s/notoserif/v6/ga6Iaw1J5X9T9RW6j9bNfFcWbQ.ttf */
      url('./assets/fonts/Noto_Serif.ttf') format('truetype');
  }
  @font-face {
    font-family: 'Vollkorn';
    font-style: normal;
    font-weight: normal;
    src:
      local('Vollkorn Regular'),
      local('Vollkorn-Regular'),
      /* from https://fonts.gstatic.com/s/vollkorn/v8/0yb9GDoxxrvAnPhYGxkpaE0.woff2 */
      url('./assets/fonts/Vollkorn.woff2') format('woff2'),
      /* from https://fonts.gstatic.com/s/vollkorn/v8/0yb9GDoxxrvAnPhYGxkpaEs.woff */
      url('./assets/fonts/Vollkorn.woff') format('woff'),
      /* from https://fonts.gstatic.com/s/vollkorn/v8/0yb9GDoxxrvAnPhYGxkpaEk.eot */
      url('./assets/fonts/Vollkorn.eot?#iefix') format('embedded-opentype'),
      /* from https://fonts.gstatic.com/l/font?kit=0yb9GDoxxrvAnPhYGxkpaEo&skey=70793812edfff824&v=v8#Vollkorn */
      url('./assets/fonts/Vollkorn.svg#Vollkorn') format('svg'),
      /* from https://fonts.gstatic.com/s/vollkorn/v8/0yb9GDoxxrvAnPhYGxkpaEg.ttf */
      url('./assets/fonts/Vollkorn.ttf') format('truetype');
  }

  * { box-sizing: border-box; }

  html, body, #app {
    height: 100%;
    margin: 0;
    /* overflow-x: hidden; */
    font-size: 62.5%;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    background: #1A1919;
  }
  #app {
    font-size: 1.4rem;
    color: #FFF;
  }
  #app > div {
    height: calc(100% - 57px);
  }
  

  h1, h2, h3, h4, h5, h6 {
    font-family: "Unica One", Helvetica, Arial, sans-serif;
    font-weight: normal;
    text-transform: uppercase;
  }
  h1 a, h2 a, h3 a, h4 a {
    color: inherit;
    text-decoration: none;
  }
  h1 a:hover, h2 a:hover, h3 a:hover, h4 a:hover {
    text-decoration: underline;
  }

  .accent {
    color: #C31 !important;
  }
</style>
