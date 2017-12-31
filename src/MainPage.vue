<template>
  <div>
    <canvas id="main"></canvas>
  </div>
</template>

<script>
import canvas from './canvas';

export default {
  mounted() {
    new canvas();
  }
}
</script>
