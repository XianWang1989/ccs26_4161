
import tensorflow as tf
import numpy as np

# Sample data
train_inputs = np.array([[0, 1, 2], [1, 2, 3]])  # Context words
train_labels = np.array([[2], [3]])               # Target words

# Parameters
vocab_size = 4
embedding_dim = 2

# Placeholders for input and output
inputs = tf.placeholder(tf.int32, shape=[None, None])  # Context words
labels = tf.placeholder(tf.int32, shape=[None, 1])      # Target words

# Embedding layer
embed = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embedded_inputs = tf.nn.embedding_lookup(embed, inputs)

# Reduce over the context words
mean_embedded = tf.reduce_mean(embedded_inputs, axis=1)

# Output layer
weights = tf.Variable(tf.truncated_normal([embedding_dim, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))

# Logits and loss
logits = tf.matmul(mean_embedded, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(labels)))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01).minimize(loss)

# Training session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example of training loop
    for epoch in range(100):
        _, l = sess.run([optimizer, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        print(f'Epoch {epoch}, Loss: {l}')
