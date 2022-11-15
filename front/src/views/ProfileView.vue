<template>
  <div>
    <!-- https://bootstrap-vue.org/docs/components/tabs -->
    <MyStorage/>
    <UpdateUserInfo/>
  </div>
</template>



<script>
import MyStorage from '@/components/MyStorage'
import UpdateUserInfo from '@/components/UpdateUserInfo'

export default {
  name: 'ProfileView',
  components: {
    MyStorage,
    UpdateUserInfo,
  }
}
</script>

<style>

</style>