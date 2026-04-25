
import numpy as np
import tensorflow as tf

# Define parameters
vocabulary_size = 5000  # Size of your vocabulary
embedding_size = 128    # Dimension of the embedding vector
window_size = 2         # Context window size

# Placeholders for CBOW
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Variable for the embeddings
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

# Look up the embeddings for the input words
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the embeddings to create the context vector for CBOW
context_vector = tf.reduce_mean(input_embeddings, axis=1)

# Output weights and biases
output_weights = tf.Variable(tf.random_normal([vocabulary_size, embedding_size]))
output_biases = tf.Variable(tf.zeros([vocabulary_size]))

# Hidden layer to output layer
logits = tf.matmul(context_vector, tf.transpose(output_weights)) + output_biases

# Softmax output
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(loss)

# Initialization
init = tf.global_variables_initializer()

# Example: Training the model would go here
with tf.Session() as sess:
    sess.run(init)
    # Add your training loop here (e.g., feeding data into train_inputs and train_labels)

