
import tensorflow as tf
import numpy as np

# Sample data
# Let's assume we want to predict the target word based on its context words.
context_words = [0, 1, 2]  # Context words (indices)
target_word = [3]           # Target word (index)

# Hyperparameters
vocabulary_size = 10
embedding_size = 8

# Placeholder for context words
train_inputs = tf.placeholder(tf.int32, shape=[None, len(context_words)])  # Shape of input
train_labels = tf.placeholder(tf.int32, shape=[None, 1])                  # Shape of output

# Create embedding matrix
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))

# Lookup for context words
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# Average the embeddings across the context words
average_embed = tf.reduce_mean(embed, axis=1)

# Output layer weights and biases
W = tf.Variable(tf.random_uniform([embedding_size, vocabulary_size], -1.0, 1.0))
b = tf.Variable(tf.zeros([vocabulary_size]))

# Logits and prediction
logits = tf.matmul(average_embed, W) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))
optimizer = tf.train.AdamOptimizer().minimize(loss)

# Training loop (example setup)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example: Run one training step
    feed_dict = {
        train_inputs: [[context_words]],
        train_labels: [[target_word]]
    }
    _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)
    print("Loss:", loss_value)
