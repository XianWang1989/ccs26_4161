
import numpy as np
import tensorflow as tf

# Sample data
vocab_size = 10000
embedding_dim = 128

# Placeholder for input (context words) and output (target word)
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # CBOW expects a single target word

# Embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Lookup for context words
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average embeddings for CBOW
average_input = tf.reduce_mean(input_embeds, axis=0)

# Output layer
weights = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(tf.reshape(average_input, [1, -1]), weights) + biases

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(train_labels, [-1]), logits=logits))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(loss)

# Session to run the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Train your model here
