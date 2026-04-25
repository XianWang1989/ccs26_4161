
import numpy as np
import tensorflow as tf

# Example parameters
vocab_size = 5000
embedding_size = 128
window_size = 2  # Number of context words

# Placeholder for context words (inputs) and target word (label)
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])  # context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
embedded_inputs = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Output layer
weights = tf.Variable(tf.random_normal([embedding_size, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))
logits = tf.matmul(embedded_inputs, weights) + biases

# Loss and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Initialize variables
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example training data (context: [1, 2, 3], target: [4])
    example_inputs = np.array([[1, 2, 3, 2, 3, 4]])
    example_labels = np.array([[4]])

    # Train step
    feed_dict = {train_inputs: example_inputs, train_labels: example_labels}
    loss_value, _ = sess.run([loss, optimizer], feed_dict=feed_dict)

    print("Loss:", loss_value)
