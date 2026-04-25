
import tensorflow as tf
import numpy as np

# Sample data: context words and target words
context_words = np.array([[1, 2, 3], [3, 4, 5], [5, 6, 7]])  # Context input
target_words = np.array([[4], [5], [6]])  # Target output

# Parameters
vocab_size = 10  # Vocabulary size
embedding_dim = 8  # Dimension of embedding

# Placeholders
inputs = tf.placeholder(dtype=tf.int32, shape=[None, None])  # Context
labels = tf.placeholder(dtype=tf.int32, shape=[None, None])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embedded = tf.nn.embedding_lookup(embeddings, inputs)

# CBOW: Average of context word embeddings
context_mean = tf.reduce_mean(input_embedded, axis=1)

# Output layer
W = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
b = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(context_mean, W) + b

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(labels), logits=logits))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Initialize variables
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Train the CBOW model (example loop)
    for epoch in range(100):  # Number of epochs
        feed_dict = {inputs: context_words, labels: target_words}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch {epoch+1}, Loss: {loss_value}')

