
import numpy as np
import tensorflow as tf

# Assuming you have some preprocessing to create your dataset
# Let's say `context_words` is an array of context words for each target word
# and `target_words` is the corresponding target word for each example.

# Example data
context_words = np.array([[1, 2], [3, 4], [2, 3]])  # context words (2 per example)
target_words = np.array([[0], [3], [2]])  # target words

# Define placeholders for the inputs and targets
train_inputs = tf.placeholder(tf.int32, shape=[None, 2])  # CBOW takes 2 context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # target words

# Model parameters
vocab_size = 10  # Just an example
embedding_size = 128  # Size of the embedding vector

# Lookup embeddings for context words
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))

# Get embeddings for context words
input_embeddings = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the context embeddings to create the input for the output layer
average_embeddings = tf.reduce_mean(input_embeddings, axis=1)

# Output layer
W = tf.Variable(tf.random_normal([embedding_size, vocab_size]))
b = tf.Variable(tf.zeros([vocab_size]))

# Logits and loss
logits = tf.matmul(average_embeddings, W) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.squeeze(train_labels), logits=logits))

# Training step
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_step = optimizer.minimize(loss)

# Initialize all variables
init = tf.global_variables_initializer()

# Example of running the training
with tf.Session() as sess:
    sess.run(init)
    # You would typically loop over your dataset here
    # for epoch in range(training_epochs):
    #     sess.run(train_step, feed_dict={train_inputs: context_words, train_labels: target_words})

    print("Model trained successfully!")

