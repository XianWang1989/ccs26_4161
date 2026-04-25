
import tensorflow as tf
import numpy as np

# Sample data: context (input) and target (label)
train_inputs = np.array([[1, 2, 3],  # Context words for target '4'
                         [0, 2, 4]])  # Context words for target '1'
train_labels = np.array([[0, 0, 0, 1, 0],  # One-hot encoding for target '4'
                         [1, 0, 0, 0, 0]])  # One-hot encoding for target '1'

# Define model parameters
vocabulary_size = 5
embedding_dimension = 2

# Build the CBOW model
inputs = tf.placeholder(tf.int32, shape=[None, 3])  # Input for context words
labels = tf.placeholder(tf.float32, shape=[None, vocabulary_size])  # Target labels

# Initialize the weight matrix and bias
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_dimension], -1.0, 1.0))
context_embeddings = tf.nn.embedding_lookup(embeddings, inputs)

# Average the context word embeddings to create a single vector
average_context = tf.reduce_mean(context_embeddings, axis=1)

# Build the output layer
W = tf.Variable(tf.random_normal([embedding_dimension, vocabulary_size]))
b = tf.Variable(tf.random_normal([vocabulary_size]))

# Compute logits and loss
logits = tf.matmul(average_context, W) + b
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=labels, logits=logits))

# Define the optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Start the session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example training loop
    for epoch in range(1000):
        _, loss_value = sess.run([optimizer, loss], feed_dict={inputs: train_inputs, labels: train_labels})
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {loss_value}')
