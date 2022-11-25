# FINAL PJT

영화 추천 알고리즘 기반 커뮤니티 서비스

### 🎞Movie Memory🎞

<br><br>

---

# Contributors 👨🏼‍🤝‍👨🏻
| Backend | Frontend |
|:------:|:------:|
||![yonghyun](https://user-images.githubusercontent.com/93974908/203923626-fe6bcfc9-6b77-4931-8219-6ca5b0f22195.png)|
| 🐊 박승재| 😎 조용현|


<br><br>

---

# 프로젝트 개요 📝

<br>

## 1️⃣ What

### 🤗 사용자 맞춤형 영화 추천 커뮤니티 🤗

▫ 사용자에게 1부터 10까지 전부 맞춘 취향 저격 영화 추천  
▫ 좋아하는 영화로 직접 꾸미는 영화 피드

<br>

## 2️⃣ For Whom

▫ 영화를 사랑하는 모든 사람들  
▫ 내가 본 영화에 대한 기록을 남기고 싶은 사람들  
▫ 추후 볼 영화를 저장해두고 싶은 사람들  
▫ 영화에 대한 다른 사람들의 평가와 감상이 궁금한 사람들

<br>

## 3️⃣ Why

▫ 국내 OTT 시장이 기하급수적으로 성장하며, 영화관에 가지 않고도 집에서 편하게 다양한 영화를 볼 수 있으며, 과거 또는 해외의 영화도 손쉽게 감상할 수 있다.

▫ 그러나 넷플릭스, 왓챠플레이 등 기존의 영화 OTT는 영화 시청에 그 목적이 있기 때문에 이미 감상한 영화에 대한 기록에 대해서는 부족함이 있다.

▫ OTT를 통해 집에서 감상하는 영화의 경우에는 티켓이 남지 않기 때문에 그 기록을 남기기가 쉽지 않다.

▫ 그렇기 때문에 감상한 영화를 기록하고 보관하는 일종의 다이어리의 필요성이 대두된다.

▫ 특히나 더더욱 영화를 사랑하고, 영화에 대한 후기와 감상평을 남기는 사람들에게는 자신이 시청한 영화와 그에 대한 리뷰를 한 번에 관리하고 열람할 수 있는 공간이 필요할 것이다.

<br>

## 4️⃣ How (목표 기능)

❶ 사용자 맞춤형 사이트이므로 로그인 유저를 대상으로 함

- 회원가입
- 로그인 & 로그아웃 & 프로필 정보 등록
- 회원 정보 수정

<br>

❷ 영화 추천 알고리즘

- 작성한 리뷰를 기반으로 한 사용자 맞춤형 추천
- 선호 장르별 추천
- 계절 및 날씨에 따른 추천

<br>

❸ 영화 열람 기능

- 전체 영화 목록
- 검색한 영화 목록
- 인기순, 최신순 영화 목록

<br>

❹ 개별 영화 정보

- 영화 제목, 포스터, 장르, 줄거리, 평점 등
- 영화별 리뷰 목록
- 영화 좋아요 (저장)

<br>

❺ 리뷰 작성
- 작성자만 수정, 삭제 가능
- 좋아요 (저장)
- 댓글 작성

<br>

❻ 사용자 프로필 및 리뷰 서랍

- 닉네임, 자기소개, 사진 
- 팔로우, 팔로잉
- 작성한 리뷰 피드
- 좋아요한 영화 목록
- 좋아요한 리뷰 목록

<br>

❼ 댓글 & 좋아요 알림

- 새 알림
- 이전 알림



<br><br>

---

# 프로젝트 기반

## 기술 스택
![image](https://user-images.githubusercontent.com/93974908/203924990-2d638811-0a8c-4f36-8edc-d5ac4f73f2ab.png)


![image](https://user-images.githubusercontent.com/93974908/203925060-0361b2a2-5ac2-4eb5-a60e-d014e864c00e.png)


<br>


## 프로젝트 활용 도구

notion
draw.io
github
figma

<br>


# 프로젝트 아키텍쳐


### 📋 ERD
![ERD](https://user-images.githubusercontent.com/93974908/203925328-0e7089ec-1d7b-43d3-a59d-bb0d0103246d.png)


<br>

### 📝 컴포넌트 구조  



<br>

### 🖌 Wireframe
(Figma 이용)   


![image](https://user-images.githubusercontent.com/93974908/203926613-289055b3-eccc-45f5-a074-d78badff4189.png)


![image](https://user-images.githubusercontent.com/93974908/203926790-6771edd1-2b5a-4584-bdf0-d4c866b6c390.png)


![image](https://user-images.githubusercontent.com/93974908/203926728-aefa104c-31c4-46be-a034-21751b645516.png)

![image](https://user-images.githubusercontent.com/93974908/203926844-7f9cce70-0463-410a-a083-dfc72e94b1de.png)


![image](https://user-images.githubusercontent.com/93974908/203926898-367a47f3-a8fc-4450-b23f-ae1ecc453774.png)

![image](https://user-images.githubusercontent.com/93974908/203926962-8330b56c-7b9b-4b54-8df1-4a61ceb2e39d.png)

<br><br>

---

# 기능 구현 🔧

GET 요청

|    기능명    |     URL(Back)    | Action | Mutation |
|:------------:|:----------------:|:-------:|:--------:|
| 전체 영화 조회 | `api/v1/movies/` | getMovies | GET_MOVIES |
| 영화 상세 | `api/v1/movies/<int:movie_pk>/`| getOneMovie | GET_ONE_MOVIE|
| 전체 리뷰 조회 |`api/v1/reviews/`|getReviews|GET_REVIEWS|
| 영화 리뷰 조회 | `api/v1/movies/<int:movie_pk>/reviews/` | getMovieReview| GET_MOVIE_REVIEWS |
| 리뷰 상세 |`api/v1/reviews/<int:review_pk>/`|getOneReview|GET_ONE_REVIEW|
| 리뷰 댓글 조회 |`api/v1/reviews/<int:review_pk>/comments/`|getReviewComment|GET_REVIEW_COMMENTS & NO_COMMENTS|
| 댓글 상세 |`api/v1/comments/<int:comment_pk>/`|getOneComment|GET_ONE_COMMENT|

| 계절별 영화 조회 |`api/v1/season/<int:season>/ `|getSeasonGenreMovie|GET_SEASON_MOVIE & SEASON_MOVIE_GENRE|
| 날씨별 영화 조회 |`api/v1/weather/<int:weather>/ `|getWeatherGenreMovie|GET_WEATHER_MOVIE & WEATHER_MOVIE_GENRE|


| 내 프로필 조회 |`accounts/user/myprofile/`|getUserInfo|GET_USER_INFO|
| 유저 리뷰 조회 |`api/v1/user/<int:user_pk>/reviews/`|MyReviews|MY_REVIEWS|
| 좋아요 한 영화 조회|`api/v1/movies/<int:user_pk>/like_movies/`|userLikedMovie|USER_LIKED_MOVIE|
|좋아요 한 리뷰 조회 |`api/v1/reviews/<int:user_pk>/like_reviews/`|userLikedReview|USER_LIKED_REVIEW|
| 유저 프로필 조회 |`accounts/user/<int:user_id>/profile/`|getProfile|GET_PROFILE|

|내 알람 조회 |`accounts/user/my_notice/`|getNotice|GET_NOTICE|
|||visitNoti||
|유저 맞춤 장르 영화 조회 |`accounts/user/genres_movies/`|getMyGenreMovie|GET_MY_GENRE_MOVIE|

| 랜덤 장르 영화 조회 |`api/v1/movies/genres/<int:random_num>/`|getRandomGenreMovie|GET_RANDOM_GENRE_MOVIE & RANDOM_MOVIE_GENRE|
|색다른 장르 영화 조회 |`accounts/user/new_kind_movies/`|getNewKindGenreMovie|GET_NEW_KIND_GENRE_MOVIE|
| 유저 팔로우 조회 |`accounts/user/<int:user_id>/profile/follow/`|FirstFollow|FIRST_FOLLOW|

<br>

POST 요청 
|    기능명    |     URL(Back)    | Action | Mutation |
|:------------:|:----------------:|:-------:|:--------:|
| 회원가입 | `accounts/signup/` | SignUp | SIGNUP_SAVE_TOKEN & LogIn |
| 로그인 | `accounts/login/` |logIn | LOGIN_SAVE_TOKEN & LogIn |
| 영화 좋아요 |`api/v1/movies/<int:movie_pk>/likes/`|||
|팔로우|`accounts/user/<int:user_id>/profile/follow/`|follow|FOLLOW|
|댓글 작성 |`api/v1/reviews/<int:review_pk>/comments/`|createComment||
| 리뷰 좋아요|`api/v1/reviews/<int:movie_pk>/likes/`|getReviewLike||
| 리뷰 삭제 |`api/v1/reviews/<int:review_pk>`|DeleteReview||

| 댓글 좋아요 |`api/v1/comments/<int:comment_pk>/likes/`|getCommentLike||
| 댓글 삭제 |`api/v1/comments/<int:comment_pk>/`|deleteComment||
| 댓글 수정 |`api/v1/comments/<int:comment_pk>/`|changeComment||

| 영화 좋아요 |`api/v1/movies/<int:movie_pk>/likes/`|getMovieLike||


|알림 삭제 |`accounts/user/delete_checked_notice/`|deleteCheckedNotices||
|리뷰 생성|`api/v1/movies/<int:movie_pk>/reviews/`|createReview||
|리뷰 수정|`api/v1/reviews/<int:review_pk>/`|updateReview||
|프로필 생성|`accounts/user/myprofile/`|setUserInfo||
|프로필 정보 수정 |`accounts/user/myprofile/`|setUserInfo||










1. 영화 목록 (찜)
2. 리뷰 목록 (좋아요)
3. 댓글 (대댓글, 좋아요)
4. 회원가입
5. 로그인 
6. 정보 찾기 (비밀번호 변경&찾기)
7. 추천영화 알고리즘
8. 계절(겨울)/날씨별 영화 추천
9. 검색 (자동완성, 포스터)
10. 리뷰&댓글 알림 (새 알림, 이전 알림, 모든 알림)



[TMDB API](https://developers.themoviedb.org/3/authentication/how-do-i-generate-a-session-id)

# Front

1. 홈페이지
2. 메인 추천 페이지
3. 영화 조회 페이지
4. 영화 디테일 페이지
5. 회원가입 (*3D모델링 예정*)
6. 로그인
7. 개인정보 수정
8. 프로필
9. 리뷰 작성 페이지

---
코드 모음 (스타일 가이드)



<br><br>

---

<br><br>

추천 알고리즘
1.
남, 여 나이대별로
신규 가입자가 좋아하는 콘텐츠와 성별 나이대의 영화를 결합해서 추천하는 방식

2.
신규 가입자가 좋아하는 콘텐츠와 리뷰를 작성한 장르를 종합해서
가장 많이 중복된 장르에서 랜덤으로 추천

3.
날씨별로 영화에 어울리는 날씨정보를 입력해서 오늘의 날씨에 해당하는 영화를
추출하여 사용자의 장르와 중복되는 영화들 중 랜덤 추출

4.
사용자가 잘 보지 않는 장르들과 보지 않은 영화에서 평점이 제일 높고 리뷰가 제일 많은 영화 추천
(이런 영화는 어떠신가요?)
