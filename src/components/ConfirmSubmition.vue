<template>
  <div class="confirmation">
    <div
      @click="cancelClickHandler"
      class="confirmation__cancel">
      <div class="confirmation__icon_cancel"></div>
    </div>
    <div
      @click="confirmClickHandler"
      class="confirmation__apply">
      <div class="confirmation__icon_apply"></div>
    </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: "ConfirmSubmition",
  methods: {
    cancelClickHandler() {
      this.$emit('cancel')
    },
    confirmClickHandler() {
      this.$emit('confirm')
    }
  }
}
</script>

<style lang="stylus" scoped>
.confirmation
  display flex
  justify-content space-between
  align-items center
  position absolute
  width 100%
  height 80px
  background #42b983

  &__cancel
  &__apply
    height 80px
    width 80px
    padding 15px
    background-clip content-box

  &__icon_apply
  &__icon_cancel
    width 100%
    height 100%
    background url("../assets/delete.svg") no-repeat 50% 50%
    background-size contain


  &__icon_apply
    background url("../assets/tick.svg") no-repeat 50% 50%



</style>
