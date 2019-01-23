<template>
  <div class="container">
    <div class="main">
      <h1>茶 歇</h1>
      <h5>Tea Time</h5>
      <p>
        <router-link to="/digit_recognition">手写数字识别</router-link><br>
        <a href="https://webrtc.laravue.org/#/">一对一视频通话</a><br>
        <a href="https://mutilwebrtc.laravue.org/#/">多人视频通话</a><br>
        <!-- <router-link to="#" style="text-decoration: line-through;">上传图片检测性别</router-link> -->
      </p>
    </div>
    <div class="footer">
      <div style="text-align: center">
        <span style="color: #aaa">Developed By </span>
        <span><a href="https://github.com/zmecust">Min Zhang</a></span>
      </div>
    </div>
  </div>
</template>

<script>
export default {

};
</script>

<style lang="scss">
.main {
  text-align: center;
  margin-top: 15%;
  h5 {
    color: #aaa
  }
  p {
    padding-top: 3%;
    a {
      color: #00b5ad;
      font-weight: normal;
      font-size: 18px;
      &:hover, &:active {
        color: tomato;
      }
    }
  }
}

.footer {
  position: absolute;
  top: 95%;
  left: 0;
  width: 100%;
  a {
    color: #aaa;
    font-size: 14px;
    font-weight: bold
  }
}
</style>