<template>
  <div id="app">
    <WelcomePage />
    <router-view/>
  </div>
</template>

<script>
import WelcomePage from './components/WelcomePage.vue'

export default {
  name: 'App',
  components: {
    WelcomePage
  }
}
</script>

<style>
#app {
  font-family: Roboto, Montserrat, sans-serif;
}
</style>
