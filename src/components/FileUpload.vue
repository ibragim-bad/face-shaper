<template>
  <div class="upload">
    <label
      for="the_file"
      class="upload__lable"
      >Upload</label>
    <input
      class="upload__file-input"
      @change="inputHandler"
      accept="image/*"
      type="file"
      name="the_file"
      id="the_file">
    <!-- <input hidden type="text" name="rotate" id="rotate" :value="rotateDeg"> -->
  </div>
</template>

<script>
import { mapGetters, mapActions} from 'vuex'
import { Promise } from 'q';
import { promises } from 'fs';
import rotateDetect from "../assets/rotateDetect"

export default {
  name: "FileUpload",
  data: () => ({
    photo: null,
  }),
  props: {
    disabled: {
      type: Boolean,
      default: false,
    }
  },
  computed: {
    ...mapGetters([
      'rotateDeg'
    ]),
    isPhotoLoaded() {
      return !!photo
    },
  },
  methods: {
    ...mapActions([
      'setPhoto',
      'setRotateDeg',
    ]),
    inputHandler({target}) {
      if (target.files.length) {
        const file = target.files[0];
        this.getDataURL(file)
          .then(response => {
            this.setPhoto(response);
          })
        rotateDetect(file, this.setRotateDeg)
      } else {
        this.setPhoto(null);
      }
    },
    getDataURL(file) {
      const reader = new FileReader()

      const promise =  new Promise((resolve, reject) => {
        reader.addEventListener('loadend', () => {
          resolve(reader.result)
        })
      })

      reader.readAsDataURL(file);

      return promise;
    }
  }

}
</script>

<style lang="stylus" scoped>
.upload
  &__lable
    display flex
    justify-content center
    align-items center
    width 100%
    height 80px
    background #42b983
    font-size 26px
    text-transform uppercase
    font-weight 700

  &__file-input
    position fixed
    bottom -100px
    visibility hidden


</style>
