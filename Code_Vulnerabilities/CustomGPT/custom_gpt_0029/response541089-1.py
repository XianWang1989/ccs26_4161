
import tensorflow as tf
import numpy as np

# Sample data: context (X) and target words (y)
context_words = [[0, 1], [1, 2], [2, 3], [3, 4]]  # Context input
target_words = [2, 3, 4, 5]  # Target labels

# Parameters
vocab_size = 6  # Total number of unique words
embedding_dim = 2  # Dimensions of word embeddings

# Placeholders for input and output
train_inputs = tf.placeholder(tf.int32, shape=[None])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embedded_inputs = tf.nn.embedding_lookup(embeddings, train_inputs)

# CBOW model: Average the embeddings for context words
context_mean = tf.reduce_mean(embedded_inputs, axis=1)

# Output layer weights and biases
weights = tf.Variable(tf.random_normal([embedding_dim, vocab_size]))
biases = tf.Variable(tf.zeros([vocab_size]))

# Logits for softmax
logits = tf.matmul(context_mean, weights) + biases
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=tf.reshape(train_labels, [-1]), logits=logits))

# Optimizer
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(loss)

# Training the model
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(1000):
        feed_dict = {train_inputs: context_words, train_labels: np.array(target_words).reshape(-1, 1)}
        _, l = sess.run([train_op, loss], feed_dict=feed_dict)
        if epoch % 100 == 0:
            print(f'Epoch {epoch}, Loss: {l}')

    trained_embeddings = sess.run(embeddings)

print("Trained embeddings:")
print(trained_embeddings)
