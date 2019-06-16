<template>
  <div class="home">
    <ConfirmSubmition
      v-show="isPhoto"
      @cancel="cancelHandler"
      @confirm="confirmHandler"
    />
    <h1
      v-show="!isPhoto && !isSuggestion"
      class="home__greeteng">Choose<br>Your<br>Shades</h1>
    <div class="home__info">
      <h2 class="home__loading" v-show="loading">Loading...</h2>
      <h2 class="home__error" v-show="error">There is an error</h2>
      <div class="home__suggestion" v-if="suggestion">
        <h3 class="home__face-shape">Face shape - {{ suggestion.shape }}</h3>
      </div>
    </div>
    <div class="home__photo">
      <div
        :style="rotatePreview + bgImage"
        class="home__preview"></div>
    </div>
    <form ref="form">
      <FileUpload
        :disabled="isPhoto"
        class="home__file-upload"
      />
    </form>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

import ConfirmSubmition from '@/components/ConfirmSubmition.vue'
import FileUpload from '@/components/FileUpload.vue'

export default {
  name: 'home',
  components: {
    FileUpload,
    ConfirmSubmition,
  },
  computed: {
    ...mapGetters([
      'isPhoto',
      'photo',
      'loading',
      'suggestion',
      'isSuggestion',
      'error',
      'rotateDeg',
    ]),
    bgImage() {
      return `background-image: url('${this.photo || (this.suggestion && this.suggestion.path)}');`
    },
    errorText() {
      return this.error && JSON.stringify(this.error)
    },
    rotatePreview() {
      return `transform: rotate(${this.rotateDeg}deg);`
    }
  },
  methods: {
    ...mapActions([
      'setPhoto',
      'sendPhoto',
      'setSuggestion',
    ]),
    clearPhoto() {
      this.setPhoto(null)
    },
    clearSuggestion() {
      this.setSuggestion(null)
    },
    cancelHandler() {
      this.clearPhoto()
      this.$refs.form.reset()
    },
    confirmHandler() {
      if (this.loading) {
        return
      }
      this.sendPhoto(new FormData(this.$refs.form))
      this.clearSuggestion()
      this.$refs.form.reset()
    }
  }
}
</script>

<style lang="stylus" scoped>
.home

  &__file-upload
    position absolute
    left 0
    bottom 0
    width 100%

  &__photo
    width 100%
    height 100%
    padding-top 80px
    padding-bottom 80px

  &__preview
    background-position 50% 50%
    background-repeat no-repeat
    background-size contain
    width 100%
    height 100%

  &__info
    z-index 50
    position absolute
    bottom 80px
    left 50%
    transform translateX(-50%)
    display flex
    flex-direction column
    align-items center
    justify-content center

  &__error
    color red

  &__loading
    color black

  &__greeteng
    position absolute
    top 40%
    left 50%
    transform translate(-50%, -50%)
    line-height 1.44
    text-transform uppercase
    font-size 40px
    font-weight bold
</style>

