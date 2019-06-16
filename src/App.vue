<template>
  <div id="app">
    <div
      v-show="!isPhoto"
      id="nav">
      <template
          v-if="$route.path !== '/'"
          >
        <router-link
          to="/"
          >Home</router-link> |
      </template>
      <router-link to="/about">About</router-link>
    </div>
    <router-view
      class="app-view"
    />
  </div>
</template>
<script>
import { mapGetters } from 'vuex'

export default {
  name: "app",
  computed: {
    ...mapGetters([
      'isPhoto'
    ]),
  }
}
</script>


<style lang="stylus">
*
  box-sizing border-box

  &::after
  &::before
    box-sizing inherit

body
  margin 0
  padding 0

#app
  position fixed
  top 0
  bottom 0
  left 0
  right 0
  font-family 'Avenir', Helvetica, Arial, sans-serif
  -webkit-font-smoothing antialiased
  -moz-osx-font-smoothing grayscale
  text-align center
  color #2c3e50

.app-view
  margin 0 auto
  max-width 400px
  position fixed
  top 0
  bottom 0
  left 0
  right 0

.app__confirmation
  z-index 100

#nav
  z-index 100
  position absolute
  left 0
  top 0
  display flex
  align-items center
  justify-content center
  width 100%
  height 80px
  padding 30px
  background #42b983

  a
    font-weight bold
    color #2c3e50
    &.router-link-exact-active
      color #ff0000
</style>
