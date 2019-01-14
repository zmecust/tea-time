<template>
  <div class="container">
    <div class="title">
      <h2>手写数字识别</h2>
    </div>
    <div class="row">
      <div class="col-md-6 col-xs-12">
        <canvas id="main"></canvas>
        <div>
          <button class="btn btn-info" @click="submit">识别</button>
          <button class="btn btn-default" @click="clear">清除</button>
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
            <tr>
              <td>results</td>
              <td><span>{{ results[0] }}</span></td>
              <td><span>{{ results[1] }}</span></td>
            </tr>
          </tbody>
        </table>
        <div class="line"></div>
      </div>
    </div>
    <div class="row feed_back">
      <div class="col-md-5 col-xs-12">
        <div>
          <h5>请给我们反馈，以便改进模型，提高准确率...</h5>
          <div class="input-group">
            <input type="text" class="form-control" placeholder="您写入的数字是什么？" v-model="currentNumber">
            <span class="input-group-btn">
              <button class="btn btn-default" @click="feedback">反馈</button>
            </span>
          </div>
          <div class="alert alert-info" role="alert" v-show="this.inputs.length > 0 && showInfo">谢谢您的反馈，我们已收到</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Canvas from '../canvas';
import axios from 'axios';
import * as config from '../../config';
let canvas = Object;

export default {
  data() {
    return {
      num: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      inputs: [],
      feedForward: [],
      convolution: [],
      results: [],
      currentNumber: '',
      showInfo: false
    };
  },
  mounted() {
    canvas = new Canvas();
  },
  methods: {
    submit() {
      this.inputs = canvas.inputs;
      axios
        .post(`${config.API_ROOT}/recognition`, this.inputs)
        .then(res => {
          this.feedForward = this.transformer(res.data.results[0]);
          this.convolution = this.transformer(res.data.results[1]);
          this.results[0] = this.feedForward.indexOf(Math.max.apply(null, this.feedForward))
          this.results[1] = this.convolution.indexOf(Math.max.apply(null, this.convolution))
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
      return data.map(item => {
        return + item.toFixed(8);
      })
    },
    feedback() {
      this.currentNumber = '';
      this.showInfo = true;

      axios
        .post(`${config.API_ROOT}/feedback`, { image: this.inputs, label: this.currentNumber })
        .then(res => {})
        .catch(function(error) {
          console.log(error);
        });

      setTimeout(() => {
        this.showInfo = false;
      }, 3000);
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

.feed_back {
  margin-top: 20px;
}
</style>
