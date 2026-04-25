
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 1000  # Size of vocabulary
embedding_size = 128  # Dimensions for word embeddings
window_size = 2  # Context window size
num_sampled = 64  # Number of negative samples

# Placeholder for the context (input words)
train_inputs = tf.placeholder(tf.int32, shape=[None])
# Placeholder for the target word (output word)
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
input_vectors = tf.nn.embedding_lookup(embeddings, train_inputs)

# Weights and biases for the output layer
weights = tf.Variable(tf.random_normal([vocab_size, embedding_size]))
biases = tf.Variable(tf.zeros([vocab_size]))

# CBOW model
logits = tf.matmul(input_vectors, weights, transpose_b=True) + biases
loss = tf.reduce_mean(tf.nn.sampled_softmax_loss(weights, biases, train_labels, input_vectors, num_sampled, vocab_size))

# Optimizer
optimizer = tf.train.AdamOptimizer().minimize(loss)

# Session to run the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # You would add your training loop here to feed in your data.
