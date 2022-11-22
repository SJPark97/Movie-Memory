<template>
  <div>
    <div class="content" v-if="!update">
      <p>{{ comment.content }}</p>
      <!-- <hr> -->
      <span>{{ comment.username }}</span>
      <span>{{ comment.created_at.substr(0, 10) }}</span>
      <span @click="likeUnlike">
        <font-awesome-icon icon="fa-solid fa-heart" class="heart" v-show="is_liked"/>
        <font-awesome-icon icon="fa-regular fa-heart" class="heart" v-show="!is_liked"/>
        {{ like_users_count }}
      </span>
    </div>

    <div class="comment-create" v-else>
      <form @submit.prevent="changeComment(comment.id)">
        <input type="text" v-model.trim="newComment">
        <input type="submit" value="작성">
      </form>
    </div>

      <div @click="popSelector" class="dot">
        <font-awesome-icon icon="fa-solid fa-ellipsis-vertical"/>
        <div v-show="selector" class="pop">
          <p @click="changeInput" class="pop-name">수정</p>
          <hr>
          <p @click="deleteComment(comment.id)" class="pop-name">삭제</p>
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
      update: false,
      newComment: this.comment.content
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
    changeInput() {
      this.update = true
    },
    changeComment(id) {
      const content = this.newComment
      const commentId = id

      if (!content) {
        alert('내용을 입력하세요')
        return
      }

      axios({
        method: 'put',
        url: `${API_URL}/api/v1/comments/${commentId}/`,
        headers: {
          'Authorization' : `Token ${this.$store.state.token}`
        },
        data: {content: content},
      })
        .then((response) => {
          console.log(response)
          this.$store.dispatch('getReviewComment', this.$route.params.review_id)
        })
        .catch((error) => {
          console.log(error)
        })
      this.update = false
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
  margin-top: 0;
  margin-left:8px;
  margin-right: 15px;
}

hr {
  margin-bottom: 0;
  margin-top: 0;
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
  margin-right: 17px;
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

.pop-name {
  font-size: 13px;
  margin: 0;
  margin-top: 3px;
  margin-bottom: 3px;
  padding: 0;
}


.pop-name:hover {
  cursor: pointer;
  font-weight: bold;
}

.comment-create {
  display: inline-block;
  width: 80%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 20px;
  margin-top: 30px;
}

.comment-create > form > input[type='text'] {
  width: 35vw;
  height: 50px;
  border-radius: 10px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  background-color: rgb(248, 241, 241);
  padding-left: 10px;
}

.comment-create > form > input[type='submit'] {
  color: black;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 40%;
  padding-left: 8px;
  padding-right: 8px;
  height: 45px;
  margin-left: 10px;
  text-decoration: none;
  background-color: rgb(218, 210, 210);
}
.heart {
  color: rgb(208, 93, 93);
}

</style>