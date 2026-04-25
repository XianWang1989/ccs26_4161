
import numpy as np
import tensorflow as tf

# Parameters
vocab_size = 5000
embedding_size = 128
num_sampled = 64  # Number of negative samples
window_size = 2

# Example data: sentences as lists of word indices
sentences = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]  # Example word indices
train_inputs, train_labels = [], []

# Creating training data for CBOW
for sentence in sentences:
    for target_index in range(len(sentence)):
        context_indices = list(range(max(0, target_index - window_size), 
                                      min(len(sentence), target_index + window_size + 1)))
        context_indices.remove(target_index)

        for word_index in context_indices:
            train_inputs.append(sentence[target_index])  # Target word
            train_labels.append(sentence[word_index])  # Context word

# Convert to numpy arrays
train_inputs = np.array(train_inputs)
train_labels = np.array(train_labels)

# Placeholder for inputs and labels
X = tf.placeholder(tf.int32, shape=[None])
Y = tf.placeholder(tf.int32, shape=[None])

# Define the embedding layer
embeddings = tf.Variable(tf.random_uniform([vocab_size, embedding_size], -1.0, 1.0))

# Look up embeddings for the inputs
embed = tf.nn.embedding_lookup(embeddings, X)

# Define the weights and biases
W = tf.Variable(tf.truncated_normal([vocab_size, embedding_size], stddev=0.1))
b = tf.Variable(tf.zeros([vocab_size]))

# CBOW model
logits = tf.matmul(embed, W) + b
loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=Y, logits=logits))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Training session
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(100):
        _, loss_value = sess.run([optimizer, loss], feed_dict={X: train_inputs, Y: train_labels})
        print(f'Epoch {epoch}: Loss = {loss_value}')
