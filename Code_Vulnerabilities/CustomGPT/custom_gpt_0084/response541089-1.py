
import tensorflow as tf
import numpy as np

# Sample data: context (input) and target (output)
context = np.array([[0, 1], [1, 2], [2, 3]])  # Example context of words
target = np.array([[1], [2], [3]])  # Example target words

# Parameters
vocab_size = 4  # Size of vocabulary
embedding_dim = 2  # Dimension of the embedding

# Placeholders for inputs and labels
train_inputs = tf.placeholder(tf.int32, shape=[None, 2])  # Context words
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Target word

# Embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_dim], -1.0, 1.0))
embed = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Output layer
weights = tf.Variable(tf.truncated_normal([vocab_size, embedding_dim], stddev=0.1))
biases = tf.Variable(tf.zeros([vocab_size]))

logits = tf.matmul(embed, weights, transpose_b=True) + biases
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=tf.one_hot(train_labels, vocab_size), logits=logits))

# Optimizer
optimizer = tf.train.AdamOptimizer(0.01).minimize(loss)

# Training
with tf.Session() as session:
    session.run(tf.global_variables_initializer())

    for epoch in range(1000):
        _, loss_value = session.run([optimizer, loss], feed_dict={train_inputs: context, train_labels: target})
        if epoch % 100 == 0:
            print(f'Epoch: {epoch}, Loss: {loss_value}')

# The embeddings can be accessed via session.run(embeddings)
