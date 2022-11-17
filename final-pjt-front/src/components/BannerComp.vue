<template>
  <div>
    <div class="slide">
      <!-- https://bootstrap-vue.org/docs/components/carousel -->
      <b-carousel
        id="carousel-no-animation"
        style="text-shadow: 0px 0px 2px #000"
        no-animation
        indicators
        img-width="256"
        img-height="120"
      >
        <b-carousel-slide
          caption="First Slide"
          img-src="https://picsum.photos/1024/480/?image=10"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="Second Slide"
          img-src="https://picsum.photos/1024/480/?image=12"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="Third Slide"
          img-src="https://picsum.photos/1024/480/?image=22"
        ></b-carousel-slide>
        <b-carousel-slide
          caption="Fourth Slide"
          img-src="https://picsum.photos/1024/480/?image=23"
        ></b-carousel-slide>
      </b-carousel>
    </div>
  </div>
</template>

<script>
export default {
  name: 'BannerComp',
}
</script>

<style scoped>
.slide {
  display: inline-block;
  width: 80%;
}
</style>