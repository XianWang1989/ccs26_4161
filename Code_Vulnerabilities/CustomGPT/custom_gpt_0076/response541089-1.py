
import tensorflow as tf
import numpy as np

# Sample data (word indices)
context = [[1, 2], [2, 3], [4, 5]]  # context words
target = [3, 4, 6]  # target words

# Hyperparameters
embedding_dim = 128
vocab_size = 10  # Adjust based on your corpus
num_sampled = 1  # Number of negative samples

# Placeholders for inputs and labels
X = tf.placeholder(tf.int32, shape=[None, 2])  # Context word IDs
y = tf.placeholder(tf.int32, shape=[None])      # Target word IDs

# Variables for embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Lookup embeddings for context
context_embeddings = tf.nn.embedding_lookup(embeddings, X)

# Average the context embeddings
average_context = tf.reduce_mean(context_embeddings, axis=1)

# Output layer weights and biases
W = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
b = tf.Variable(tf.zeros([vocab_size]))

# Compute logits
logits = tf.matmul(average_context, W, transpose_b=True) + b

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=y, logits=logits))
optimizer = tf.train.AdamOptimizer().minimize(loss)

# Training procedure
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(100):
        # Assume 'context' and 'target' contain batches of data
        feed_dict = {X: context, y: target}
        _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
        print(f'Epoch {epoch}: Loss = {loss_value}')

