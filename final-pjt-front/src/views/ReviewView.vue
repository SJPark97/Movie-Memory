<template>
  <div>
    <div>
      <h5> REVIEW </h5>
    </div>
    <div class="review">



      <div class="title">
        <h1>{{ review.title }}</h1>
        <span @click="likeUnlike">
          <font-awesome-icon icon="fa-solid fa-heart" v-show="is_liked"/>
          <font-awesome-icon icon="fa-regular fa-heart"  v-show="!is_liked"/>
        </span>
        {{ like_users_count }}
        <p>작성자: {{ review.username }}</p>
        <span>작성일시 : {{ review?.created_at.substr(0, 10) }}</span>
        <span>수정일시 : {{ review?.updated_at.substr(0, 10) }}</span>
        <hr>
      </div>
      <div class="content">
        <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
        <h4>{{ review.content }}</h4>
      </div>
      <div class="comment-create">
        <hr>
        <h4>댓글 쓰기</h4>
        <form @submit.prevent="createComment">
          <input type="text" v-model.trim="comment">
          <input type="submit" value="작성">
        </form>
      </div>
      <CommentList />
    </div>
    <!-- <p>이 영화의 다른 리뷰 보기 (시간있으면 하겠음)</p>
    <div v-for="review in otherReview" :key="review.id">
      {{ review.title }}
    </div> -->
  </div>
</template>

<script>
import CommentList from '@/components/CommentList.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewView',
  components: {
    CommentList,
  },
  computed: {
    review() {
      return this.$store.state.review
    },
    otherReview() {
      return this.$store.state.movieReviews
    },
    is_liked() {
      if (this.$store.state.review.like_users.indexOf(this.$store.state.userId) === -1) {
        return false
      } else {
        return true
      }
    },
    like_users_count() {
      return this.$store.state.review.like_users.length
    },
  },
  data() {
    return {
      comment: null,
    }
  },
  methods: {
    getOneReview(reviewId) {
      this.$store.dispatch("getOneReview", reviewId)
    },
    getMovieReview(movie_id) {
      this.$store.dispatch("getMovieReview", movie_id)
    },
    getReviewComment(reviewId) {
      this.$store.dispatch("getReviewComment", reviewId)
    },
    createComment() {
      const content = this.comment
      const reviewPk = this.$route.params.review_id

      if (!content) {
        alert('내용을 입력하세요')
        return
      }

      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${reviewPk}/comments/`,
        headers: {
          'Authorization' : `Token ${this.$store.state.token}`
        },
        data: {content: content},
      })
        .then((response) => {
          console.log(response)
          this.getReviewComment(this.$route.params.review_id)
        })
        .catch((error) => {
          console.log(error)
        })
      this.comment = null
    },
    getReviewLike(movie_id) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/reviews/${movie_id}/likes/`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.is_liked = response.data.is_liked
          this.like_users_count = response.data.like_users_count
          this.$store.dispatch('getOneReview', this.$route.params.review_id)
        })
        .catch((error) => {
          console.log(error)
        })
      },
    likeUnlike() {
      this.getReviewLike(this.$route.params.review_id)
    },
  },
  created() {
    this.getOneReview(this.$route.params.review_id)
    this.getMovieReview(this.review.movie)
    this.$store.dispatch('getReviewComment', this.$route.params.review_id)
  }
}
</script>

<style scoped>

h5 {
  display: inline-block;
  position: relative;
  text-align: center;
  width: 150px;
  border-right: 1px solid black;
  border-left: 1px solid black;
}
.review {
  display: inline-block;
  position: relative;
  text-align: left;
  width: 70%;
  height: auto;
  /* border: 2px solid rgb(203, 120, 134); */
  /* border-top-left-radius: 30px; */
  /* border-bottom-right-radius: 30px; */
  /* box-shadow: 1px 1px 3px 3px rgb(136, 136, 136); */
  padding: 20px;
}
span {
  font-size: 10px;
  /* margin-left: 5px; */
  margin-right: 10px;
}
.title {
  display: inline-block;
  height: 100px;
  width: 80%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 50px;
}

.title > h1 {
  margin-bottom: 15px;
}

.title > p {
  margin: 0
}
.content {
  display: inline-block;
  width: 80%;
  margin-left: 30px;
  margin-right: 30px;

}

.content > img {
  width: 300px; 
}

.content > h4 {
  display: inline-block;
  vertical-align: top;
  margin-left: 30px;
  margin-right: 30px;
  margin-top: 20px;
  
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
</style>