from flask import request, Flask, jsonify, render_template
from flask_cors import *
import numpy as np
import tensorflow as tf

from mnist import model


x = tf.placeholder("float", [None, 784])
sess = tf.Session()

# restore trained data
with tf.variable_scope("regression"):
    y1, variables = model.regression(x)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/regression.ckpt")


with tf.variable_scope("convolutional"):
    keep_prob = tf.placeholder("float")
    y2, variables = model.convolutional(x, keep_prob)
saver = tf.train.Saver(variables)
saver.restore(sess, "mnist/data/convolutional.ckpt")


def regression(input):
    return sess.run(y1, feed_dict={x: input}).flatten().tolist()


def convolutional(input):
    return sess.run(y2, feed_dict={x: input, keep_prob: 1.0}).flatten().tolist()


app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route('/recognition', methods=['POST'])
def recognition():
    input = ((255 - np.array(request.json, dtype=np.uint8)) / 255.0).reshape(1, 784)
    output1 = regression(input)
    output2 = convolutional(input)
    return jsonify(results=[output1, output2])

@app.route('/feedback', methods=['POST'])
def feedback():
    # saveSample.save(request.json.image, request.json.label)
    return jsonify(results='we got the feedback, thanks!')

if __name__ == '__main__':
    app.run(host='0.0.0.0')