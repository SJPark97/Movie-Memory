<template>
  <div>
    <div>
      <h2> REVIEW </h2>
    </div>
    <div class="review">
      <div class="title">
        <h1>{{ review.title }}</h1>

        <span @click="likeUnlike">
          <font-awesome-icon icon="fa-solid fa-heart" class="heart" v-show="is_liked"/>
          <font-awesome-icon icon="fa-regular fa-heart" class="heart" v-show="!is_liked"/>
        </span>
        겨우 {{ like_users_count }} 명이 좋아함

        <div class="back-to-movie">
          <div>
            <p><span class="name">작성자</span> |
              <router-link :to="`/${review.user}`" class="value">{{ review.username }}</router-link>
            </p>
          </div>
          <router-link :to="`/movies/${review.movie}`">목록</router-link>
        </div>

        <span class="day-name">작성일</span><span class="day">{{ review?.created_at.substr(0, 10) }}</span>
        <span class="day-name">수정일</span><span class="day">{{ review?.updated_at.substr(0, 10) }}</span>
        
        <br>

        <!-- 버튼 리뷰 작성자에게만 보임 -->
        <button 
          v-show="this.$store.state.userId === review.user" 
          @click="updateReview"
          class="update"
        >리뷰 수정</button>
        <ReviewUpdate v-show="popAva" @pop-exit="popExit" :review="review"/>

        <button 
          v-show="this.$store.state.userId === review.user" 
          @click="popAlert"
        >리뷰 삭제</button><br>
        <div v-show="alert" class="alert alert-danger" role="alert">
          정말 삭제하시겠습니까?<br>
          <button @click="noDelete" class="no">아니요</button>
          <button @click="DeleteReview(review.id, review.movie)">네</button>
        </div>

        <hr>
      </div>
      <div class="content">
        <img :src="`http://127.0.0.1:8000${review?.img}`" alt="">
        <h4>{{ review.content }}</h4>
      </div>
      <div class="comment-create">
        <hr>
        <h4>COMMENT</h4>
        <p v-if="this.$store.state.reviewComments">{{ this.$store.state.reviewComments.length }}개의 댓글이 있습니다.</p>
        <p v-else>댓글이 아직 없습니다.</p>
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
import ReviewUpdate from '@/components/ReviewUpdate.vue'
import axios from 'axios'

const API_URL = 'http://127.0.0.1:8000'

export default {
  name: 'ReviewView',
  components: {
    CommentList,
    ReviewUpdate,
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
      alert: false,
      popAva: false,
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
    popAlert() {
      this.alert = true
    },
    noDelete() {
      this.alert = false
    },
    DeleteReview(review_id, movie_id) {
      axios({
        method: 'delete',
        url: `${API_URL}/api/v1/reviews/${review_id}`,
        headers: {
          'Authorization': `Token ${this.$store.state.token}`
        },
      })
        .then((response) => {
          this.$router.push({name: 'movie_detail', params: {movie_id: movie_id}})
        })
        .catch((error) => {
          console.log(error)
        })
    },
    updateReview() {
      this.popAva = true
    },
    popExit() {
      this.popAva = false
    }
  },
  created() {
    this.getOneReview(this.$route.params.review_id)
    this.getMovieReview(this.review.movie)
    this.getReviewComment(this.$route.params.review_id)
    this.$store.dispatch('getReviewComment', this.$route.params.review_id)
    this.$store.dispatch('FirstFollow', this.$route.params.userId)
  }
}
</script>

<style scoped>

body {
  display: flex;
  justify-content: center;
}

hr {
  margin-top: 0; 
}
h2 {
  font-family: Harmond;
  color: rgb(0, 0, 0);
  text-shadow: 1px 1px #908581;

  display: inline-block;
  position: relative;
  text-align: center;
  width: 200px;
  border-right: 1px solid black;
  border-left: 1px solid black;
}
.review {
  display: inline-block;
  /* position: relative; */
  text-align: left;
  width: 80%;
  height: auto;
  /* border: 2px solid rgb(203, 120, 134); */
  /* border-top-left-radius: 30px; */
  /* border-bottom-right-radius: 30px; */
  /* box-shadow: 1px 1px 3px 3px rgb(136, 136, 136); */
  padding: 20px;
}
span {
  font-size: 15px;
  /* margin-left: 5px; */
  margin-right: 10px;
}

a {
  color: black;
  text-decoration: none;
}

button {
  border: 0px;
  background-color: transparent;
  color: red;
  padding: 0;
  font-size: 13px;
  margin-top: 10px;
  margin-bottom: 5px;
  margin-right: 20px;
  /* font-weight: bold; */
}

.update {
  color: rgb(58, 58, 248);
}

.heart {
  color: rgb(208, 93, 93);
  font-size: 2.5vw;
}

.back-to-movie {
  display: flex;
  justify-content: space-between;
  vertical-align: middle;
  margin: 0;
}

.back-to-movie > a {
  display: inline-block;
  height: 42px;
  background-color: #E6E6E6;
  /* border: 1px solid gray; */
  border-radius: 10px;
  padding: 10px;
  font-size: 15px;
}
.back-to-movie > a:hover {
  color: black;
  font-weight: bold;
}

.back-to-movie > div > p {
  font-size: 20px;
  margin: 0;
}
.no {
  color: blue
}

.title {
  display: inline-block;
  height: 100px;
  width: 90%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 50px;
}

.title > h1 {
  margin-bottom: 15px;
}

.title > p {
  font-size: 20px;
  /* margin-top: 5px;
  margin-bottom: 5px; */
  margin: 0;
}
.content {
  display: inline-block;
  width: 90%;
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
  width: 90%;
  text-align: left;
  margin-left: 30px;
  margin-right: 30px;
  margin-bottom: 20px;
  margin-top: 30px;
}

.comment-create > h4 {
  font-family: Harmond;
  color: rgb(0, 0, 0);
  text-shadow: 1px 1px #908581;

  display: inline-block;
  position: relative;
  text-align: center;
  width: 200px;
  border-right: 1px solid black;
  border-left: 1px solid black;
  margin-top: 10px;
  margin-bottom: 20px;
}

.comment-create > form > input[type='text'] {
  width: 40vw;
  height: 45px;
  border-radius: 10px;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  padding-left: 1vw;
}

.comment-create > form > input[type='submit'] {
  color: black;
  border: 1px solid gray;
  box-shadow: 1px 1px 1px 0px #908581;
  border-radius: 40%;
  padding-left: 10px;
  padding-right: 10px;
  height: 50px;
  margin-left: 10px;
  text-decoration: none;
  background-color: rgb(218, 210, 210);
}

.name {
  display: inline-block;
  width: 50px;
  text-align: left;
  font-weight: 600;
  margin-bottom: 20px;
}

.value {
  margin-left: 10px;
}

.day-name {
  display: inline-block;
  width: 37px;
  text-align: left;
  font-size: 13px;
  font-weight: 600;
}

.day {
  font-size: 13px;
  margin-right: 50px;
}
</style>