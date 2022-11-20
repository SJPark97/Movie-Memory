<template>
  <div>
    <p>{{ comment.content }}</p>
    <span>{{ comment.username }}</span>
    <span>{{ comment.created_at.substr(0, 10) }}</span>
    <span @click="likeUnlike">
      <font-awesome-icon icon="fa-solid fa-heart" v-show="is_liked"/>
      <font-awesome-icon icon="fa-regular fa-heart"  v-show="!is_liked"/>
    </span>
    {{ like_users_count }}
  </div>
</template>

<script>
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'CommentCard',
  props: {
    comment: Object,
  },
  data() {
    return {
      is_liked: null,
      like_users_count: 0,
    }
  },
  methods: {
    getCommentLike(comment_id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/comments/${comment_id}/likes/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.is_liked = response.data.is_liked
          this.like_users_count = response.data.like_users_count
        })
        .catch((error) => {
          console.log(error)
        })
      },
    likeUnlike() {
      this.getCommentLike(this.comment.id)
    }
  },
  created() {
    this.getCommentLike(this.comment.id)
  }
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
}

p {
  font-size: medium;
  margin-bottom: 3px;
  margin-left:8px;
}

span {
  margin-left:8px;
}
</style>