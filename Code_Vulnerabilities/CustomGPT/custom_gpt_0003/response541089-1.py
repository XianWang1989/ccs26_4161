
import numpy as np
import tensorflow as tf

# Sample data: let's say we have a simple dataset
context_words = [[1, 2, 3]]  # Context words (input)
target_words = [[4]]         # Target word (label)

# Parameters
vocab_size = 5  # Size of our vocabulary
embedding_dim = 2  # Dimension of the embedding vector

# Placeholders for input (context words) and output (target words)
X = tf.placeholder(tf.int32, shape=[None, None])  # Context input
Y = tf.placeholder(tf.int32, shape=[None, None])  # Target output

# Embedding Layer
embeddings = tf.Variable(tf.random_normal([vocab_size, embedding_dim]))
input_embeddings = tf.nn.embedding_lookup(embeddings, X)

# CBOW Model: Averaging the context embeddings
context_mean = tf.reduce_mean(input_embeddings, axis=1)

# Output Layer
W = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
b = tf.Variable(tf.random_normal([vocab_size]))
logits = tf.matmul(context_mean, W) + b

# Loss Function (Softmax Cross Entropy)
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(Y)))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Running the graph
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    # Example of training step (this would typically be in a loop with batches)
    feed_dict = {X: context_words, Y: target_words}
    _, loss_value = sess.run([optimizer, loss], feed_dict=feed_dict)

    print("Loss:", loss_value)
