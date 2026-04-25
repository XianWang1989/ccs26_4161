
import numpy as np
import tensorflow as tf

# Sample data (context words and target words)
context_words = np.array([[1, 2], [2, 3], [3, 4]])  # Example context words
target_words = np.array([[0], [1], [1]])  # Corresponding target words

# Parameters
vocab_size = 5
embedding_dim = 32

# Placeholder for input
train_inputs = tf.placeholder(tf.int32, shape=[None, 2])  # Context word pairs
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target words

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Look up embeddings for the context words
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the embeddings of the context words
average_embeddings = tf.reduce_mean(input_embeddings, axis=1)

# Output layer
weights = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocab_size]))

# Logits
logits = tf.matmul(average_embeddings, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))

# Optimizer
optimizer = tf.train.AdamOptimizer(0.001)
train_op = optimizer.minimize(loss)

# Initialize variables
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example of training
    for epoch in range(1000):
        _, loss_value = sess.run([train_op, loss], feed_dict={train_inputs: context_words, train_labels: target_words})
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {loss_value}")

# Note: Replace context_words and target_words with your actual training data.
