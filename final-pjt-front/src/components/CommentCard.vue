<template>
  <div>
    <div class="content">
      <p>{{ comment.content }}</p>
      <span>{{ comment.username }}</span>
      <span>{{ comment.created_at.substr(0, 10) }}</span>
      <span @click="likeUnlike">
        <font-awesome-icon icon="fa-solid fa-heart" v-show="is_liked"/>
        <font-awesome-icon icon="fa-regular fa-heart"  v-show="!is_liked"/>
        {{ like_users_count }}
      </span>
    </div>

      <div @click="popSelector" class="dot">
        <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
        <div v-show="selector" class="pop">
          <p @click="changeComment">수정</p>
          <p @click="deleteComment(comment.id)">삭제</p>
        </div>
      </div>

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
  computed: {
    is_liked() {
      if (this.comment.like_users.indexOf(this.$store.state.userId) === -1) {
        return false
      } else {
        return true
      }
    },
    like_users_count() {
      return this.comment.like_users.length
    },
  },
  data() {
    return {
      selector: false,
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
          this.$emit('change-comments')
        })
        .catch((error) => {
          console.log(error)
        })
      },
    likeUnlike() {
      this.getCommentLike(this.comment.id)
    },
    popSelector() {
      if (! this.selector) {
        this.selector = true
      } else { 
        this.selector = false
      }
    },
    deleteComment(comment_id) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/comments/${comment_id}/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.$emit('change-comments')
        })
        .catch((error) => {
          console.log(error)
        })
    },
    changeComment() {

    }
  },
}
</script>

<style scoped>
div {
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

p {
  font-size: medium;
  margin-bottom: 3px;
  margin-left:8px;
}

span {
  margin-left:8px;
  margin-right: 15px;
}

.content {
  display: inline-block;
}

.content > p {
  font-size: 20px;
  margin-top: 7px;
  margin-bottom: 7px;
}
.dot {
  display: inline-block;
  margin-right: 15px;
  font-size: 20px;
  background-color: transparent;
  border: none;
  color: black;
  position: relative;
}

.dot:hover {
  background-color: transparent;
}

/* .dot {
  background-color: transparent;
} */

.pop {
  display: inline-block;
  position: absolute;
  z-index: 999;
  background-color: rgb(218, 210, 210);
  border-radius: 10px;
  top: 8px;
  left: -50px;
  width: 50px;
  text-align: center;
}

.pop > p {
  margin: 0;
  padding: 0;
}
</style>