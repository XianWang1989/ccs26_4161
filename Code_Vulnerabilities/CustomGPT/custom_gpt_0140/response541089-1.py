
import tensorflow as tf
import numpy as np

# Sample data: context (words surrounding a target word)
context_data = [[0, 1, 2], [2, 3, 4]]  # Each sub-list is a context (input)
target_data = [[3], [2]]  # Corresponding target words

# Define parameters
vocab_size = 5
embedding_dim = 128

# Input and output placeholders
train_inputs = tf.placeholder(tf.int32, shape=[None, 3])  # Context size of 3
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# Reduce the embedding to a single vector for each input
embed = tf.reduce_mean(embed, axis=1)

# Output layer weights and biases
W = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
b = tf.Variable(tf.zeros([vocab_size]))

# Compute logits and predict
logits = tf.matmul(embed, W) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(train_labels), logits=logits))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Training the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example training loop
    for epoch in range(1000):  # Number of epochs
        feed_dict = {train_inputs: context_data, train_labels: target_data}
        _, l = sess.run([optimizer, loss], feed_dict=feed_dict)

        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {l}")

# Example output: Obtain word embeddings
trained_embeddings = sess.run(embeddings)
