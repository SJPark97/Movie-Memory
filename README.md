# Final_PJT

# Back

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

URL 정리
- 영화 조회: api/v1/movies/
- 계절별 영화 조회: api/v1/season/<int:season>/    (1: 봄, 2: 여름, 3: 가을, 4: 겨울)
- 날씨별 영화 조회: api/v1/weather/<int:weather>/    (1: 화창, 2: 흐림, 3: 비, 4:눈)
- 영화 상세: api/v1/movies/<int:movie_pk>/
- 영화 리뷰 조회: api/v1/movies/<int:movie_pk>/reviews/
- 영화 좋아요: api/v1/movies/<int:movie_pk>/likes/
- 내가 리뷰 많이 쓴 장르 영화 조회: accounts/user/genres_movies/
- 내가 평소 즐기지 않는 색다른 영화 조회: accounts/user/new_kind_movies/
- 내 알람 조회: accounts/user/my_notice/
- 내 알람 조회시 방문처리: accounts/user/<int:notice_id>/change_notice/
- 좋아요 한 영화 조회: api/v1/movies/<int:user_pk>/like_movies/
- 리뷰 조회: api/v1/reviews/
- 리뷰 상세: api/v1/reviews/<int:review_pk>/
- 리뷰 만들기: api/v1/movies/<int:movie_pk>/reviews/
- 리뷰 좋아요: api/v1/reviews/<int:review_pk>/likes/
- 좋아요 한 리뷰 조회: api/v1/reviews/<int:user_pk>/like_reviews/
- 유저 리뷰 조회: : api/v1/user/<int:user_pk>/reviews/
- 댓글 조회: api/v1/comments/
- 댓글 상세: api/v1/comments/<int:comment_pk>/
- 댓글 만들기: api/v1/reviews/<int:review_pk>/comments/
- 댓글 좋아요: api/v1/comments/<int:comment_pk>/likes/
- 유저 댓글 조회: : api/v1/user/<int:user_pk>/comments/
- 리뷰 댓글 조회: api/v1/reviews/<int:review_pk>/comments/
- 계정 로그인: accounts/login/
- 계정 로그아웃: accounts/logout/
- 계정 정보 수정: accounts/user/
- 내 프로필 생성, 조회, 수정: accounts/user/myprofile/
- 유저 프로필 조회: accounts/user/<int:user_id>/profile/
- 유저 좋아요: accounts/user/<int:user_id>/profile/follow/
- 계정 생성: accounts/signup/
- 계정 생성 이메일 재전송: accounts/signup/resend-email/
- 계정 생성 이메일 확인: accounts/signup/verify-email/
- 계정 비밀번호 체인지: accounts/password/change/
- 계정 비밀번호 리셋: accounts/password/reset/
- 계정 비밀번호 리셋 확인: accounts/password/reset/confirm/


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

# 프로젝트 개요

<br>

## 1️⃣ What
### 사용자 맞춤형 영화 추천 커뮤니티  
▫ 사용자에게 1부터 10까지 전부 맞춘 취향 저격 영화 추천  
▫ 좋아하는 영화로 직접 꾸미는 영화 프로필   

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

## 4️⃣ How

▫ 사용자 맞춤형 사이트이므로 로그인 유저를 대상으로 함
- 회원가입
- 로그인 & 로그아웃
- 회원 정보 수정


▫ 영화 추천 알고리즘
- 작성한 리뷰를 기반으로 한 사용자 맞춤형 추천
- 선호 장르별 추천
- 계절 및 날씨에 따른 추천


▫ 영화 열람 기능 
- 전체 영화 목록
- 리뷰를 작성한 영화 목록
- 리뷰를 작성하지 않은 영화 목록
- 검색한 영화 목록 


▫ 개별 영화 정보
- 영화 제목, 포스터, 장르, 줄거리, 감독, 배우, 평점 등
- 영화별 리뷰 목록  


▫ 리뷰 작성, 좋아요, 댓글 작성


▫ 사용자 프로필 및 리뷰 서랍   
- 닉네임, 자기소개, 사진
- 작성한 리뷰 피드
- 좋아요한 영화 목록
- 좋아요한 리뷰 목록


▫ 댓글 & 좋아요 알림
- 새 알림
- 이전 알림
- 모든 알림




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
