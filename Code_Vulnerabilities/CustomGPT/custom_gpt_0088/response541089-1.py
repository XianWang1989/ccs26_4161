
import tensorflow as tf
import numpy as np

# Sample data: context words and target words
context_words = [[0, 1], [1, 2], [2, 3]]  # context (input)
target_words = [[2], [3], [4]]  # target (output)

# Parameters
vocab_size = 5
embedding_size = 2

# Create placeholders for inputs and outputs
X = tf.placeholder(tf.int32, shape=[None, 2])  # context words
Y = tf.placeholder(tf.int32, shape=[None, 1])  # target words

# Embedding layer
W = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))

# Compute embeddings for context words
embeddings = tf.nn.embedding_lookup(W, X)

# Average the embeddings
context_embeddings = tf.reduce_mean(embeddings, axis=1)

# Output layer
W_out = tf.Variable(tf.random_uniform([embedding_size, vocab_size], -1.0, 1.0))
b_out = tf.Variable(tf.zeros([vocab_size]))

# Logits and loss
logits = tf.matmul(context_embeddings, W_out) + b_out
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(Y), logits=logits))

# Training step
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Training loop
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(1000):
        feed_dict = {X: context_words, Y: target_words}
        _, loss_value = sess.run([train_op, loss], feed_dict=feed_dict)
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value}')
