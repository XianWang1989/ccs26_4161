
import tensorflow as tf
import numpy as np

# Parameters
vocab_size = 10000  # Set your vocabulary size
embedding_size = 128  # Dimension of the embedding vector
window_size = 2  # Context window size
num_sampled = 64  # Number of negative examples to sample

# Placeholder for input and output
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])  # Context
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Weights and biases for the output layer
weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_size], stddev=0.1))
biases = tf.Variable(tf.zeros([vocab_size]))

# CBOW model output
logits = tf.matmul(embed, weights, transpose_b=True) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.reshape(train_labels, [-1])))

# Optimizer
optimizer = tf.train.AdamOptimizer().minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()

# Start session
with tf.Session() as sess:
    sess.run(init)

    # Example input data (context and target)
    example_contexts = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
    example_targets = np.array([[4], [8]])  # Corresponding targets for the contexts

    # Training step
    for epoch in range(1000):  # Set the number of epochs
        feed_dict = {train_inputs: example_contexts, train_labels: example_targets}
        _, current_loss = sess.run([optimizer, loss], feed_dict=feed_dict)

        if epoch % 100 == 0:
            print('Epoch:', epoch, ' Loss:', current_loss)

    # Final embeddings
    trained_embeddings = sess.run(embeddings)
