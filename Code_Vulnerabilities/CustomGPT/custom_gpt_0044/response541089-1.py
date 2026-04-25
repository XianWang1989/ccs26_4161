
import tensorflow as tf
import numpy as np

# Sample data
context_words = np.array([[0, 1, 2], [2, 3, 4]])  # Example context words (input)
target_words = np.array([[1], [3]])                # Example target words (output)

# Hyperparameters
embedding_size = 128  # Size of the embedding vector
vocabulary_size = 5    # Size of the vocabulary
learning_rate = 0.01

# Input placeholders
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocabulary_size, embedding_size], -1.0, 1.0))
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# Reduce mean to create a single vector for context words
sum_embed = tf.reduce_mean(embed, axis=1)

# Output layer (softmax to produce probabilities)
weights = tf.Variable(tf.truncated_normal([embedding_size, vocabulary_size], stddev=0.1))
biases = tf.Variable(tf.zeros([vocabulary_size]))
logits = tf.matmul(sum_embed, weights) + biases

# Loss function and optimizer
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.squeeze(train_labels)))
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)

# Training process (example loop)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for epoch in range(1000):
        feed_dict = {train_inputs: context_words.flatten(), train_labels: target_words}
        _, l = sess.run([optimizer, loss], feed_dict=feed_dict)
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {l}')

# Use embeddings for further tasks
