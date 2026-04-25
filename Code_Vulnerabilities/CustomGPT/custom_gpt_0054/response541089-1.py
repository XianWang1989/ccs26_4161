
import tensorflow as tf
import numpy as np

# Parameters
embedding_size = 128  # Dimension of the embedding vector
vocab_size = 10000  # Size of the vocabulary
window_size = 2  # Size of the context window
num_sampled = 64  # Number of negative examples

# Inputs and Labels
train_inputs = tf.placeholder(tf.int32, shape=[None])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target words

# Variables
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# CBOW model: Average the context word embeddings
mean_embed = tf.reduce_mean(embed, axis=1)

# Softmax NCE loss
nce_weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_size], stddev=1.0 / tf.sqrt(embedding_size)))
nce_biases = tf.Variable(tf.zeros([vocab_size]))

loss = tf.reduce_mean(
    tf.nn.nce_loss(weights=nce_weights, biases=nce_biases, labels=train_labels, inputs=mean_embed, num_sampled=num_sampled, num_classes=vocab_size)
)

# Training operation
optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)

# Running the session
with tf.Session() as session:
    tf.global_variables_initializer().run()
    # Training loop here...
