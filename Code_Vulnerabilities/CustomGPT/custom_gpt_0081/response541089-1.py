
import tensorflow as tf
import numpy as np
import collections
import random
import math

# Sample data
sentences = ["the cat sat on the mat", "the dog sat on the rug"]
words = ' '.join(sentences).split()
vocab = set(words)
word_to_id = {w: i for i, w in enumerate(vocab)}
id_to_word = {i: w for i, w in enumerate(vocab)}
data = [word_to_id[word] for word in words]

# Hyperparameters
embedding_dim = 128
window_size = 2  # Window size for context
num_samples = 10000

# Generate training data for CBOW
def generate_cbow_data(words, window_size):
    context = []
    target = []
    for i in range(window_size, len(words) - window_size):
        context_words = []
        for j in range(1, window_size + 1):
            context_words.append(words[i - j])
            context_words.append(words[i + j])
        context.append([word_to_id[w] for w in context_words])
        target.append(words[i])
    return context, target

# Create input-output pairs
context, target = generate_cbow_data(data, window_size)

# Creating the model
train_inputs = tf.placeholder(tf.int32, shape=[None])  # Input context
train_labels = tf.placeholder(tf.int32, shape=[None, 1])  # Output target

# Variables
embeddings = tf.Variable(tf.random_uniform([len(vocab), embedding_dim], -1.0, 1.0))
embed = tf.nn.embedding_lookup(embeddings, train_inputs)

# Use the averaged context vectors for CBOW
average_context = tf.reduce_mean(embed, axis=1)

# Softmax weights and biases
weights = tf.Variable(tf.random_normal([embedding_dim, len(vocab)]))
biases = tf.Variable(tf.random_normal([len(vocab)]))

# Build the model
logits = tf.matmul(average_context, weights) + biases
cross_entropy = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.reshape(train_labels, [-1])))
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cross_entropy)

# Training session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(num_samples):
        _, loss = sess.run((optimizer, cross_entropy), feed_dict={train_inputs: context, train_labels: np.array(target).reshape(-1, 1)})
        if epoch % 1000 == 0:
            print(f"Epoch: {epoch}, Loss: {loss}")

print("Training finished.")
