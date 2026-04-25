
import tensorflow as tf
import numpy as np

# Sample data: context words and target words
context_words = [[0, 1, 2], [1, 2, 3]]  # Example context (input)
target_words = [[3], [4]]  # Example targets (output)

# Parameters
vocabulary_size = 5
embedding_dimension = 8
batch_size = len(context_words)

# Create placeholders for input and output
train_inputs = tf.placeholder(tf.int32, shape=[batch_size, 3])  # 3 context words
train_labels = tf.placeholder(tf.int32, shape=[batch_size, 1])   # 1 target word

# Define embeddings
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dimension], -1.0, 1.0))

# Look up the embeddings for the context words
input_embeds = tf.nn.embedding_lookup(embeddings, train_inputs)

# Reduce mean to get a single vector for the context
mean_input = tf.reduce_mean(input_embeds, axis=1)

# Output layer weights and biases
weights = tf.Variable(tf.random_uniform([embedding_dimension, vocabulary_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocabulary_size]))

# Compute logits
logits = tf.matmul(mean_input, weights) + biases

# Loss function and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(train_labels), logits=logits))
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Initialize variables and run the session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # Example training loop
    for epoch in range(1000):
        _, loss_value = sess.run([optimizer, loss], feed_dict={train_inputs: context_words, train_labels: target_words})
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value}')
