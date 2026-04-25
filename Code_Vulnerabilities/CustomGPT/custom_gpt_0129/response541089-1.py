
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 5000  # Size of the vocabulary
embedding_dim = 128  # Dimension of the embedding vector
window_size = 2  # Context window size
num_epochs = 100  # Number of training epochs
learning_rate = 0.001

# Sample training data (context, target) pairs
# Example: context words ('the', 'cat') predicting target word ('sits')
train_data = np.array([[1, 2, 0], [3, 4, 2]])  # Context words (as indices)
train_labels = np.array([[0], [2]])  # Target words (as indices)

# Placeholders for inputs and labels
X = tf.placeholder(tf.int32, shape=[None, window_size * 2])  # Context words
Y = tf.placeholder(tf.int32, shape=[None, 1])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
input_embeddings = tf.nn.embedding_lookup(embeddings, X)

# Aggregate context word embeddings (average them)
context_embeddings = tf.reduce_mean(input_embeddings, axis=1)

# Output layer
W_out = tf.Variable(tf.random_uniform([embedding_dim, vocab_size], -1.0, 1.0))
b_out = tf.Variable(tf.zeros([vocab_size]))

# Logits and predictions
logits = tf.matmul(context_embeddings, W_out) + b_out
predictions = tf.nn.softmax(logits)

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(Y)))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(loss)

# Training
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(num_epochs):
        _, loss_value = sess.run([optimizer, loss], feed_dict={X: train_data, Y: train_labels})
        print(f'Epoch {epoch + 1}, Loss: {loss_value}')

    # Fetch the learned embeddings
    learned_embeddings = sess.run(embeddings)
    print("Embeddings for words in the vocabulary:")
    print(learned_embeddings)
