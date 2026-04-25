
import tensorflow as tf
import numpy as np

# Example data: context words (inputs) and target words (labels)
context_words = [[0, 1], [1, 2], [0, 2]]  # input context (two words)
target_words = [2, 0, 1]  # corresponding target words

# Parameters
vocabulary_size = 3
embedding_dim = 2

# Placeholders for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dim], -1.0, 1.0))
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Calculate the mean of input embeddings (CBOW)
mean_input = tf.reduce_mean(input_embeddings, axis=1)

# Output layer
weights = tf.Variable(tf.random_uniform([embedding_dim, vocabulary_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocabulary_size]))
logits = tf.matmul(mean_input, weights) + biases

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))
optimizer = tf.train.SimpleGradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Session to run the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example training loop
    for epoch in range(100):
        feed_dict = {train_inputs: [0, 1], train_labels: [[2], [0]]}  # Example batch
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch: {epoch}, Loss: {loss_value}')
