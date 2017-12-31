<template>
  <div class="container">
    <div class="title">
      <h2>手写数字识别</h2>
    </div>
    <div class="row">
      <div class="col-md-6 col-xs-12">
        <canvas id="main"></canvas>
        <div>
          <button class="btn btn-success" @click="submit">识别</button>
          <button class="btn btn-success" @click="clear">清除</button>
        </div>
      </div>
      <div class="col-md-6 col-xs-12">
        <canvas id="input" style="border: 1px solid; display: none" width="140" height="140"></canvas>
        <p>结果：</p>
        <table class="table table-hover" style="margin-bottom: 0; text-align: center">
          <thead>
            <tr>
              <th style="text-align: center">#</th>
              <th style="text-align: center">前馈神经网络</th>
              <th style="text-align: center">卷积神经网络</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="index in num" :key="index">
              <td>{{ index }}</td>
              <td>{{ feedForward[index] }}</td>
              <td>{{ convolution[index] }}</td>
            </tr>
            <!-- <tr>
              <td>results</td>
              <td><span>{{ results[0] }}</span></td>
              <td><span>{{ results[1] }}</span></td>
            </tr> -->
          </tbody>
        </table>
        <div class="line"></div>
      </div>
    </div>
  </div>
</template>

<script>
import Canvas from "./canvas";
import axios from "axios";
let canvas = Object;
const root = "http://localhost:5000";

export default {
  data() {
    return {
      num: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      inputs: [],
      feedForward: [],
      convolution: [],
      results: []
    };
  },
  mounted() {
    canvas = new Canvas();
  },
  methods: {
    submit() {
      this.inputs = canvas.inputs;
      axios
        .post(`${root}/recognition`, this.inputs)
        .then(res => {
          this.feedForward = this.transformer(res.data.results[0]);
          this.convolution = this.transformer(res.data.results[1]);
          this.results[0] = this.feedForward.indexOf(String(Math.max.apply(null, this.feedForward)))
          this.results[1] = this.convolution.indexOf(String(Math.max.apply(null, this.convolution)))
        })
        .catch(function(error) {
          console.log(error);
        });
    },
    clear() {
      canvas = new Canvas();
      this.inputs = [],
      this.feedForward = [],
      this.convolution = [],
      this.results = []
    },
    transformer(data) {
      return data.map((item) => {
        return item.toFixed(8);
      })
    }
  }
};
</script>

<style>
.title {
  text-align: center;
  margin: 5% 0 5%;
}

.line {
  border-top: 1px solid #ddd;
}

p {
  font-size: 20px;
  font-weight: bold;
}

span {
  color: red;
  font-weight: bold;
}
</style>
