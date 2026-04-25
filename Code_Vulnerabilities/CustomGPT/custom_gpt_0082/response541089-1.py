
import tensorflow as tf
import numpy as np

# Sample data: context words and target word
context_words = [[1, 2, 3], [2, 3, 4]]  # Example context (CBOW with 3 context words)
target_words = [[0], [1]]  # Corresponding target words

# Parameters
vocab_size = 10
embedding_dim = 8

# Placeholders for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None, 3])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])   # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_normal([vocab_size, embedding_dim]))

# Look up the embeddings for context words
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Output layer
W = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
b = tf.Variable(tf.zeros([vocab_size]))

# Logits and loss
logits = tf.matmul(embed, W) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=train_labels, logits=logits))

# Optimizer
optimizer = tf.train.AdamOptimizer(0.01).minimize(loss)

# Initialize variables and run the session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example training loop (pseudo-code)
    for epoch in range(1000):
        # Randomly select a context and corresponding target word for training
        # feed_dict = {train_inputs: context_data, train_labels: target_data}
        # sess.run(optimizer, feed_dict=feed_dict)

    # After training, you can extract the embeddings
    trained_embeddings = sess.run(embeddings)

print("Trained embeddings:", trained_embeddings)
