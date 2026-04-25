
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 10000  # Size of the vocabulary
embedding_dim = 128  # Dimension of the embedding vector
window_size = 2  # Context window size
num_sampled = 64  # Number of negative samples

# Sample data: list of context words (X) and target words (Y)
# X should be a list of lists containing context words
# Y should be the corresponding target word
X = [[1, 2], [2, 3], [3, 4]]  # Example input context words
Y = [[0], [1], [2]]  # Corresponding target words

# Define placeholders for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Define embeddings
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Define the weights and biases for output layer
weights = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
biases = tf.Variable(tf.zeros([vocab_size]))

# Compute logits and define loss function
logits = tf.matmul(embed, tf.transpose(weights)) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))

# Define the optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()

# Example training loop (using dummy data)
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(1000):
        _, l = sess.run([optimizer, loss], feed_dict={train_inputs: X, train_labels: Y})
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Loss: {l}")

# After training, you can retrieve the word embeddings
word_vectors = sess.run(embeddings)
