
import tensorflow as tf
import numpy as np

# Parameters
vocabulary_size = 10000  # Adjust this based on your vocab size
embedding_size = 128     # Dimension of embedding vector
num_sampled = 64         # Number of negative samples
window_size = 2          # Context window size

# Placeholder for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Define the embeddings
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

# Look up embeddings for inputs
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Get weights and biases for the output layer
weights = tf.Variable(tf.truncated_normal([vocabulary_size, embedding_size], stddev=1.0 / np.sqrt(embedding_size)))
biases = tf.Variable(tf.zeros([vocabulary_size]))

# Compute the logits
logits = tf.matmul(input_embeddings, weights, transpose_b=True) + biases

# Define loss function, e.g., using sampled softmax
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(train_labels, [-1]), logits=logits))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(1.0).minimize(loss)

# Training process (example)
with tf.Session() as session:
    session.run(tf.global_variables_initializer())
    # Suppose train_data contains input-output pairs for training CBOW
    for inputs, labels in train_data:
        feed_dict = {train_inputs: inputs, train_labels: labels}  # Note the usage of labels
        session.run(optimizer, feed_dict=feed_dict)
