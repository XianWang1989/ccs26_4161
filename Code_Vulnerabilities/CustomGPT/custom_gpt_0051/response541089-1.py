
import tensorflow as tf
import numpy as np

# Sample data: word indices for context and target
train_inputs = np.array([[1, 2], [2, 3], [1, 3]])  # context words
train_labels = np.array([[4], [4], [4]])            # target words

# Setting up parameters
vocab_size = 5  # size of your vocabulary
embedding_dim = 64

# Creating placeholders for inputs and labels
inputs = tf.placeholder(tf.int32, shape=[None, 2])  # two context words
labels = tf.placeholder(tf.int32, shape=[None, 1])  # one target word

# Defining the embedding matrix
embed_matrix = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Look up embeddings for context words
embedded_inputs = tf.nn.embedding_lookup(embed_matrix, inputs)

# Average the embeddings for context words
mean_embedding = tf.reduce_mean(embedded_inputs, axis=1)

# Output layer to predict target word probabilities
weights = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocab_size]))

logits = tf.matmul(mean_embedding, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(labels)))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Training the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    # You would typically run a loop over your data here
    for epoch in range(1000):
        feed_dict = {inputs: train_inputs, labels: train_labels}
        sess.run(train_op, feed_dict=feed_dict)
