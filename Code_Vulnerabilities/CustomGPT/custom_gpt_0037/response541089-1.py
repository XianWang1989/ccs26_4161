
import tensorflow as tf
import numpy as np

# Parameters
vocabulary_size = 5000
embedding_size = 128
window_size = 2
num_samples = 10000  # Number of training examples

# Placeholder for input context words and target words
train_inputs = tf.placeholder(tf.int32, shape=[None, window_size * 2])
train_labels = tf.placeholder(tf.int32, shape=[None, 1])

# Embedding layer
embeddings = tf.Variable(tf.random_normal([vocabulary_size, embedding_size]))

# Look up embeddings for context words
input_embeddings = tf.reduce_mean(tf.nn.embedding_lookup(embeddings, train_inputs), axis=1)

# Output layer
output_weights = tf.Variable(tf.random_normal([vocabulary_size, embedding_size]))
output_biases = tf.Variable(tf.random_normal([vocabulary_size]))

# Logits and loss
logits = tf.matmul(input_embeddings, tf.transpose(output_weights)) + output_biases
loss = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=logits, labels=tf.reshape(train_labels, [-1]))

# Optimizer
optimizer = tf.train.AdamOptimizer(learning_rate=0.01).minimize(loss)

# Example data preparation for CBOW
def create_cbow_data(sentences):
    train_data = []
    for sentence in sentences:
        words = sentence.split()
        for i in range(window_size, len(words) - window_size):
            context = words[i - window_size:i] + words[i + 1:i + window_size + 1]
            target = words[i]
            train_data.append((context, target))
    return train_data

# Dummy sentences for example
sentences = ["the quick brown fox jumps", "over the lazy dog"]
train_data = create_cbow_data(sentences)

# Convert to indices (not shown here, assume you have a mapping)
# train_inputs_data, train_labels_data = ...

# Sample training loop (simplified)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for epoch in range(num_epochs):
        # Feed the data into the model
        # sess.run(optimizer, feed_dict={train_inputs: train_inputs_data, train_labels: train_labels_data})

print("CBOW model built successfully!")
