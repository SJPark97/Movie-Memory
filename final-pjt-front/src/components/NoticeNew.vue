<template>
  <div class="inside">
    <p v-if="!newNotice" class="no-notice">새 알림이 없습니다</p>
    <NoticeButton
      v-else
      v-for="notice in newNotice"
      :key="notice.id"
    />
  </div>
</template>

<script>
import NoticeButton from '@/components/NoticeButton'

export default {
  name: 'NoticeNew',
  components: {
    NoticeButton
  },
  props: {
    newNotice: Array,
  }
}
</script>

<style>
.inside {
  position: absolute;
  top: 70px;
  left: 0px;
  width: 280px;
  height: 355px;
  overflow: auto;
}

.inside::-webkit-scrollbar {
  display: none;
}

.no-notice{
  position: absolute;
  top: 50px;
  left: 80px;
}
</style>