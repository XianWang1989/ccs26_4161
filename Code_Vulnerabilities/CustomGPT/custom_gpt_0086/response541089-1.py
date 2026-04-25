
import tensorflow as tf
import numpy as np

# Sample data (context words and corresponding target words)
context_words = [[0, 1], [1, 2], [2, 3]]  # Example context word indices
target_words = [2, 3, 4]  # Example target word indices

# Parameters
vocab_size = 5
embedding_dim = 3
batch_size = len(context_words)

# Create placeholders for inputs and labels
inputs = tf.placeholder(tf.int32, shape=[None, 2])  # Context words
labels = tf.placeholder(tf.int32, shape=[None])      # Target words

# Create embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))

# Lookup the embeddings for context words
embed_inputs = tf.nn.embedding_lookup(embeddings, inputs)

# Ensure we average the embeddings for CBOW
cbow = tf.reduce_mean(embed_inputs, axis=1)

# Weights and biases for output layer
Weights = tf.Variable(tf.truncated_normal([embedding_dim, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))

# Logits and predictions
logits = tf.matmul(cbow, Weights) + biases
predictions = tf.nn.softmax(logits)

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=labels))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Training loop (placeholder for actual training logic)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(100):  # Number of epochs
        _, l = sess.run([optimizer, loss], feed_dict={inputs: context_words, labels: target_words})
        print(f'Epoch {epoch}, Loss: {l}')
